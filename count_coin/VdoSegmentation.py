import cv2
import numpy as np
import time
cap = cv2.VideoCapture("coin.mp4")
#try:
while cap.read():

	ret,frame = cap.read()
	#frame=frame[:1080,0:1920]
	if ret:
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		gray_blur=cv2.GaussianBlur(gray,(15,15),0)
		thresh=cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1)
		kernel=np.ones((3,3),np.uint8)
		closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=4)
		contours,hierachy=cv2.findContours(closing,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		n = 0
		print(contours)
		for coin in contours:
			area = cv2.contourArea(coin)
			print(area)
			if area<2000 or area>70000:
				continue
			ellipse = cv2.fitEllipse(coin)
			cv2.ellipse(frame,ellipse,(0,255,0),5)
			n += 1
		cv2.putText(frame,str(n),(10,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
		print(n)

		cv2.imshow("coins",frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()

#except:
#	print("End")