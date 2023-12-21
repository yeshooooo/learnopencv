import cv2

# 创建窗口
cv2.namedWindow("video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("video", 640, 480)
# 获取视频设备

# 通过设备id读取
# cap = cv2.VideoCapture(0)
# 从视频文件中读取视频帧
cap = cv2.VideoCapture("./static/videos/stone.mp4")

while True:
    # 从摄像头读视频帧
    ret, frame = cap.read()
    # 将视频帧在窗口中显示
    # frame 也是Mat类型
    cv2.imshow("video", frame)
    # 等待键盘事件，如果为q，退出
    # 这里不能为0了，否则他会一直等待键盘事件，卡在当前帧
    # 实时视频用1没问题，视频文件可以用ffplay看下参数，一般是25帧左右，所以这里设置为40ms,否则播放的会很快
    # 严格来说需要 1000/视频帧率
    key = cv2.waitKey(40)
    if key & 0xFF == ord("q"):
        break

# 释放VideoCapture
cap.release()
# 释放窗口资源
cv2.destroyAllWindows()

