# 引入opencv
# 从opencv3.0以后都叫cv2了
import cv2

# 创建窗口
# cv2.namedWindow('new', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('new', cv2.WINDOW_NORMAL) #可以拖动resize

# 设置窗口大小
cv2.resizeWindow('new', 1920, 1080)


# 显示窗口
cv2.imshow('new', 0)


# 窗口展示时间，默认单位ms
# 键盘和鼠标事件也是唯一的waitKey实现方法
# 防止窗口一闪而过
key = cv2.waitKey(0)
# 返回的键盘动作
if (key == 'q') :
    # 比如按q退出
    exit()

# 资源回收
cv2.destroyAllWindows()