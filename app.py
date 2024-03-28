import pytesseract
import time
import pyautogui
import os
import cv2
from PIL import Image, ImageGrab

tesseract_exe = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = tesseract_exe

tess_instalado = os.path.isfile(tesseract_exe)

if not tess_instalado :
    print('Se requiere la instalación de Tesseract-OCR en el directorio :')
    print(tesseract_exe)
    time.sleep(10)
    exit(tesseract_exe)

print('Version 1.1')

current_screen = 'currentscreen.png'
waiting_for_server = 'waiting for a server'
esperando_servidor = 'servidor'
w,h = pyautogui.size()
waiting_screen = 0

def mismaPantalla(w,h, waiting_screen):

    pic = ImageGrab.grab(bbox=(0, h-120, w, h))
    #pic = pyscreenshot.grab(bbox=(0, h-120, w, h))
    #pic.show()
    pic.save(current_screen)

    try:
        img = cv2.imread(current_screen)
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(img, config=custom_config)
        print('text ', text)
    except Exception as e:
        print('screen shot', e)

    if(waiting_for_server in text.lower() or esperando_servidor in text.lower()):
        waiting_screen += 1

    print('waiting_screen', waiting_screen)

    if waiting_screen >= 60:
        time.sleep(1)
        pyautogui.press('esc')
        waiting_screen = 0

    return waiting_screen


loc = 0
while True:
    time.sleep(2)
    loc+=1

    try:
        img_str = ''
        waiting_screen = mismaPantalla(w,h, waiting_screen)

        if os.path.isfile('./eliminated.png'):
            img_str = './eliminated.png'

        if(os.path.isfile('./eliminated.jpg')):
            img_str = './eliminated.jpg'

        located = pyautogui.locateOnScreen(img_str, confidence=0.9, grayscale=True, region=(int(w/2), int(h/2), w, h))
        print("LOCATED ", located)
        #print(typeof(locate[0]))
        #screenshot = pyautogui.screenshot(region=(1462,873,387,71))
        #pic = ImageGrab.grab(bbox=located)
        #screenshot.save(str(loc)+'located.png')
        print("Fuimos eliminados, saliendo de partida...")
        pyautogui.press('esc')
        waiting_screen = 0
    except Exception as e:
        print('continuar ', e)

    pyautogui.press('enter')