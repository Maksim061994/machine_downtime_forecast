from app.helpers.utils.custom_datetime import strptime


class QueryBuilder:

    def __init__(self, setting):
        self.setting = setting
        self.base_path = "app/handlers/predictors/sql"

    def make_query_for_upload_features(self,
            db: str, table: str, start_date: str, end_date: str,
            skip: int = 0, limit: int = 10, machine_number: int = 0
    ):
        start_dt = strptime(start_date, self.setting.date_format, self.setting.date_format_default)
        end_dt = strptime(end_date, self.setting.date_format, self.setting.date_format_default)
        with open(f"{self.base_path}/make_query_base.sql", "r") as f:
            base_query = f.read()
        with open(f"{self.base_path}/make_query_cnt.sql", "r") as f:
            cnt_query = f.read()
        base_query = base_query.format(db=db, table=table)
        cnt_query = cnt_query.format(db=db, table=table)
        filter_where = f" where ctime >= '{start_dt}' and ctime < '{end_dt}' and "
        if machine_number:
            filter_where += f"machine_number = {machine_number} and "
        base_query = base_query + filter_where[:-4] + f"order by ctime, date_op, ser_loc, zns_loc, prs_loc limit {skip}, {limit}"
        cnt_query = cnt_query + filter_where[:-4]
        return base_query, cnt_query

