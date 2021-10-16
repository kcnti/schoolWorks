import cv2

vdo = cv2.VideoCapture("pixaar.mp4")
while(vdo.isOpened()):
    ret,frame = vdo.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video',gray)
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break
vdo.release()
cv2.destroyAllWindows()