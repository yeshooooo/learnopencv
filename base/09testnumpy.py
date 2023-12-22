import numpy as np
import cv2
# 通过array 定义矩阵
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)
# print(b)

# 定义zeros 矩阵
# 前面是行/高度，3层是因为rgb有三个通道
c = np.zeros((8, 8, 3), np.uint8)
# print(c)

# 定义ones矩阵
d = np.ones((8, 8), np.uint8)
# print(d)

# 定义full矩阵
e = np.full((8, 8), 255, np.uint8)
# print(e)

# 定义单元矩阵
f = np.identity(8)
# print(f)

# eye矩阵
# key是从第几个开始(从0开始计数)
g = np.eye(5, 7, 3)
# print(g)

img = np.zeros((480, 640, 3), np.uint8)

# count = 0
# while count < 200:
#     img[count, 100, 0] = 255
#     count += 1

roi = img[100:400, 100:600]
roi[:,:] = [0, 0, 255]
roi[10:200, 10:200] = [0, 255, 0]

cv2.imshow('img', img)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()