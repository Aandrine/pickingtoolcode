import cv2
import numpy as np

img = cv2.imread('eyetest.jpg',cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray_blurred = cv2.blur(gray,(3,3))

detected_circles = cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT,1,80,param1 = 120,
                                    param2 = 30,minRadius=60, maxRadius=90)

if detected_circles is not None:

    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0,:]:
        a,b,r = pt[0],pt[1],pt[2]

        cv2.circle(img,(a,b),r,(0,255,0),2)

        cv2.circle(img,(a,b),1,(0,0,255),3)
        cv2.imshow('detected circles',img)
        cv2.waitKey()