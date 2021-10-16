# coding=utf-8
import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageGrab
def convertImage(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 100, 200)
    return canny
image = cv2.imread('license.jpg')
process_img = convertImage(image)
original_img = image.copy()
contour_img = process_img.copy()
contours, heirarchy = cv2.findContours(contour_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:4]
for contour in contours:
    p = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02*p, True)
    if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(contour)
        license_img = original_img[y:y+h,x:x+w]
        cv2.imshow('License Detected', license_img)
        cv2.drawContours(image, [contour], -1, (0, 255, 255), 3)
        cv2.imwrite('plate.jpg', license_img)
img = Image.open('plate.jpg')
result = pytesseract.image_to_string(img, lang='tha+eng')
cv2.putText(image, result, (x,y), cv2.FONT_HERSHEY_PLAIN, 0.8, (255,255,255), 2)
cv2.imshow('img', image)
print(result)
cv2.waitKey(0)
