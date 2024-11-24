import pytesseract
import time
import pyautogui
import pytesseract
import os
import cv2
from PIL import Image, ImageGrab, ImageEnhance

img_str             = ''
current_screen      = 'currentscreen.png'
results_screen      = 'results_screen.png'
waiting_for_server  = 'waiting for a server'
esperando_servidor  = 'servidor'
results_words       = ['resultados', 'results', 'resultats', 'résultats']
eliminated_wors     = ['ELIMINATED!', 'ELIMINATED?', 'ELIMINADO!', 'ELIMINADO?']

ENTER_KEY   = 'enter'
ESC_KEY     = 'esc'

loc = 0
w,h = pyautogui.size()
waiting_screen = 0

print('Version 1.2')

# Validar si el tesseract está instalado
tesseract_exe = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = tesseract_exe

tess_instalado = os.path.isfile(tesseract_exe)

if not tess_instalado :
    print('Se requiere la instalación de Tesseract-OCR en el directorio :')
    print(tesseract_exe)
    time.sleep(10)
    exit(tesseract_exe)

# validar si existe la captura de pantalla de eliminado, si no existe no se puede continuar
if os.path.isfile('./eliminated.png'):
    img_str = './eliminated.png'

if(os.path.isfile('./eliminated.jpg')):
    img_str = './eliminated.jpg'

if(img_str == ''):
    print('Nos hace falta un paso para continuar...')
    print('Saca la captura de pantalla de eliminado como se indica en las instrucciones')
    exit()

# función para validar si nos encontramos en la pantalla donde se va llenando la lobby
def mismaPantalla(w,h, waiting_screen):
    try:
        bottom_screen = pyautogui.screenshot(region=(0, h-120, w, h))
        text = pytesseract.image_to_string(bottom_screen)
    except Exception as e:
        print('screen shot', e)

    if(waiting_for_server in text.lower() or esperando_servidor in text.lower()):
        waiting_screen += 1

    print('waiting_screen', waiting_screen)

    if waiting_screen >= 60:
        time.sleep(1)
        pyautogui.press(ESC_KEY)
        waiting_screen = 0

    return waiting_screen

def texto_top():
    # region left, top, right, lower
    cropped_screenshot = pyautogui.screenshot(region=(0, 0, w//2, h//5))
    text = pytesseract.image_to_string(cropped_screenshot)

    if any(word in text.lower() for word in results_words):
        print('Estamos en la pantalla de Recompensas')
        pyautogui.keyDown(ENTER_KEY)
        time.sleep(1)
        pyautogui.keyUp(ENTER_KEY)

while True:
    time.sleep(2)
    loc+=1

    try:
        waiting_screen = mismaPantalla(w,h, waiting_screen)
        texto_top()

        located = pyautogui.locateOnScreen(img_str, confidence=0.9, grayscale=True, region=(w//2, 0, w, h))
        #print("LOCATED ", located)
        print("Fuimos eliminados, saliendo de partida...")
        pyautogui.press(ESC_KEY)
        waiting_screen = 0
    except Exception as e:
        print('continuar ', e)

    pyautogui.press(ENTER_KEY)