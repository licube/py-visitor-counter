#!/usr/bin/python
__author__ = 'youngbin'

from SimpleCV import *

imgone = Image("stache.png")
imgtwo = Image("stache.png")

if imgone.findKeypointMatch(imgtwo) is not None:
    print "keypoint match found"
else:
    "keypoint match not fond"


