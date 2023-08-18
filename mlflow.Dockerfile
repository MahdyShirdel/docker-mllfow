# Use the official Python 3.10 image as the base image
FROM python:3.10.5

# Update pip to the latest version
RUN python -m pip install --upgrade pip


# Copy the requirements file into the container
COPY ./requirements.txt .
COPY ./authenticate.py .
COPY ./.env .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Run mlflow server
CMD mlflow server --app-name basic-auth \ 
    --backend-store-uri postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:5432/${POSTGRES_DB} \
    --default-artifact-root ${ARTIFACT_ROOT} \
    --host 0.0.0.0 \
    --port 5000 