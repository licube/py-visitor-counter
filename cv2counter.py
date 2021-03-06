#-*- coding: utf-8 -*-

__author__ = 'youngbin'

import cv2
import numpy

MIN_MATCH_COUNT = 10
ORB = cv2.FastFeatureDetector_create(100,1,"ORB")


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('HaarCascades/face.xml')


while(True):
    print "new frame"
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        print "face detected"
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        


        


    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


