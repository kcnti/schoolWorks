import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyecascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')


def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,clf):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors) 
    scale = []
    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        id, con = clf.predict(cvtgray[y:y+h,x:x+w])

        if con <= 45: #ถ้า % >= 60 ก็คือ Earth
            cv2.putText(img,'Earth',(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
        else:
            cv2.putText(img,'who?',(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
        
        if (con < 100):
            con = "you look like Earth {0}%".format(round(100-con))
        else:
            con = "you look like Earth {0}%".format(round(100-con))
        print(str(con))
        scale = [x,y,w,h]
    return img,scale


def detect (img,faceCascade,pic_no,clf):
    img,scale = draw_boundary(img,faceCascade,1.1,10,(0,0,255),clf)
    if len(scale) == 4:
        id = 1
        pic_crop = img[scale[1]:scale[1]+scale[3],scale[0]:scale[0]+scale[2]]
                    #    y         (y+h)             x          (x+w)
        #create_modelpicture(pic_crop,id,pic_no)
    return img

pic_no = 0
vdo = cv2.VideoCapture(0)
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("earth.xml")

while(True):
    ret,frame = vdo.read()
    if ret:
        frame = detect(frame,faceCascade,pic_no,clf)
        frame = eyecascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=5)
        pic_no += 1
        cv2.imshow('face detection',frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
vdo.release()
cv2.destroyAllWindows()