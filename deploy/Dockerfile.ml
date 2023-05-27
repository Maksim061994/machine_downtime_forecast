FROM ubuntu/mlflow:2.1.1_1.0-22.04
USER root
RUN apt update && \
    apt install curl net-tools iputils-ping telnet -y && \
    pip install --upgrade pip && \
    pip install --no-cache mlflow[extras] psycopg2-binary sqlalchemy boto3
