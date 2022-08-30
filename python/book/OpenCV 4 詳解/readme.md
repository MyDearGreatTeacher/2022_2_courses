# [OpenCV 4 詳解：基於 Python()馮振，陳亞萌 人民郵電](https://www.tenlong.com.tw/products/9787115566034?list_name=srh)
- [GITHUB](https://github.com/fengzhenHIT/learnOpenCV4_Python)


```
# -*- coding:utf-8 -*-
import cv2 as cv
from google.colab.patches import cv2_imshow

if __name__ == '__main__':
    video = cv.VideoCapture('./road.mp4')

    # 判断是否成功创建视频流
    while video.isOpened():
        ret, frame = video.read()
        if ret is True:
            #cv.imshow('Video', frame)
            cv2_imshow(frame)

            # 设置视频播放速度
            # 读者可以尝试将该值做更改，并观看视频播放速度的变化
            cv.waitKey(int(1000 / video.get(cv.CAP_PROP_FPS)))
            # 按下q退出
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # 输出相关信息
    print('视频中图像的宽度为：{}'.format(video.get(cv.CAP_PROP_FRAME_WIDTH)))
    print('视频中图像的高度为：{}'.format(video.get(cv.CAP_PROP_FRAME_HEIGHT)))
    print('视频帧率为：{}'.format(video.get(cv.CAP_PROP_FPS)))
    print('视频总帧数为：{}'.format(video.get(cv.CAP_PROP_FRAME_COUNT)))
    # 释放并关闭窗口
    video.release()
    cv.destroyAllWindows()
```

## chapter3/Convert_color.py

- !wget https://raw.githubusercontent.com/fengzhenHIT/learnOpenCV4_Python/main/chapter3/images/lena.jpg

```
# -*- coding:utf-8 -*-
import cv2 as cv
import sys
import numpy as np
from google.colab.patches import cv2_imshow

if __name__ == '__main__':
    # 读取图像并判断是否读取成功
    img = cv.imread('./lena.jpg')
    if img is None:
        print('Failed to read lena.jpg.')
        sys.exit()
    else:

        # 将图像进行颜色模型转换
        image = img.astype('float32')
        image *= 1.0 / 255
        HSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        YUV = cv.cvtColor(image, cv.COLOR_BGR2YUV)
        Lab = cv.cvtColor(image, cv.COLOR_BGR2Lab)
        GRAY = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        # 展示结果
        cv2_imshow(image)
        cv2_imshow(HSV)
        cv2_imshow(YUV)
        cv2_imshow(Lab)
        # 由于计算出Lab结果会有负数值，不能通过cv.imshow()函数显示
        # 因此我们可以使用cv.imwrite()函数保存下来进行查看
        cv.imwrite('./results/Convert_color_Lab.jpg', Lab)
        cv2_imshow(GRAY)

        # 关闭窗口
        cv.waitKey(0)
        cv.destroyAllWindows()
```
