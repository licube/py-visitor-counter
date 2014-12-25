__author__ = 'youngbin'
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('HaarCascades/face.xml')
twoeye_cascade = cv2.CascadeClassifier('HaarCascades/two_eyes_big.xml')

# read images
original = cv2.imread("large.jpg")
fdeco = cv2.imread("stache.png")
edeco = cv2.imread("glasses.png")

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
        crop_img = original[y:y+h, x:x+w]
        cv2.rectangle(original,(x,y),(x+w,y+h),(255,0,0),2)
        print "face detected"
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = original[y:y+h, x:x+w]
        eyes = twoeye_cascade.detectMultiScale(roi_gray)
        x_offset=1
        y_offset=1
        fdeco = cv2.resize(fdeco, (w,h))

        # m,n = original.shape[:2]
        #
        # # create overlay image with fdeco at the upper left corner, use uint16 to hold sum
        # overlay = np.zeros_like(original, "uint16")
        # overlay[y:y+fdeco.shape[0], x:x+fdeco.shape[1]] = fdeco
        #
        # # add the images and clip (to avoid uint8 wrapping)
        # waterfdecoed = np.array(np.clip(original+overlay, -255, 255), "uint8")
        rows,cols,channels = fdeco.shape
        roi = original[0:rows, 0:cols ]
        
        # Now create a mask of logo and create its inverse mask also
        fdecogray = cv2.cvtColor(fdeco,cv2.COLOR_BGR2GRAY)
        ret, fmask = cv2.threshold(fdecogray, 10, 255, cv2.THRESH_BINARY)
        fmask_inv = cv2.bitwise_not(fmask)
        
        # Now black-out the area of logo in ROI
        original_bg = cv2.bitwise_and(roi, roi, mask = fmask_inv)

        
        # Take only region of logo from logo image.
        fdeco_fg = cv2.bitwise_and(fdeco,fdeco,mask = fmask)
        
        # Put logo in ROI and modify the main image
        dst = cv2.add(crop_img,fdeco_fg)

        original[y:y+h, x:x+w] = dst

        for (ex,ey,ew,eh) in eyes:
                eyecrop = roi_color[y:y+h, x:x+w]
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                edeco = cv2.resize(edeco, (ew,eh))
            
                erows,ecols,echannels = edeco.shape
                eroi = roi_color[0:erows, 0:ecols ]
                
                # Now create a mask of logo and create its inverse mask also
                edecogray = cv2.cvtColor(edeco,cv2.COLOR_BGR2GRAY)
                ret, emask = cv2.threshold(edecogray, 10, 255, cv2.THRESH_BINARY)
                emask_inv = cv2.bitwise_not(emask)
                
                # Now black-out the area of logo in ROI
                eoriginal_bg = cv2.bitwise_and(eroi, eroi, mask = emask_inv)
        
                
                # Take only region of logo from logo image.
                edeco_fg = cv2.bitwise_and(edeco,edeco,mask = emask)
                
                # Put logo in ROI and modify the main image
                edst = cv2.add(eyecrop,edeco_fg) # ERROR
        
                roi_color[ey:ey+eh, ex:ex+ew] = edst

        cv2.imshow('img',original)
        # cv2.imshow('crop',crop_img)
        # cv2.imshow("waterfdecoed", waterfdecoed)
        cv2.waitKey(0)
        cv2.destroyAllWindows()