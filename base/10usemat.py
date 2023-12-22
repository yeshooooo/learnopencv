import cv2
import numpy as np

img = cv2.imread("./static/RMB.jpeg")

# 如果修改a， b的内容也跟着变化了，说明是浅拷贝
img2 = img

# 深拷贝
img3 = img.copy()
img[10:100, 10:100] = [0, 0, 255]

cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)


cv2.waitKey(0)