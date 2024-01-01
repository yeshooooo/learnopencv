#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>
using namespace cv;
int main()
{
	Mat srcImage = imread("1.jpg");
	imshow("��ԭʼͼ��Canny��Ե���", srcImage);

	// �������
	Mat dstImage, edge, grayImage;

	// ������src ͬ���ͺʹ�С�ľ���(dst)
	dstImage.create(srcImage.size(), srcImage.type());

	// ��ԭʼͼ��ת��Ϊ�Ҷ�ͼ��
	cvtColor(srcImage, grayImage, COLOR_BGR2GRAY);

	// ʹ��3x3�ں˽���
	blur(grayImage, edge, Size(3, 3));

	// ����Canny ����
	Canny(edge, edge, 3, 9, 3);

	// ��ʾЧ��ͼ
	imshow("��Ч��ͼ��Canny��Ե���", edge);
	waitKey(0);

	return 0;
}