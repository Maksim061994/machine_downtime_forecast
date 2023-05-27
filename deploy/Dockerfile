FROM apache/superset:1583090623c5083de504ad1e1710b894f0dc7f67
USER root
RUN pip install --upgrade pip && \
    pip install clickhouse-connect clickhouse-driver clickhouse-sqlalchemy && \
    pip install -r superset/translations/requirements.txt
USER superset