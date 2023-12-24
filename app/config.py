import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"
    SECRET_KEY = os.getenv("SECRET_KEY")


CALC_PATH = os.getenv("CALC_PATH")
