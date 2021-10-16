import cv2
import classifier
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

vdo = cv2.VideoCapture(0)
while(True):
    ret,frame = vdo.read()
#    frame = classifier.detect_face(frame,facecascade)
#    frame = classifier.detect_eye(frame,eyecascade)
#    frame = classifier.detect_bd(frame,fullbody)
#    frame = classifier.detect_cat_face(frame,cat_face)
#    frame = classifier.detect_leye(frame,lefteye)
#    frame = classifier.detect_lwbd(frame,lowerbody)
#    frame = classifier.detect_reye(frame,righteye)
#    frame = classifier.detect_upbd(frame,upperbody)
#    frame = classifier.detect_smile(frame,smile)
    frame = classifier.detect_eteg(frame,eye_tree_glasses)

    cv2.imshow("vdo",frame)
    if (cv2.waitKey(1)) & 0xFF == ord('q'):
        break
vdo.release()
cv2.destroyAllWindows()
