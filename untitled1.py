from PIL import Image
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
tela = pytesseract.image_to_string(Image.open('out11.jpg'), lang='eng')
maha = pytesseract.image_to_string(Image.open('out.jpg'), lang='eng')
anda = pytesseract.image_to_string(Image.open('out.jpg'), lang='eng')
bihar = pytesseract.image_to_string(Image.open('3.jpeg'), lang='eng')
andra = pytesseract.image_to_string(Image.open('out5.jpeg'), lang='eng')