import random

from bot.settings import POSITIVE_AFFIRMATIONS


def process_request() -> str:
    return random.choice(POSITIVE_AFFIRMATIONS)
