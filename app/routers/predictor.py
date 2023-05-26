from fastapi import APIRouter

# handlers
from app.config.settings import get_settings


predict_api_routers = APIRouter()
settings = get_settings()


@predict_api_routers.post('/predict')
async def predict(request: PredictParamsSchema):
    predictor = Predictor(settings)
    return await predictor.compute(request)


@predict_api_routers.get('/features')
async def features(request: PredictParamsSchema):
    predictor = Predictor(settings)
    return await predictor.compute(request)
