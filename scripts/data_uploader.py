import argparse
from ch_saver import DatabaseClickhouseConnector
import os
import dask.dataframe as dd
import pandas as pd


URL_CONNECTION_CH = os.getenv("url_ch", "tis5000.vniizht.lan")
PORT_CONNECTION_CH = os.getenv("port_ch", 9010)
DB_CH = os.getenv("db_ch", "hakaton")
TABLE_TELEMETRY_CH = os.getenv("table_telemetry_ch", "telemetry")
TABLE_PREDICT_M1_CH = os.getenv("table_predict_m1_ch", "predict_m1")
TABLE_PREDICT_M1_TO_FAILURE_CH = os.getenv("table_predict_m1_to_failure_ch", "predict_m1_to_failure")
USER_CH = os.getenv("user_ch", "hakaton")
PASSWORD_CH = os.getenv("password_ch", "hakatoN420M3haK")


rename_params = {
    'ВИБРАЦИЯ НА ОПОРЕ 1': 'vibration_on_support_1',
    'ВИБРАЦИЯ НА ОПОРЕ 2': 'vibration_on_support_2',
    'ВИБРАЦИЯ НА ОПОРЕ 3': 'vibration_on_support_3',
    'ВИБРАЦИЯ НА ОПОРЕ 4': 'vibration_on_support_4',
    'ВИБРАЦИЯ НА ОПОРЕ 3. ПРОДОЛЬНАЯ.': 'vibration_on_support_3_prodol',
    'ВИБРАЦИЯ НА ОПОРЕ 4. ПРОДОЛЬНАЯ.': 'vibration_on_support_4_prodol',
    'ДАВЛЕНИЕ МАСЛА В СИСТЕМЕ': 'oil_pressure_system',
    'ТЕМПЕРАТУРА МАСЛА В МАСЛОБЛОКЕ': 'oil_temp_oil_block',
    'ТЕМПЕРАТУРА МАСЛА В СИСТЕМЕ': 'oil_temp_system',
    'ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 1': 'bearing_temp_on_support_1',
    'ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 2': 'bearing_temp_on_support_2',
    'ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 3': 'bearing_temp_on_support_3',
    'ТЕМПЕРАТУРА ПОДШИПНИКА НА ОПОРЕ 4': 'bearing_temp_on_support_4',
    'ТОК РОТОРА 1': 'rotor_current_1',
    'ТОК РОТОРА2': 'rotor_current_2',
    'ТОК СТАТОРА': 'stator_current_2'
}

order_cols = ['dt', 'machine_number', 'rotor_current_1', 'rotor_current_2', 'stator_current_2',
       'oil_pressure_system', 'bearing_temp_on_support_1',
       'bearing_temp_on_support_2', 'bearing_temp_on_support_3',
       'bearing_temp_on_support_4', 'oil_temp_system', 'oil_temp_oil_block',
       'vibration_on_support_1', 'vibration_on_support_2',
       'vibration_on_support_3', 'vibration_on_support_3',
       'vibration_on_support_4', 'vibration_on_support_4']


def loader_data_telemetry(args):
    data = dd.read_parquet(args.filename)
    cols = data.columns
    col_for_upload = [col for col in cols if "ЭКСГАУСТЕР 4." in col]
    cols_new = {col: rename_params[col.split(". ")[1]] for col in col_for_upload}
    cols_new["DT"] = "dt"
    data_by_machine = dd.read_parquet(args.filename, columns=col_for_upload)
    result = (data_by_machine
              .reset_index()
              .rename(columns=cols_new)
              .assign(machine_number=4)
    ).compute()
    result.interpolate(inplace=True)
    result = result[order_cols]
    result.fillna(method="backfill", inplace=True)
    return result


def loader_preds_m1_to_failure(args):
    result_task_3 = pd.read_csv(args.filename)
    result_task_3 = (result_task_3
        .rename(columns={"DT": "dt"})
        .assign(machine_number=int(args.machine))
        .reindex(columns=['dt', 'machine_number', 'time_to_m1_seconds'])
        .assign(dt=lambda x:  pd.to_datetime(x["dt"]))
    )
    return result_task_3


def loader_preds_m1_test_intervals(args):
    result_task_1 = pd.read_csv(args.filename)
    result_task_1 = (
        result_task_1
        .drop(columns=["Unnamed: 0"])
        .rename(columns={
            f"preds_proba_{args.machine}": "preds_proba",
            f"preds_label_{args.machine}": "preds_label",
            "start": "dt_start",
            "finish": "dt_end"
        })
        .assign(machine_number=int(args.machine))
        .reindex(columns=['dt_start', 'dt_end', 'machine_number', 'preds_proba', 'preds_label'])
    )
    result_task_1["dt_start"] = pd.to_datetime(result_task_1["dt_start"])
    result_task_1["dt_end"] = pd.to_datetime(result_task_1["dt_end"])
    return result_task_1


def main_uploader(args):
    print(f"type - {args.type}, file - {args.filename}, machine - {args.machine}")
    print("prepare data")
    result = None
    tabel = None
    if args.type == 'telemetry':
        result = loader_data_telemetry(args)
        tabel = TABLE_TELEMETRY_CH
    elif args.type == 'preds_m1_test_intervals':
        result = loader_preds_m1_test_intervals(args)
        tabel = TABLE_PREDICT_M1_CH
    elif args.type == 'preds_m1_to_failure':
        result = loader_preds_m1_to_failure(args)
        tabel = TABLE_PREDICT_M1_TO_FAILURE_CH
    if result is not None:
        connector = DatabaseClickhouseConnector(
                host=URL_CONNECTION_CH, port=PORT_CONNECTION_CH,
                user=USER_CH, password=PASSWORD_CH
            )
        connector.connect()
        print("upload data")
        connector.save_dataframe(data_frame=result, bd_name=DB_CH, bd_table=tabel)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='UploaderData',
        description='Загрузка измерений с датчиков (X_train, X_test, y_train) и состояний оборудования в CH',
    )
    parser.add_argument('-f', '--filename', default='data/X_train.parquet', help='Путь до файла с данными')
    parser.add_argument('-t', '--type', default='telemetry', help='Тип файла: telemetry')
    parser.add_argument('-m', '--machine', default=9, help='Номер машины (указывать при загрузке telemetry)')
    args = parser.parse_args()
    main_uploader(args)
