from app.helpers.db.clickhouse_connector import ClickhouseConnector
from app.handlers.predictors.query_builder import QueryBuilder


class LoaderFeatures:

    def __init__(self, settings):
        self.settings = settings
        self.query_builder = QueryBuilder()
        self.db_ch_database_models = settings.db_ch_database_models
        self.db_ch_table_models = settings.db_ch_table_models

    async def get(self, *args, **kwargs):
        skip = kwargs["page_size"] * kwargs["page_index"]
        query_base, query_cnt = self.query_builder.make_query_for_upload_features(
            db=self.db_ch_database_models, table=self.db_ch_table_models,
            skip=skip, limit=kwargs["page_size"]
        )
        result = {
            "data": [], "page_info": {"all_docs": 0, "output_docs": 0}
        }
        async with ClickhouseConnector() as client:
            out_ch = await client.fetch(query_base)
            if len(out_ch) > 0:
                cols = list(out_ch[0].keys())
                cnt_data = await client.fetch(query_cnt)
                result["data"] = [dict(zip(cols, el.values())) for el in out_ch]
                result["page_info"]["all_docs"] = list(cnt_data[0].values())[0]
                result["page_info"]["output_docs"] = len(result["data"])
            return result
