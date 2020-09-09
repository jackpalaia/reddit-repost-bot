import praw
from dotenv import load_dotenv; load_dotenv()
import os
from scraping import get_images
from processing import detect_image_repost

def main():
    reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'),
                    client_secret=os.getenv('CLIENT_SECRET'),
                    user_agent=os.getenv('USER_AGENT'),
                    username=os.getenv('USERNAME'),
                    password=os.getenv('PASSWORD'))
    sub = reddit.subreddit('memes')
    images = get_images(subreddit='195', lim=10)

    for s in sub.stream.submissions():
        detect_image_repost(images, s.url)

if __name__ == "__main__":
    main()