import os
from mlflow.server import get_app_client
from dotenv import find_dotenv, load_dotenv

# find env config
load_dotenv(find_dotenv())

MLFLOW_TRACKING_USERNAME=os.environ.get('MLFLOW_TRACKING_USERNAME', None)
MLFLOW_TRACKING_PASSWORD=os.environ.get('MLFLOW_TRACKING_PASSWORD', None)
MLFLOW_UPDATED_USERNAME=os.environ.get('MLFLOW_UPDATED_USERNAME', None)
MLFLOW_UPDATED_PASSWORD=os.environ.get('MLFLOW_UPDATED_PASSWORD', None)
MLFLOW_TRACKING_URI=os.environ.get('MLFLOW_TRACKING_URI', "http://0.0.0.0:5000")

# update the admin credentials
auth_client = get_app_client("basic-auth", tracking_uri=MLFLOW_TRACKING_URI)

try:
    print(f"Adding new admin user/pass: {MLFLOW_UPDATED_USERNAME}, {MLFLOW_UPDATED_PASSWORD}")
    auth_client.create_user(username=MLFLOW_UPDATED_USERNAME, password=MLFLOW_UPDATED_PASSWORD)
    auth_client.update_user_admin(username=MLFLOW_UPDATED_USERNAME, is_admin=True)
except Exception:
    print("New user name", MLFLOW_UPDATED_USERNAME)
    print("Did not complete auth change, the user may already exist...")

try:
    print("Deleting default user/pass")
    auth_client.delete_user(username=MLFLOW_TRACKING_USERNAME)
except Exception:
    print("Could not delete default admin user...")
