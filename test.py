import cv2
import pyscreenshot
import pyautogui
import pytesseract

tesseract_exe = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = tesseract_exe

current_screen = 'currentscreen.png';

w,h = pyautogui.size()
print(w, h)

pic = pyscreenshot.grab(bbox=(0, h-120, w, h))

pic.show()

pic.save(current_screen)

img = cv2.imread(current_screen)
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)

print(text)