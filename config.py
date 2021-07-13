# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 123456))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    TG_MAX_SIZE = 2040108421
