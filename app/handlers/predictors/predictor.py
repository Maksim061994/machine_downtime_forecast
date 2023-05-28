import os
import mlflow
import pandas as pd


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
            4: "runs:/dc5de2c91e394e3a99d2aeebb6bd4a25/model",
            5: "runs:/8f659233792648569e7692dd6c0d5417/model"
        }

    def compute(self, data, columns, machine_number):
        logged_model = self.d_machine.get(machine_number)
        if logged_model:
            loaded_model = mlflow.pyfunc.load_model(logged_model)
            df = pd.DataFrame(data, columns=columns).astype(float)
            res = loaded_model.predict(df)
            return res


