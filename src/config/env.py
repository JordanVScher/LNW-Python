import os
from dotenv import load_dotenv

load_dotenv()

ETHEREAL_LOGIN = os.getenv("ETHEREAL_LOGIN")
ETHEREAL_PASSWORD = os.getenv("ETHEREAL_PASSWORD")
