#include <opencv2/opencv.hpp>
using namespace cv;
int main()
{
	VideoCapture capture("1.avi");

	// ѭ����ʾÿһ֡
	while (true)
	{
		Mat frame;
		capture >> frame;
		imshow("��ȡ��Ƶ", frame);
		waitKey(30); // ��ʱ30ms
	}

	return 0;

}