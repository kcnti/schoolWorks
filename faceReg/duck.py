import cv2

image = cv2.imread('duck.jpg',0)
cv2.imshow('test',image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
cv2.imwrite('duckblack.jpg',image)
