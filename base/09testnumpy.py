import numpy as np

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
print(g)
