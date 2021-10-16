import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def colors(frame,array1,array2,text,color):
    n = 0
    Lower = np.array([array1],np.uint8)
    Upper = np.array([array2],np.uint8)
    Mask = cv2.inRange(hsv,Lower,Upper)
    _, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
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

while True:
    ret,frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        colors(frame,(160,127,127),(179,255,255),"Red",(0,0,255))
        colors(frame,(130,127,127),(160,255,255),"Violet",(173,68,143))
        colors(frame,(75,127,127),(130,255,255),"Blue",(219,152,52))
        colors(frame,(38,127,127),(75,255,255),"Green",(113,204,46))
        colors(frame,(26,127,127),(38,255,255),"Yellow",(111,220,247))
        colors(frame,(0,127,127),(20,255,255),"Orange",(51,118,220))
        
        cv2.imshow("Detect Color",frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            #cap.read()
            cv2.destroyAllWindows()
            break
