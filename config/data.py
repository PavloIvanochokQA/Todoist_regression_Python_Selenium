from dotenv import load_dotenv
import os

load_dotenv()


class Data:

    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    USERNAME = os.getenv("USERNAME")
    GMAIL = os.getenv("GMAIL")
    GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
    GMAIL_USERNAME = os.getenv("GMAIL_USERNAME")
