from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_PORT = os.environ.get('DB_PORT')

DB_HOST_TEST = os.environ.get('DB_HOST_TEST')
DB_NAME_TEST = os.environ.get('DB_NAME_TEST')
DB_USER_TEST = os.environ.get('DB_USER_TEST')
DB_PASSWORD_TEST = os.environ.get('DB_PASSWORD_TEST')
DB_PORT_TEST = os.environ.get('DB_PORT_TEST')

SECRET_KEY_COOKIE = os.environ.get('SECRET_KEY_COOKIE')
SECRET_KEY_MANAGER = os.environ.get('SECRET_KEY_MANAGER')

SMTP_USER = os.environ.get('SMTP_USER')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
