import cv2

vdo = cv2.VideoCapture("pixaar.mp4")
while(vdo.isOpened()):
    ret,frame = vdo.read()
    #cv2.line(frame,(0,0),(640,360),(255,0,255),1)
    #cv2.line(frame,(640,0),(0,360),(255,0,255),1)
    cv2.rectangle(frame,(0,0),(300,200),(255,0,0),0) # -1 for fill
    cv2.imshow('video',frame)
    if(cv2.waitKey(30) & 0xFF == ord("q")):
        break
vdo.release()
cv2.destroyAllWindows()