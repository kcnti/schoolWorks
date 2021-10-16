import cv2
facecascade = cv2.CascadeClassifier("C:\\Users\\EAI-20\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
eyecascade = cv2.CascadeClassifier("C:\\Users\\EAI-20\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml")
fullbody = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
cat_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
lefteye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lefteye_2splits.xml')
lowerbody = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lowerbody.xml')
righteye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_righteye_2splits.xml')
upperbody = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')
smile = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
eye_tree_glasses = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')


#face
def draw_face(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors)  

    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
    return img

def detect_face(img,facecas):
    img=draw_face(img,facecascade,1.1,20,(0,0,255),"face")
    return img

#eye
def draw_eye(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors)  

    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
    return img

def detect_eye(img,facecas):
    img=draw_eye(img,eyecascade,1.1,10,(255,0,0),"eye")
    return img

#body
def draw_bd(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors)  

    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
    return img

def detect_bd(img,classifi):
    img=draw_eye(img,fullbody,1.1,5,(0,0,255),"body")
    return img 

#cat_face
def draw_cat_face(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors)  

    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
    return img

def detect_cat_face(img,classifi):
    img=draw_cat_face(img,cat_face,1.1,10,(0,0,255),"cat")
    return img

#lefteye_2split
def draw_leye(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors)  

    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
    return img

def detect_leye(img,classifi):
    img=draw_leye(img,lefteye,1.1,5,(0,0,255),"left_eye")
    return img 

#lowerbody
def draw_lwbd(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors)  

    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
    return img

def detect_lwbd(img,classifi):
    img=draw_lwbd(img,lowerbody,1.1,5,(0,0,255),"lower body")
    return img

#righteye
def draw_reye(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors)  

    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
    return img

def detect_reye(img,classifi):
    img=draw_reye(img,righteye,1.1,5,(0,0,255),"right_eye")
    return img 

#upperbody
def draw_upbd(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors)  

    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
    return img

def detect_upbd(img,classifi):
    img=draw_upbd(img,upperbody,1.1,10,(0,0,255),"upper_body")
    return img 

#smile
def draw_smile(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors)  

    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
    return img

def detect_smile(img,classifi):
    img=draw_smile(img,smile,1.1,50,(0,0,255),"smile")
    return img

#eye_tree_eyeglasses
def draw_eteg(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors)  

    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
    return img

def detect_eteg(img,classifi):
    img=draw_eteg(img,eye_tree_glasses,1.1,10,(0,0,255),"eye_tree_glasses")
    return img 