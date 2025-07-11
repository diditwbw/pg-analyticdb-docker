FROM apache/superset

USER root

RUN pip install --upgrade pip setuptools wheel \
    && pip install psycopg2-binary sqlalchemy

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY superset_config.py /app/pythonpath/superset_config.py

USER superset

ENTRYPOINT ["/entrypoint.sh"]
