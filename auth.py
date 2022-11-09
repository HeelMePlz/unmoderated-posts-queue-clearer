import os

import dotenv
import praw

dotenv.load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
USER_AGENT = os.environ.get("USER_AGENT")
SUBREDDIT_NAME = os.environ.get("SUBREDDIT_NAME")


def request():
    return praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=USERNAME,
        password=PASSWORD,
        user_agent=USER_AGENT,
    )


def get_subreddit_name():
    return SUBREDDIT_NAME
