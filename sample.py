
__author__ = 'youngbin'
from SimpleCV import *
import time

#Threshold
threshold = 1

# Initialize the camera
cam = Camera()

# Get Reference Image from camera
print "Getting Reference Image"
refImg = cam.getImage()

# Save Image for Reference
refImg.save("reference.png")

print "Reference Created"

# Loop to continuously get images
while True:
    # Get New Image from camera
    img = cam.getImage()
    img.show()

    # Get Differences between two Images
    imgmath = refImg - img
    print "=========="
    print imgmath.getNumpyCv2().mean()
    print "=========="

    if imgmath.getNumpy().mean() > threshold:
        #Update Reference
        refImg = img
        img.save("reference.png")
        img.drawText("Motion Detected At"+time.strftime("%H:%M:%S"))
        img.show()
        #Save Image
        img.save("Motion_Detected_At"+time.strftime("%H:%M:%S")+".png")
        print "Motion Detected"



