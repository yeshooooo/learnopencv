#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;

int main()
{
	// 
	Mat girl = imread("dota.jpg"); //����ͼ��Mat
	namedWindow("��1������ͼ"); //����һ����Ϊ "��1������ͼ"�Ĵ���  
	imshow("��1������ͼ", girl);//��ʾ��Ϊ "��1������ͼ"�Ĵ���  

	//-----------------------------------����������ͼ���ϡ�--------------------------------------
	//	��������������ͼ����
	//--------------------------------------------------------------------------------------------------
	//����ͼƬ
	Mat image = imread("dota.jpg", 199);
	Mat logo = imread("dota_logo.jpg");

	//���������ʾ
	namedWindow("��2��ԭ��ͼ");
	imshow("��2��ԭ��ͼ", image);

	namedWindow("��3��logoͼ");
	imshow("��3��logoͼ", logo);

	// ����һ��Mat���ͣ����ڴ�ţ�ͼ���ROI
	Mat imageROI;
	//����һ
	imageROI = image(Rect(800, 350, logo.cols, logo.rows));
	//������
	//imageROI= image(Range(350,350+logo.rows),Range(800,800+logo.cols));

	// ��logo�ӵ�ԭͼ��
	addWeighted(imageROI, 0.5, logo, 0.3, 0., imageROI);

	//��ʾ���
	namedWindow("��4��ԭ��+logoͼ");
	imshow("��4��ԭ��+logoͼ", image);

	//-----------------------------------������ͼ��������--------------------------------------
	//	��������һ��Matͼ�������ͼ���ļ�
	//-----------------------------------------------------------------------------------------------
	//���һ��jpgͼƬ������Ŀ¼��
	imwrite("��imwrite���ɵ�ͼƬ.jpg", image);

	waitKey();

	return 0;
}