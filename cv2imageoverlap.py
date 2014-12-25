__author__ = 'youngbin'
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('HaarCascades/face.xml')
twoeye_cascade = cv2.CascadeClassifier('HaarCascades/two_eyes_big.xml')
mouth_cascade = cv2.CascadeClassifier('HaarCascades/mouth.xml')

# read images
original = cv2.imread("large.jpg")
fdeco = cv2.imread("stache.png")
edeco = cv2.imread("stache.png")
mdeco = cv2.imread("stache.png")


gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
        crop_img = original[y:y+h, x:x+w]
        cv2.rectangle(original,(x,y),(x+w,y+h),(255,0,0),2)
        print "face detected"
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = original[y:y+h, x:x+w]
        eyes = twoeye_cascade.detectMultiScale(roi_gray)
        mouthes = mouth_cascade.detectMultiScale(roi_gray)
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
                eyecrop = roi_color[ey:ey+eh, ex:ex+ew]
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
        
                original[y+ey:y+ey+eh, x+ex:x+ex+ew] = edst

        for (mx,my,mw,mh) in mouthes:
                mouthcrop = roi_color[my:my+mh, mx:mx+mw]
                cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,255,0),2)
                mdeco = cv2.resize(mdeco, (mw,mh))

                mrows,mcols,mchannels = mdeco.shape
                mroi = roi_color[0:mrows, 0:mcols ]

                # Now create a mask of logo and create its inverse mask also
                mdecogray = cv2.cvtColor(mdeco,cv2.COLOR_BGR2GRAY)
                ret, mmask = cv2.threshold(mdecogray, 10, 255, cv2.THRESH_BINARY)
                mmask_inv = cv2.bitwise_not(mmask)

                # Now black-out the area of logo in ROI
                moriginal_bg = cv2.bitwise_and(mroi, mroi, mask = mmask_inv)


                # Take only region of logo from logo image.
                mdeco_fg = cv2.bitwise_and(mdeco,mdeco,mask = mmask)

                # Put logo in ROI and modify the main image
                mdst = cv2.add(mouthcrop,mdeco_fg) # ERROR

                original[y+my:y+my+mh, x+mx:x+mx+mw] = mdst

        cv2.imshow('img',original)
        # cv2.imshow('crop',crop_img)
        # cv2.imshow("waterfdecoed", waterfdecoed)
        cv2.waitKey(0)
        cv2.destroyAllWindows()