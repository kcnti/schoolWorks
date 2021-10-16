import cv2
import numpy
img = cv2.imread('picc.png',1)

#Me
cv2.rectangle(img,(653,273),(833,499),(200,200,0),2)
cv2.putText(img,"Kantinun",(653,125),cv2.FONT_HERSHEY_COMPLEX,1,(123,12,99),2)
cv2.arrowedLine(img,(690,150),(700,273),(90,133,55),2)

#Ohm
cv2.circle(img,(441,397),125,(111,23,154),2)
cv2.putText(img,"Nattakit",(349,200),cv2.FONT_HERSHEY_COMPLEX,1,(116,22,255),2)

#Butter
cv2.ellipse(img,(195,473),(100,150),0,90,1000,(127,0,1),2)
cv2.putText(img,"Saksit",(170,240),cv2.FONT_HERSHEY_SIMPLEX,1,(198,168,1),3)

#Jiang
cv2.line(img,(901,245),(1083,453),(119,50,111),2)
cv2.line(img,(1083,245),(901,453),(255,0,255),2)
    #cv2.line(frame,(0,0),(640,360),(255,0,255),1)
    #cv2.line(frame,(640,0),(0,360),(255,0,255),1)
cv2.putText(img,"Pavadol",(930,200),cv2.FONT_HERSHEY_SIMPLEX,1,(112,11,111),2)

#Atom
cv2.ellipse(img,(1307,271),(100,150),0,90,1000,(0,0,0),2)
cv2.putText(img,"Thanapat",(1225,100),cv2.FONT_HERSHEY_TRIPLEX,1,(100,100,100),2)

cv2.imshow('test',img)
cv2.waitKey(0)
cv2.imwrite("finished.png",img)
cv2.destroyAllWindows