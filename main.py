import praw
from dotenv import load_dotenv; load_dotenv()
import os
import time
from scraping import get_images
from processing import detect_image_repost

def main():
    reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'),
                    client_secret=os.getenv('CLIENT_SECRET'),
                    user_agent=os.getenv('USER_AGENT'),
                    username=os.getenv('USERNAME'),
                    password=os.getenv('PASSWORD'))
    sub = reddit.subreddit('memes')
    start_time = time.time()
    for submission in sub.stream.submissions():
        if submission.created_utc < start_time:
            continue
        print(submission.url)
        images = get_images(subreddit='memes', lim=10)
        url = submission.url
        if url.startswith('https://i.redd.it') or url.startswith('https://i.imgur.com'):
            print(detect_image_repost(images, url))

if __name__ == "__main__":
    main()