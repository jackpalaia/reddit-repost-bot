import os
import praw
from typing import List
from dotenv import load_dotenv; load_dotenv()

reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv(
        'CLIENT_SECRET'), user_agent=os.getenv('USER_AGENT'))

def get_images(subreddit: str, lim: int) -> List[str]:
    ''' returns list of image URLs for specified subreddit '''
    sub = reddit.subreddit(subreddit)
    final = []
    for s in sub.new(limit=lim):
        url = s.url
        # images from reddit or imgur are currently supported
        if url.startswith('https://i.redd.it') or url.startswith('https://i.imgur.com'):
            final.append(url)
    return final

def get_recent_image(subreddit: str) -> str:
    ''' returns url of most recently posted image to subreddit '''
    sub = reddit.subreddit(subreddit)
    for s in sub.new():
        url = s.url
        if url.startswith('https://i.redd.it') or url.startswith('https://i.imgur.com'):
            return url

get_recent_image('195')