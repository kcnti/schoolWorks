import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

vdo = cv2.VideoCapture(0)

while True:
    ret,frame = vdo.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # eyes = eye_cascade.detectMultiScale(gray,1.1,3)
        # for (ex,ey,ew,eh) in eyes:
        #     cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        
    cv2.imshow('VDO',frame)
#    if cv2.waitKey(30) & 0xff == ord('q'):
#        break
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

vdo.release()