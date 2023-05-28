from fastapi import APIRouter

# handlers
from app.config.settings import get_settings
from app.handlers.predictors.loader import LoaderFeatures
from app.handlers.predictors.predictor import Predictor
from app.handlers.predictors.schemas import PredictSchemas


predict_api_routers = APIRouter()
settings = get_settings()


@predict_api_routers.post('/predict')
async def predict(request: PredictSchemas):
    predictor = Predictor(settings)
    return await predictor.compute(
        data=request.data, columns=request.columns, machine_number=request.machine_number
    )


@predict_api_routers.get('/features')
async def features(
        start: str, end: str, machine_number: int, version_model: int = 0,
        page_index: int = 0, page_size: int = 10
):
    loader = LoaderFeatures(settings)
    return await loader.get(
        start=start, end=end, version_model=version_model, machine_number=machine_number,
        page_index=page_index, page_size=page_size
    )
