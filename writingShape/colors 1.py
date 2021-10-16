import numpy as np
import cv2

def colors(frame,array1,array2,text,color):
    n = 0
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    Lower = np.array([array1],np.uint8)
    Upper = np.array([array2],np.uint8)
    Mask = cv2.inRange(hsv,Lower,Upper)
    contours,hierarchy = cv2.findContours(Mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 5000):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w, y+h),color,2)
            cv2.putText(frame,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,1,color)
            n += 1
    kernal = np.ones((5,5),"uint8")
    Mask = cv2.dilate(Mask,kernal)
    print(f"{text} {n}")