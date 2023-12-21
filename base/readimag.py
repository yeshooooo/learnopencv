import cv2

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
# img = cv2.imread("E:\\codes\\opencv\\lichao\\learnopencv\\base\\static\\perspective.jpeg")
# 这里相对路径很奇怪
img = cv2.imread("base/static/perspective.jpeg")

# 将图片和窗口绑定到一起
cv2.imshow("img", img)
key = cv2.waitKey(0)

if(key == 'q'):
    exit()
cv2.destroyAllWindows()
