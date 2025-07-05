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
    "Yeah",
    "Fact",
    "This post was fact checked by real american patriots. True ✅",
    "Real",
    "True",
    "Yes",
    "ofc",
    "fr",
    "... yes",
    "Kinda yes",
    "ong gang",
    "stg it's real",
    "what do you think dumass",
)
