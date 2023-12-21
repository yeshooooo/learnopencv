import cv2

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
# vscode和pycharm的相对路径写法不一样
img = cv2.imread("base/static/perspective.jpeg")

# 加while的目的是防止按其他键逻辑也往下走，也会退出
while True:
    cv2.imshow("img", img)

    key = cv2.waitKey(0)

    if(key & 0xFF == ord('q')):
        break
        
    elif(key & 0xFF == ord('s')):
        # 保存图片
        # 这样其实是保存到了跟base平级的顶层文件夹下
        cv2.imwrite("1123.png", img)
cv2.destroyAllWindows()