from timeit import timeit

import cv2
import numpy as np
from matplotlib import pyplot as plt

DEBUG = False

BGR = 'bgr'
HSV = 'hsv'


def filter_color(image, color, input_format='bgr'):
    if input_format == 'bgr':
        hsv_color = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)[0][0]
    elif input_format == 'hsv':
        hsv_color = color
    else:
        raise ValueError("Input format not supported. Please select 'bgr' or 'hsv'.")
    h, s, v = hsv_color
    hue_tolerance = 20
    saturation_tolerance = 50
    value_tolerance = 50
    lower_color_range = np.array([h - hue_tolerance, s - saturation_tolerance, v - value_tolerance])
    upper_color_range = np.array([h + hue_tolerance, s + saturation_tolerance, v + value_tolerance])
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_color_range, upper_color_range)
    if DEBUG:
        cv2.imshow("mask", mask)
    return mask


def get_part(mask):
    contours, hierachy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    size = 0
    array = []
    for c in contours:
        if cv2.contourArea(c) < 20:
            continue
        array.append(c)
        size += 1

    if DEBUG:
        print("size:", size)
    if size == 0:
        return None, 0

    i = np.random.randint(size)
    if DEBUG:
        print("ranPart:", i)
    part = np.zeros_like(mask)
    cv2.drawContours(part, array, i, (255, 255, 255), cv2.FILLED)
    if DEBUG:
        cv2.imshow("part", part)
    return part, size


def check_hist(mask):
    hist = cv2.calcHist([mask], [0], None, [256], [0, 256])
    white = hist[255]
    black = hist[0]
    print((white / (black + white)))
    return (white / (black + white)) < 0.003


def random_change_color(image):
    height, width, channels = image.shape
    part = None
    while True:
        color = (255, 255, 255)
        max_iterations = height * width
        iterations = 0
        while (color == (255, 255, 255) or color == (0, 0, 0)) and iterations < max_iterations:
            x = np.random.randint(height)
            y = np.random.randint(width)
            color = tuple(map(int, image[x][y]))
            iterations += 1
        if DEBUG:
            print("color:", color)
        mask = filter_color(image, color)
        part, size = get_part(mask)
        if size != 0:
            break
    dif_image = image.copy()
    dif_c = tuple(np.random.randint(0, 256, 3))
    dif_image[part == 255] = dif_c
    return dif_image


def gen_image(part):
    i = cv2.imread(part)
    a = np.random.randint(5)
    d_i = None
    for x in range(a):
        d_i = random_change_color(i)
        i = d_i
    return d_i


# i = cv2.imread("adu.png")
# cv2.imshow("origin", i)
# d_i = gen_image("adu.png")
# cv2.imshow("abc", d_i)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
