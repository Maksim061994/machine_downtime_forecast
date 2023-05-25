import logging

# fastapi
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.logger import logger as fastapi_logger

# custom libs
from app.routers.user_access import user_access_router
# from app.helpers.utils.verify_token import verify_token


# setup logger
gunicorn_error_logger = logging.getLogger("gunicorn.error")
gunicorn_logger = logging.getLogger("gunicorn")
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = gunicorn_error_logger.handlers
fastapi_logger.handlers = gunicorn_error_logger.handlers


app = FastAPI(
    title="API для работы с предиктивными моделями по оборудованию",
    description="Сделано в рамках хакатона",
    version="0.0.1",
    contact={
        "name": "Maksim Kulagin",
        "email": "kulagin.maxim@vniizht.ru",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['POST', 'GET'],
    allow_headers=['*'],
    allow_credentials=True,
)

# users
app.include_router(
    user_access_router, prefix='/users',
    tags=['user_access_router']
)

# models
# app.include_router(
#     assistant_router, prefix='/models',
#     tags=['assistant_model'],
#     dependencies=[Depends(verify_token)],
# )



