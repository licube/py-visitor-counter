__author__ = 'youngbin'
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('HaarCascades/face.xml')

# read images
original = cv2.imread("large.jpg")
mark = cv2.imread("stache.png")

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
        crop_img = original[y:y+h, x:x+w]
        cv2.rectangle(original,(x,y),(x+w,y+h),(255,0,0),2)
        print "face detected"
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = original[y:y+h, x:x+w]
        
        x_offset=1
        y_offset=1
        mark = cv2.resize(mark, (w,h))



        # m,n = original.shape[:2]
        #
        # # create overlay image with mark at the upper left corner, use uint16 to hold sum
        # overlay = np.zeros_like(original, "uint16")
        # overlay[y:y+mark.shape[0], x:x+mark.shape[1]] = mark
        #
        # # add the images and clip (to avoid uint8 wrapping)
        # watermarked = np.array(np.clip(original+overlay, -255, 255), "uint8")
        rows,cols,channels = mark.shape
        roi = original[0:rows, 0:cols ]
        
        # Now create a mask of logo and create its inverse mask also
        markgray = cv2.cvtColor(mark,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(markgray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        
        # Now black-out the area of logo in ROI
        original_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

        
        # Take only region of logo from logo image.
        mark_fg = cv2.bitwise_and(mark,mark,mask = mask)
        
        # Put logo in ROI and modify the main image
        dst = cv2.add(crop_img,mark_fg)

        original[y:y+h, x:x+w] = dst


        cv2.imshow('img',original)
        # cv2.imshow('crop',crop_img)
        # cv2.imshow("watermarked", watermarked)
        cv2.waitKey(0)
        cv2.destroyAllWindows()