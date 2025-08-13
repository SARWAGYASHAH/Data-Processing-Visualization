import os

BASE_DIR=os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER=os.path.join(BASE_DIR,'uploads')
PROCESSED_FOLDER=os.path.join(BASE_DIR,'processed')
LOG_FOLDER=os.path.join(BASE_DIR,'logs')

SECRET_KEY="dev-server-key-change-me"

os.makedirs(UPLOAD_FOLDER,exist_ok=True)
os.makedirs(PROCESSED_FOLDER,exist_ok=True)
os.makedirs(LOG_FOLDER,exist_ok=True)
