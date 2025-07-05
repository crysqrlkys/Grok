import enum
import logging

from github import Github
from github_bot_api import Event, Webhook, GithubApp
from pathlib import Path

from bot.core.complex_ai_logic import process_request
from bot.settings import BOT_ALIASES, PREFIX, Settings

logger = logging.getLogger(__name__)


webhook = Webhook(secret=Settings.WEBHOOK_SECRET)
app = GithubApp(
    user_agent="drone/0.0.1",
    app_id=Settings.GITHUB_APP_ID,
    private_key=Path(Settings.PRIVATE_KEY_PATH).read_text()
)

class UserTypes(str, enum.Enum):
    BOT = "Bot"
    USER = "User"


class CommentType(str, enum.Enum):
    ISSUE = "issue_comment"
    PULL_REQUEST = "pull_request_comment"


def comment_validation(comment: dict) -> bool:
    if user_type := comment.get("user", {}).get("type", UserTypes.BOT) != UserTypes.BOT:
        if comment.get("body").lower().startswith(tuple(PREFIX + _ for _ in BOT_ALIASES)):
            return True
    else:
        logger.info(f"Skipped {user_type}")
    return False


def send_comment(event: Event):
    client: Github = app.installation_client(event.payload["installation"]["id"])
    repo = client.get_repo(event.payload["repository"]["full_name"])
    match event.name:
        case CommentType.ISSUE:
            target = repo.get_issue(event.payload["issue"]["number"])
        case CommentType.PULL_REQUEST:
            target = repo.get_pull(event.payload["pull_request"]["number"])
    answer = process_request()
    target.create_comment(answer)


@webhook.listen("pull_request_comment")
@webhook.listen("issue_comment")
def on_issue_comment(event: Event) -> bool:
    try:
        comment = event.payload.get("comment")
        if comment_validation(comment=comment):
            send_comment(event)
            return True
        return False
    except Exception as e:
        logger.error(e)
