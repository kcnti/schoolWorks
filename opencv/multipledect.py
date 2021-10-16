import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

name = []
def draw(img,cascade,scaleFactor,minNeighbors,color,clf):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    classifier = cv2.CascadeClassifier(face_cascade)
    features = classifier.detectMuiltiScale(gray,scaleFactor,minNeighbors)

    for x,y,w,h in features:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        id,con = clf.predict(gray[y:y+h,x:x+h])

        if con <= 70:
            cv2.putText(img,f"{name[id-1]}:{abs(round(100-con))}%",(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
        else:
            cv2.putText(img,"Unknown",(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
    return img

def detect(frame,cascade,clf):
    frame = draw(frame,cascade,1.1,10,(0,0,255),clf)
    return frame

vdo = cv2.VideoCapture(0)
clf = cv2.face.LBPHFaceReconizer_create()
clf.read("me.xml") #your train dataset
while True:
    ret,frame = vdo.read()
    frame = detect(frame,face_cascade,clf)
    cv2.imshow("Cam",frame)
    if (cv2.keyWait(30) & 0xff == ord('q')):
        break
vdo.release()
cv2.destroyAllWindows()
