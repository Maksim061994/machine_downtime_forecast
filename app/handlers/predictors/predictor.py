import os
import mlflow
import pandas as pd
import asyncio
import warnings
warnings.filterwarnings('ignore')


os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://tis5000.vniizht.lan:9000"
os.environ['AWS_ACCESS_KEY_ID'] = 'hakaton'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'JD643JcviPvhnRtbf'
mlflow.set_tracking_uri("http://tis5000.vniizht.lan:5000")
mlflow.set_experiment("exg-machine-downtime-forecast")


class Predictor:
    # TODO: рефакторинг

    def __init__(self, settings):
        self.setting = settings
        self.d_machine = {
            4: "runs:/1173d0bf82d94c399089acde753db61b/model",
            5: "runs:/667ba75ca85b4016bffd57e340939e4a/model",
            6: "runs:/03731a859af44ec7a88fc869716794d9/model",
            7: "runs:/71ce6e6640994ad4969dd4bcd6ce6bf9/model",
            8: "runs:/ef6c50e2c9d04b5082076b90d7953682/model",
            9: "runs:/14e3514d4ef34e2591de0137babaddb7/model"
        }

    def __get_predict(self, data, logged_model, columns):
        loaded_model = mlflow.pyfunc.load_model(logged_model)
        df = pd.DataFrame(data, columns=columns).astype(float)
        res = loaded_model.predict(df)
        res = res.tolist()
        out_d = {"predicts": res}
        return out_d

    async def compute(self, data, columns, machine_number):
        logged_model = self.d_machine.get(machine_number)
        out_d = None
        if logged_model:
            loop = asyncio.get_event_loop()
            out_d = await loop.run_in_executor(None, self.__get_predict, data, logged_model, columns)
        return out_d


