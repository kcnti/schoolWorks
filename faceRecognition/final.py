import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
treshold = 70

def draw(img, cascade, scaleFactor, minNeighbors, color, clf):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    eye = eyeCascade.detectMultiScale(img,1.1)
    faces = faceCascade.detectMultiScale(gray, 1.3,10)
    for x,y,w,h in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        id, con = clf.predict(gray[y:y+h,x:x+h])
        print(con)
        if con <= treshold:
#            cv2.putText(img, f"{name}: {abs(round(100-con))}%",(x,y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            cv2.putText(img,f"Kantinun: {abs(round(100-con))}",(x,y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color,2)
        else:
            cv2.putText(img, "M",(x,y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color,2)

    # for (ex,ey,ew,eh) in eye:
    #     cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),1)

    return img

def detect(frame, cascade, clf):
   frame = draw(frame, cascade, 1.1, 1000, (0,0,255), clf)
   return frame

cap = cv2.VideoCapture(0)
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("./earth.xml")
#clf.read("m.xml")
while True:
    ret,frame = cap.read()
    if ret:
        frame = detect(frame, faceCascade, clf)
        cv2.imshow('lol', frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
cap.release()
cv2.destroyAllWindows()
