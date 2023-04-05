import cv2 as cv
import numpy
import numpy as np


def get_part(image):
    grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(grayscale, 100, 110, apertureSize=3)
    contour, hieachy = cv.findContours(edge, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    part = []
    for i, c in enumerate(contour):
        area = cv.contourArea(c)
        if area < 100:
            continue
        im = cv.drawContours(numpy.zeros_like(grayscale), contour, i, 255, cv.FILLED)
        if np.random.random(1) < 0.5:
            part.append(im)
    return edge, part


def gen_image(part):
    dif_i = cv.imread(part)
    edge, part = get_part(dif_i)
    for p in part:
        dif_c = tuple(np.random.randint(0, 256, 3))
        dif_i[p == 255] = dif_c
    dif_i[edge == 255] = 0
    return dif_i


# i = cv.imread("adu.png")
# dif_i = generate_image("adu.png")
# cv.imshow("ori", i)
# cv.imshow("dif", dif_i)
# cv.waitKey(0)
# cv.destroyAllWindows()
