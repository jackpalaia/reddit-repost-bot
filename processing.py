from scraping import get_images
import requests
from cv2 import cv2
import numpy as np
from skimage import io

def detect_image_repost(image: str) -> int:
    ''' returns chance that image is a repost given list of image URLs '''
    images = get_images('195')
    url1 = images[0]
    url2 = images[1]
    image1 = io.imread(url1)
    image2 = io.imread(url2)
    #cv2.imshow('title', image)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    sift = cv2.SIFT_create()
    k1, d1 = sift.detectAndCompute(image1, None)
    k2, d2 = sift.detectAndCompute(image2, None)

    print(f'key points image 1: {str(len(k1))}')
    print(f'key points image 2: {str(len(k2))}')

    index = {'algorithm': 0, 'trees': 5}
    search = {}
    flann = cv2.FlannBasedMatcher(index, search)
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

    print(f'matches: {len(points)}')

    print(f'percentage: {(len(points) / number_keypoints) * 100}')

    result = cv2.drawMatchesKnn(image1, k1, image2, k2, matches, None)
    cv2.imshow('result', result)
    cv2.waitKey()
    cv2.destroyAllWindows()

detect_image_repost('t')