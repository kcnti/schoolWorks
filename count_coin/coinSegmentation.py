import cv2
import numpy as np

n = 0
img = cv2.imread("./coin.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_blur = cv2.GaussianBlur(gray,(101,101),0)
outline = cv2.Canny(gray_blur,30,150)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1)
kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,4)
contours,hierachy = cv2.findContours(gray_blur,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(contours)
print(hierachy)

for cnt in contours:
	print(cnt)
	area = cv2.contourArea(cnt)
	if area<2000 or area>70000:
		continue
	ellispe =cv2.fitEllipse(cnt)
	cv2.ellipse(img,ellispe,(0,0,255),5)
	n+=1
print(n)

cv2.imshow("coin",img)
cv2.waitKey(0)