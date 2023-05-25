import argparse
import clickhouse_driver


def main_uploader(args):
    # Установка соединения с ClickHouse
    connection = clickhouse_driver.connect(host='localhost', port=9000, database='your_database', user='your_user', password='your_password')
    cursor = connection.cursor()

    # Определение типа файла и выполнение соответствующих действий
    if args.type == 'measurements':
        load_measurements(cursor, args.filename, args.machine)
    elif args.type == 'state_equips':
        load_state_equips(cursor, args.filename, args.machine)
    else:
        print("Неподдерживаемый тип файла")

    # Закрытие соединения с ClickHouse
    cursor.close()
    connection.close()


def load_measurements(cursor, filename, machine):
    # Загрузка данных из файла measurements в ClickHouse
    query = f"INSERT INTO your_measurements_table FORMAT Parquet"
    with open(filename, 'rb') as file:
        cursor.execute(query, {'data': file, 'machine': machine})

    # Подтверждение выполнения операции
    print("Данные measurements загружены успешно")


def load_state_equips(cursor, filename, machine):
    # Загрузка данных из файла state_equips в ClickHouse
    query = f"INSERT INTO your_state_equips_table FORMAT Parquet"
    with open(filename, 'rb') as file:
        cursor.execute(query, {'data': file, 'machine': machine})

    # Подтверждение выполнения операции
    print("Данные state_equips загружены успешно")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='UploaderData',
        description='Загрузка измерений с датчиков (X_train, X_test, y_train) и состояний оборудования в CH',
    )
    parser.add_argument('-f', '--filename', default='data/X_train.parquet', help='Путь до файла с данными')
    parser.add_argument('-t', '--type', default='measurements', help='Тип файла: measurements/state_equips')
    parser.add_argument('-mach', '--machine', default=9, help='Номер машины (указывать при загрузке measurements/state_equips)')
    args = parser.parse_args()
    main_uploader(args)
