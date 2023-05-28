import os
import time

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6378")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6378")

# Определение задачи
@celery.task
def print_message():
    # TODO дописать
    print("Привет, это задача Celery!")
    print(f"Время выполнения: {time.strftime('%H:%M:%S')}")

# Конфигурация расписания
celery.conf.beat_schedule = {
    'run-every-30-seconds': {
        'task': 'predict_calcer.print_message',
        'schedule': 5.0,
    },
}

# # Запуск Celery worker и beat
if __name__ == '__main__':
    celery.worker_main(['--beat', '--loglevel=info'])