from scraping import get_images
from typing import List
import requests
from cv2 import cv2
import numpy as np
from skimage import io

def detect_image_repost(urls: List[str], url: str) -> int:
    ''' 
    Returns image that most closely resembles a repost
    returns image in the form of a list that gives the url to the image,
    the confidence that the image is a repost
    '''
    image1 = io.imread(url)
    sift = cv2.SIFT_create()
    k1, d1 = sift.detectAndCompute(image1, None)

    index = {'algorithm': 0, 'trees': 5}
    search = {}
    flann = cv2.FlannBasedMatcher(index, search)

    max_confidence = -1
    final_url = urls[0]

    for u in urls:
        image2 = io.imread(u)
        k2, d2 = sift.detectAndCompute(image2, None)
        matches = flann.knnMatch(d1, d2, k=2)
        points = []
        for m, n in matches:
            if m.distance < .6 * n.distance:
                points.append(m)
        number_keypoints = 0
        if len(k1) < len(k2):
            number_keypoints = len(k1)
        else:
            number_keypoints = len(k2)
        confidence = (len(points) / number_keypoints) * 100
        if confidence > max_confidence:
            max_confidence = confidence
            final_url = u

    print(url, final_url, max_confidence)
    return [final_url, max_confidence]