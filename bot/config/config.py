
import os
from dotenv import load_dotenv

load_dotenv("./.env")



class Config:
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6420144202:AAHCbmnQh7JT6p7fksK_8chVgmLsYtv5wYE")
  BOT_NAME = os.environ.get("BOT_NAME", "boy")

  API_ID = int(os.environ.get("API_ID", "15851949"))
  API_HASH = os.environ.get("API_HASH", "f8e386978bf103c4a6baab0a4b92e822")

  DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb://cls5zmw31000kaume2jhqcdpd:y9q9BOZGYBTmvGdXZFyUcj8A@104.251.218.202:9001/?readPreference=primary&ssl=false")
  SESSION_NAME = os.environ.get("DATABASE_NAME", "Aleena")

  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1002049466903))
  SUDO_USERS = [int(user) for user in (os.environ.get("SUDO_USERS","1137799257")).split()]
  SUPPORT_CHAT_URL = os.environ.get("SUPPORT_CHAT_URL", "https://t.me/subotsupport")
