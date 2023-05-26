from fastapi import APIRouter

# handlers
from app.config.settings import get_settings


report_api_routers = APIRouter()
settings = get_settings()


@report_api_routers.get('/m1')
async def report_m1(request: PredictParamsSchema):
    predictor = Predictor(settings)
    return await predictor.compute(request)


@report_api_routers.get('/m3')
async def report_m1(request: PredictParamsSchema):
    predictor = Predictor(settings)
    return await predictor.compute(request)


@report_api_routers.get('/test')
async def report_m1(request: PredictParamsSchema):
    predictor = Predictor(settings)
    return await predictor.compute(request)