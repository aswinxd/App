
import os
from dotenv import load_dotenv

load_dotenv("./.env")


class Config:xvfZYfD7swIxvU")
  BOT_NAME = os.environ.get("BOT_NAME", "Aleena")

  API_ID = int(os.environ.get("API_ID", "15851949"))
  API_HASH = os.environ.get("API_HASH", "f8e386978bf103c4a6baab0a4b92e822")

  DATABASE_URI = os.environ.get("DATABASE_URI", "mongodbBTmvGdXZFyUcj8A@104.2eadPreference=primary&ssl=false")
  SESSION_NAME = os.environ.get("DATABASE_NAME", "Aleena")

  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1002049466903))
  SUDO_USERS = [int(user) for user in (os.environ.get("SUDO_USERS","1137799257")).split()]
  SUPPORT_CHAT_URL = os.environ.get("SUPPORT_CHAT_URL", "https://t.me/subotsupport")
