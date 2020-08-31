from scraping import get_images

def detect_image_repost(image: str) -> int:
    ''' returns chance that image is a repost given list of image URLs '''
    images = get_images('195')
    