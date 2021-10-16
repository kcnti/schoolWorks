import cv2

vdo = cv2.VideoCapture("pixaar.mp4")
while(vdo.isOpened()):
    ret,frame = vdo.read()
    cv2.putText(frame,"HELLO",(100,200),cv2.FONT_HERSHEY_COMPLEX,5,(0,0,0),3)
    cv2.imshow('video',frame)
    if(cv2.waitKey(30) & 0xFF == ord("q")):
        break
vdo.release()
cv2.destroyAllWindows()