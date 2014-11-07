#-*- coding: utf-8 -*-
__author__ = 'youngbin'
from SimpleCV import *
import time

#임계값
threshold = 1.0

# 카메라 초기화
cam = Camera()

# 카메라에서 이미지 얻어 기준 이미지로 정하기
print "기준 이미지 얻는중"
refImg = cam.getImage()

# 기준 이미지 저장
refImg.save("reference.png")

print "기준 이미지 생성됨"

# 무한 반복
while True:
    # 새 이미지 얻기
    img = cam.getImage()
    # img.drawText("Showing Reference")
    img.show()

    # 기준 이미지와 새 이미지 사이 차이 얻기
    imgmath = refImg - img
    print "=========="
    print imgmath.getNumpy().mean()
    print "=========="

    # 차이가 임계값 보다 크면
    if imgmath.getNumpy().mean() > threshold:
        print "움직임 감지됨"
        # 기준 이미지 갱신
        refImg = img
        img.save("reference.png")
        img.drawText("Motion Detected At"+time.strftime("%H:%M:%S"))
        print "기준 이미지 갱신"
        img.show()
        #Save Image
        img.save("Motion_Detected_At"+time.strftime("%H:%M:%S")+".png")
        print "갱신시각" + time.strftime("%H:%M:%S")
    else:
        print "기준 이미지와 큰 차이 없음 기준 이미지 유지"






