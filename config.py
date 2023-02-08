import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) 

#Database configurations
DB_HOST = os.getenv('DB_HOST', None)
DB_USER = os.getenv('DB_USER', None)
DB_PASSWORD = os.getenv('DB_PASSWORD', None)
DB_NAME = os.getenv('DB_NAME', 'dados')