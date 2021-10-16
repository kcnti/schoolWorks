import cv2

vdo = cv2.VideoCapture("pixaar.mp4")
while(vdo.isOpened()):
    ret,frame = vdo.read()
    cv2.ellipse(frame,(300,200),(80,50),90,480,100,(255,0,0),1)
                        #center,size,angle,endangle,color,thickness
    cv2.imshow('video',frame)
    if(cv2.waitKey(30) & 0xFF == ord("q")):
        break
vdo.release()
cv2.destroyAllWindows()