import cv2
import numpy

#facecascade = cv2.CascadeClassifier("C:\\Users\\EAI-20\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
#eyecascade = cv2.CascadeClassifier("C:\\Users\\EAI-20\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml")
fullbdcascade = cv2.CascadeClassifier("C:\\Users\\EAI-20\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_fullbody.xml")

def draw_eye(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors)  

    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
    return img

def detect(img,facecas):
    img=draw_eye(img,fullbdcascade,1.1,5,(0,0,255),"eye")
    return img

vdo = cv2.VideoCapture(0)
while(True):
    ret,frame = vdo.read()
    if ret:
        frame = detect(frame,fullbdcascade)
        cv2.imshow("vdo",frame)
        if (cv2.waitKey(1)) & 0xFF == ord('q'):
            break
vdo.release()
cv2.destroyAllWindows()