from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_PORT = os.environ.get('DB_PORT')


SECRET_KEY_COOKIE = os.environ.get('SECRET_KEY')
SECRET_KEY_MANAGER = os.environ.get('SECRET_KEY')
