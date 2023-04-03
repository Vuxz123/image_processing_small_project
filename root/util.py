import string

import cv2 as cv
import numpy as np
import modified_image as mi

i = cv.imread("adu.png")
i = cv.resize(i, (600, 800))
cv.imshow("ori", i)
dif_i = mi.gen_image("adu.png")
dif_i = cv.resize(dif_i, (600, 800))
cv.imshow("dif", dif_i)
dif_space = cv.absdiff(i, dif_i)
dif_space = cv.resize(dif_space, (600, 800))
dif_space = cv.cvtColor(dif_space, cv.COLOR_BGR2GRAY)
_, dif_space = cv.threshold(dif_space, 20, 255, cv.THRESH_BINARY)
cv.imshow("test", dif_space)

contours, hierachy = cv.findContours(dif_space, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

i = cv.rectangle(i, (600, 0), (600, 800), 200, 2)
combined_image = np.zeros((800, 1200, 3), dtype=np.uint8)

pos = (0, 0)


def mouse_callback(event, x, y, flags, params):
    global pos
    if event == cv.EVENT_LBUTTONDOWN:
        pos = (x, y)
        print("adudu")


array_c = []
contours_size = 0
for c in contours:
    contours_size += 1
    if cv.contourArea(c) < 100:
        continue
    array_c.append(c)
print(contours_size)
click_list = []
cv.namedWindow("cba")
cv.setMouseCallback("cba", mouse_callback)
temp = 100
while len(click_list) < temp:
    length = 0
    for idex, c in enumerate(array_c):
        length += 1
        x, y, w, h = cv.boundingRect(c)
        if idex not in click_list and x <= pos[0] <= x + w and y <= pos[1] <= y + h:
            cv.drawContours(i, array_c, idex, 150, 3)
            cv.drawContours(dif_i, array_c, idex, 150, 3)
            click_list.append(idex)

    temp = length
    combined_image[0:800, 0:600] = i
    combined_image[0:800, 600:1200] = dif_i
    text = str(temp) + " " + str(len(click_list))
    cv.putText(combined_image, text, (20, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
    cv.imshow("cba", combined_image)
    key = cv.waitKey(1) & 0xFF

    if key != -1:
        if key & 0xFF == ord("q"):
            break

cv.destroyAllWindows()
