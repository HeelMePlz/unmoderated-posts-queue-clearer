# unmoderated-posts-queue-clearer

## About

This is a script used for reddit to allow moderators of a subreddit to easily clear their unmoderated posts queue in an easy manner.

## Known Issues

- The script will crash after it has checked 100 posts. It can then be run again to clear another 100.

## Requirements

- Python

## Setup

1. Follow Reddit's [First Steps Guide](https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) to obtain a Client ID & Client Secret.

2. Create a .env file in the root directory and paste the following inside it:

    ```env
    CLIENT_ID=your-client-id
    CLIENT_SECRET=your-client-secret
    USERNAME=your-reddit-username
    PASSWORD=your-reddit-password
    USER_AGENT=subcounts by u/your-reddit-username
    SUBREDDIT_NAME=your-subreddit
    ```

3. Replace each field in the .env with your credentials.

4. Create and activate a virtual environment:

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

5. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

6. Run the script:

    ```sh
    python3 main.py
    ```
