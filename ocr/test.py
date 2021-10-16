import pytesseract
from PIL import Image, ImageGrab

img = Image.open('Hello-EAI.jpg')
result = pytesseract.image_to_string(img, lang='tha+eng')
print(result)
