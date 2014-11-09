#!/usr/bin/python
#-*- coding: utf-8 -*-

from SimpleCV import *
import os
import glob
import time
import pygame
import cv2

images_path = "visitors/"  #put your image path here if you want to override current directory
extension = "*.png"
quality = 400
minMatch = 0.4
minDist = 0.2
print SimpleCV.__version__
print pygame.__version__
print cv2.__version__
if not images_path:
        path = os.getcwd() #get the current directory
else:
        path = images_path

imgs = list() #load up an image list
directory = os.path.join(path, extension)
files = glob.glob(directory)
filecount = len(files)
print "Number of Files"
print len(files)

cam = Camera()
time.sleep(.1)
counter = 0
face_cascade = HaarCascade("HaarCascades/face.xml")

while True:
    img = cam.getImage()
    faces = img.findHaarFeatures(face_cascade)
    try:
        if faces is not None:
            print "Found Face"
            faces.draw()
            faces = faces.sortArea()
            face = faces[-1]
            newvisitor = face.crop()
            if filecount == 0:
                print "Visitors - no visitor yet"
                newvisitor.save("visitors/0.png")
                filecount += 1
            else:
                print "Visitors - One or more"

            for file in files:
                print file
                visited = Image(file)
                print "Imaged Loaded"
                visited.show()
                time.sleep(0.5)
                newvisitor.show()
                time.sleep(0.5)
                keypoints = visited.findKeypointMatch(newvisitor)
                print "Found Keypoint match percentage"
                if keypoints:
                    print "Y"
                else:
                    print "N"
    except:
        print"Exception Error"
    img.show()
