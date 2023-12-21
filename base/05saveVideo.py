import cv2

# 创建窗口
cv2.namedWindow("video", cv2.WINDOW_NORMAL)

# 获取视频设备

# 通过设备id读取
cap = cv2.VideoCapture(0)

# 创建VideoWriter
video_width = int(cap.get(3))
video_height = int(cap.get(4))
video_fps = int(cap.get(5))
fourcc = cv2.VideoWriter.fourcc(*'mp4v')
# 分辨率要写成摄像头的真实分辨率设置，否则不能写入，硬写也有方法，后面介绍
vw = cv2.VideoWriter("./out.mp4", fourcc, video_fps, (video_width, video_height))

# 判断摄像头是否为打开状态
while cap.isOpened():
    # 从摄像头读视频帧
    ret, frame = cap.read()

    if ret:
        # 将视频帧在窗口中显示
        # frame 也是Mat类型
        cv2.imshow("video", frame)

        # 防止窗口改变大小,再设置一遍大小
        cv2.resizeWindow("video", video_width, video_height)
        # 写数据到多媒体文件
        vw.write(frame)
        # 等待键盘事件，如果为q，退出
        # 这里不能为0了，否则他会一直等待键盘事件，卡在当前帧
        # 实时视频用1没问题，视频文件可以用ffplay看下参数，一般是25帧左右，所以这里设置为40ms,否则播放的会很快
        # 严格来说需要 1000/视频帧率
        key = cv2.waitKey(40)
        if key & 0xFF == ord("q"):
            break
    else:
        # 读不到数据直接退出
        break

# 释放VideoCapture
cap.release()

# 释放VideoWriter资源
vw.release()
# 释放窗口资源
cv2.destroyAllWindows()

