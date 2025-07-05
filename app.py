from github_bot_api.flask import create_flask_app
from bot.processor import webhook


flask = create_flask_app(__name__, webhook)
