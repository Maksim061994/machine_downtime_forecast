#Запуск и работа с системой

1. Отредактировать файл `.env` под свои нужды
2. Отредактировать конфигурационные файлы в каталоге `configs`
3. Запустить команду `docker-compose up -d` дождаться запуска всех контейнеров
4. Создать в PosgtreSQL базу данных `superset`
5. Ввести отредактировав под свои нужды команду:
docker exec -it severstal_ui superset fab create-admin \
               --username admin \
               --firstname Superset \
               --lastname Admin \
               --email admin@admin.com \
               --password hf#d,mIDN5dhI*C539JF; \
docker exec -it severstal_ui superset db upgrade; \
docker exec -it severstal_ui superset init;
6. Ссылки для работы в системе:
 - ip_host:8089 - Superset (логин и пароль в пункте 4 текущего документа)
 - ip_host:5000 - MLFlow
 - ip_host:3020/docs - API
 - ip_host:9002 - Minio(s3) (логин и пароль в файле .env)
 - ip_host:5555/dashboard - Flower (отслеживание работы Celery)
7. Зайти в Minio и создать область хранения данных для MLFlow (Учетные данные в .env)