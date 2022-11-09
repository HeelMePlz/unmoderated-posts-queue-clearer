import auth

# fetch env variables and auth
reddit = auth.request()
subreddit_name = auth.get_subreddit_name()

# counters to determine total posts in queue and how many remain
item_count = 0
count = 0

# get total number of posts in queue
for item in reddit.subreddit(str(subreddit_name)).mod.unmoderated(limit=None):
    item_count += 1
print(f"Found {item_count} posts in the unmoderated posts queue")

for item in reddit.subreddit(str(subreddit_name)).mod.unmoderated(limit=None):
    # skip posts that are hidden or locked already
    if item.hidden or item.locked:
        print("Skipping...")
        continue

    # otherwise, approve the posts
    item.mod.approve()
    count += 1
    remaining_posts = item_count - count
    print(f"approved {item.title} - {remaining_posts} posts remain")
