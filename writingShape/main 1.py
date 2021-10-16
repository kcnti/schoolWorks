import cv2
import numpy as np
from colors import colors

tri = 0
rec = 0
pen = 0
el = 0
cir = 0

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread("shapes.jpg", flags=1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, hierachy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
	area = cv2.contourArea(cnt, oriented=None)
	if area > 1000:
		approx = cv2.approxPolyDP(cnt, 0.011*cv2.arcLength(cnt, True), True)

		cv2.drawContours(img, [approx], 0, (0), thickness=5, lineType=None, hierarchy=None, maxLevel=None, offset=None)
		x = approx.ravel()[0]
		y = approx.ravel()[1]
		if len(approx) == 3:
			cv2.putText(img, "Triangle", (x,y), font, 1, (0), thickness=2, lineType=None, bottomLeftOrigin=None)
			tri += 1
		elif len(approx) == 4:
			cv2.putText(img, "Rectangle", (x,y), font, 1, (0), thickness=2, lineType=None, bottomLeftOrigin=None)
			rec += 1
		elif len(approx) == 5:
			cv2.putText(img, "Pentagon", (x,y), font, 1, (0), thickness=2, lineType=None, bottomLeftOrigin=None)
			pen += 1
		elif 6 < len(approx) < 11:
			el += 1
			cv2.putText(img, "Ellipse", (x,y), font, 1, (0), thickness=2, lineType=None, bottomLeftOrigin=None)
		else:
			cir += 1
			cv2.putText(img, "Circle", (x,y), font, 1, (0), thickness=2, lineType=None, bottomLeftOrigin=None)

print(f"Triangle {tri}\nRectangle {rec}\nPentagon {pen}\nEllipse {el}\nCircle {cir}")
colors(img,(160,127,127),(179,255,255),"Red",(0,0,255))
colors(img,(130,127,127),(160,255,255),"Violet",(173,68,143))
colors(img,(75,127,127),(130,255,255),"Blue",(219,152,52))
colors(img,(38,127,127),(75,255,255),"Green",(113,204,46))
colors(img,(18,127,127),(60,255,255),"Yellow",(111,220,247))
colors(img,(0,127,127),(20,255,255),"Orange",(51,118,220))
cv2.imshow("ShapesDetection", img)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()
