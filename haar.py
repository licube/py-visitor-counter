#!/usr/bin/python
#-*- coding: utf-8 -*-
import time, webbrowser
from operator import add
from SimpleCV import Color, ColorCurve, Camera, Image, pg, np, cv, HaarCascade, DrawingLayer
from SimpleCV.Display import Display

cam = Camera()
time.sleep(.1) # 0.5초 대기
counter = 0
# cascades 불러오기
face_cascade = HaarCascade("HaarCascades/face.xml")
nose_cascade = HaarCascade("HaarCascades/nose.xml")
stache = Image("stache.png") # 수염 이미지 불러오기
count = 0
display = Display((800,600))

#딱봐도 무한반복
while ( display.isNotDone() ):
    img = cam.getImage()
    # img = img.scale(.5)
    face = img.findHaarFeatures(face_cascade)
    if face is not None:
        print "FACE is NOT NONE"
        print "안면 인식됨"
        try:
            # 얼굴 영역 검출
            face = face.sortArea()
            facesort = face[-1]
            facesort.show()
            croped = facesort.crop()
            # croped.draw()
            noses = croped.findHaarFeatures(nose_cascade)
            # croped.save("Face-"+time.strftime("%H:%M:%S")+".png")
            if noses is not None :  # 코 보이는 경우
                #에이어 생성
                myLayer = DrawingLayer((img.width,img.height))

                print "코 인식됨"
                noses = noses.sortArea()
                nose = noses[0]  # get the biggest
                print "코 X좌표"
                print nose.x
                print "코 Y좌표"
                print nose.y

                NoseHW = nose.width() * 0.5
                NoseHH = nose.height() * 0.5
                FaceHW = facesort.width() * 0.5
                FaceHH = facesort.height() * 0.5

                FaceX = face.x


                # these get the upper left corner of the face/nose
                # with respect to original image
                xf = facesort.x - FaceHW
                yf = facesort.y - FaceHH
                xm = nose.x - NoseHW
                ym = nose.y - NoseHH
                #calculate the mustache position
                xmust = xf+xm-(stache.width/2)+(nose.width()/2)
                ymust = yf+ym+(2*nose.height()/3)
                #blit the stache/mask onto the image
                # nose.draw()
                #코에 수엄 표시
                myLayer.blit(stache, (xmust,ymust))
                #얼굴영역 표시
                myLayer.circle((facesort.x, facesort.y), 100, Color.BLUE)
                img.addDrawingLayer(myLayer)
                # img.scale(2.0)



        except IndexError:
            print "IndexError 발생"




    elif face is None:
        print "FACE is NONE"
        # img.scale(2.0)


    img.show()
