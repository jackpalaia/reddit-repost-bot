import os
import praw
from typing import List
from dotenv import load_dotenv; load_dotenv()

def get_images(subreddit: str) -> List[str]:
    ''' returns list of image URLs for specified subreddit '''
    reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv(
        'CLIENT_SECRET'), user_agent=os.getenv('USER_AGENT'))
    sub = reddit.subreddit(subreddit)
    
    final = []
    for s in sub.new(limit=100):
        url = s.url
        if url.startswith('https://i.redd.it') or url.startswith('https://i.imgur.com'):
            final.append(url)
    return final

get_images('195')