import os
import sys
import time

import auth

# fetch env variables and auth
reddit = auth.request()
subreddit_name = auth.get_subreddit_name()


def get_number_of_unmoderated_posts(unmoderated_queue):
    item_count = sum(1 for _ in unmoderated_queue)
    return item_count


def approve_unmoderated_posts(unmoderated_queue, item_count):
    count = 0
    for item in unmoderated_queue:
        # skip posts that are hidden or locked already
        if item.hidden or item.locked:
            print("Skipping...")
            continue

        # otherwise, approve the posts
        item.mod.approve()
        count += 1
        remaining_posts = item_count - count
        print(f"approved {item.title} - {remaining_posts} posts remain")

        # restart the script after approving 100 posts due to reddit api guideline limitations:
        # more info: https://praw.readthedocs.io/en/v3.6.2/pages/getting_started.html#obfuscation-and-api-limitations
        if count == 100 and remaining_posts > 0:
            time.sleep(2)
            print("Reached 100 approvals, restarting the script...")
            os.execv(sys.executable, ["python3"] + sys.argv)

        # if no posts remain, end
        if remaining_posts == 0:
            return


queue = reddit.subreddit(str(subreddit_name)).mod.unmoderated(limit=None)
item_count = get_number_of_unmoderated_posts(queue)
print(f"Found {item_count} posts in the unmoderated posts queue")

unmoderated_queue = reddit.subreddit(str(subreddit_name)).mod.unmoderated(limit=None)
approve_unmoderated_posts(unmoderated_queue, item_count)
