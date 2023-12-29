#include <opencv2/opencv.hpp>
using namespace cv;

int main()
{
	Mat srcImage = imread("1.jpg");
	imshow("¡¾Ô­Ê¼Í¼¡¿", srcImage);
	waitKey(0);
}