FROM python:3.6.7

COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD mlflow server \
    --backend-store-uri postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:45432/${POSTGRES_DB} \
    --default-artifact-root ${ARTIFACT_ROOT} \
    --host 0.0.0.0 \
    --port 5000

