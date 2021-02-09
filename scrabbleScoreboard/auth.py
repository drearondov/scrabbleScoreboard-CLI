import os
import requests

from dotenv import load_dotenv


def login():
    load_dotenv()

    ACCESS_TOKEN = os.environ.get("ADMIN_ACCESS_TOKEN")
    REFRESH_TOKEN = os.environ.get("ADMIN_REFRESH_TOKEN")
    API_URL = os.environ.get("API_URL")

    response = requests.get('{API_URL}/auth/login')

