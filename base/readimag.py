import cv2

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
# img = cv2.imread("E:\\codes\\opencv\\lichao\\learnopencv\\base\\static\\perspective.jpeg")
# 这里相对路径很奇怪
img = cv2.imread("base/static/perspective.jpeg")
# img = cv2.imread("./static/perspective.jpeg")
# 将图片和窗口绑定到一起
cv2.imshow("img", img)
key = cv2.waitKey(0)
print(key)
print('q')
print(ord('q')) # ord()获取字符的ascii码
# if(key == 'q'):
# 因为ascii码是8位的，所以使用位运算只获取最后一个8位
if(key & 0xFF == ord('q')):
    print(11111) #这里实际上并没有执行,应改为ord("q")
    cv2.destroyAllWindows()

