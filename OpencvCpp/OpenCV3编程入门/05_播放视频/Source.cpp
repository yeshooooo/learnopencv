#include <opencv2/opencv.hpp>
using namespace cv;
int main()
{
	VideoCapture capture("1.avi");

	// 循环显示每一帧
	while (true)
	{
		Mat frame;
		capture >> frame;
		imshow("读取视频", frame);
		waitKey(30); // 延时30ms
	}

	return 0;

}