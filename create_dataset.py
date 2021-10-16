import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#functiom draw face
def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
    cvtgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(cvtgray,scaleFactor,minNeighbors) 
    scale = []
    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_TRIPLEX,0.8,color,2)
        scale = [x,y,w,h]
    return img,scale

#function save
def create_modelpicture(pic,id,pic_no):
    cv2.imwrite('D:/__PROJ/_WORK/coding/python/_project/data/pic.'+str(id)+'.'+str(pic_no)+'.jpg',pic)

#function detect face
def detect (img,faceCascade,pic_no):
    img,scale = draw_boundary(img,faceCascade,1.1,10,(0,0,255),'face')
    if len(scale) == 4:
#        id = 1
        pic_crop = img[scale[1]:scale[1]+scale[3],scale[0]:scale[0]+scale[2]]
                    #    y         (y+h)             x          (x+w)
        create_modelpicture(pic_crop,id,pic_no)
    return img

if '__main__' == __name__:
    vdo = cv2.VideoCapture(1)
    pic_no = 0
    id = input("Enter id: ")
    while(True):
        ret,frame = vdo.read()
        if ret:
            frame = detect(frame,faceCascade,pic_no)
            #rotate = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
            pic_no += 1
        #    cv2.imshow('face detection',frame)
        #    frame2 = cv2.imshow(rotate,1)
            cv2.imshow('face detection', frame)
            print(f"id : {id}, no : {pic_no}")
            if(cv2.waitKey(1) & 0xFF == ord('q')):
                break
    vdo.release()
    cv2.destroyAllWindows()