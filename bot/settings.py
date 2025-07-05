from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)


class Settings:
    FLASK_ENV = getenv("FLASK_ENV", "DEV")
    GITHUB_APP_ID = getenv("GITHUB_APP_ID")
    PRIVATE_KEY_PATH = getenv("PRIVATE_KEY_PATH")
    WEBHOOK_SECRET = getenv("WEBHOOK_SECRET", None)


PREFIX = "@"

BOT_ALIASES = ("grok", "gok", "grurk", "gork", "gonk")

POSITIVE_AFFIRMATIONS = (
    "No way",
    "Nope",
    "no",
    "ts fake",
    "fake",
    "obv it's fake",
    "its not real 🤦",
    "... no",
)
