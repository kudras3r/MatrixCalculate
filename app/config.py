"""

    Created, supported, updated by kudraser
    
    Contacts
    tg: https://t.me/kudras3r_dev
    GitHub: https://github.com/kudras3r
    vk: https://vk.com/dgcihf

"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"
    SECRET_KEY = os.getenv("SECRET_KEY")


CALC_PATH = os.getenv("CALC_PATH")
