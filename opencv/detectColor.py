import cv2
import numpy as np

cap = cv2.VideoCapture(1)

def colors(array1,array2,text,color):
	ret,frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #hue saturation value
	lower = np.array([array1],np.uint8)
	upper = np.array([array2],np.uint8)
	mask = cv2.inRange(hsv,lower,upper)
	contours,hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if area > 5000:
			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
			cv2.putText(frame,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,1,color)
	kernal = np.ones((5,5),"uint8")
	mask = cv2.dilate(mask,kernal)
	cv2.imshow("DetectColor",frame)

while True:

	colors((160,127,127),(179,255,255),"Red",(0,0,255)) #Red
	if cv2.waitKey(1) & 0xFF == ord("q"):
		cv2.destroyAllWindows()
		break