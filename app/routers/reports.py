from fastapi import APIRouter

# handlers
from app.config.settings import get_settings


report_api_routers = APIRouter()
settings = get_settings()


@report_api_routers.get('/m1')
async def report_m1(request):
    return "В разработке"


@report_api_routers.get('/m3')
async def report_m1(request):
    return "В разработке"


@report_api_routers.get('/test')
async def report_m1(request):
    return "В разработке"