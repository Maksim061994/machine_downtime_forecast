from clickhouse_driver import Client
import pandas as pd


class DatabaseClickhouseConnector:

    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.client = None

    def connect(self):
        """
        TODO: дописать обработку ошибок
        """
        self.client = Client(
            host=self.host, port=self.port,
            user=self.user, password=self.password
        )
        self.client.execute("show databases")

    def save_dataframe(self, data_frame: pd.DataFrame, bd_name: str, bd_table: str):
        """
        TODO: дописать обработку ошибок
        """
        self.client.execute(f'INSERT INTO {bd_name}.{bd_table} VALUES', data_frame.to_dict('records'))

    def save_values(self, data: list, bd_name: str, bd_table: str):
        """
        TODO: дописать обработку ошибок
        """
        self.client.execute(f'INSERT INTO {bd_name}.{bd_table} VALUES', data, types_check=True)
