import numpy as np
import cv2

def colors(frame,array1,array2,text,color):
    n = 0
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    Lower = np.array([array1],np.uint8)
    Upper = np.array([array2],np.uint8)
    Mask = cv2.inRange(hsv,Lower,Upper)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(Mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 5000):
            approx = cv2.approxPolyDP(contour, 0.011*cv2.arcLength(contour, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            """x,y,w,h = cv2.boundingRect(contour)
                                                frame = cv2.rectangle(frame,(x,y),(x+w, y+h),color,2)"""
            cv2.drawContours(frame, [approx], 0, color, thickness=5, lineType=None, hierarchy=None, maxLevel=None, offset=None)
            cv2.putText(frame,text,(x,y-30),cv2.FONT_HERSHEY_DUPLEX,1,color)
            n += 1
    kernal = np.ones((5,5),"uint8")
    Mask = cv2.dilate(Mask,kernal)
    print(f"{text} {n}")