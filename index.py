import pyscreenshot
import pytesseract
import pyautogui as gui
from keyboard import press
import time

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

while True:
    time.sleep(5)
    pic = pyscreenshot.grab(bbox=(440, 430, 920, 900))  # x1 y1 x2 y2
    custom_config = r'-l eng --oem 3 --psm 6'
    text = pytesseract.image_to_string(pic, config=custom_config)
    if text == "":
        continue
    gui.typewrite(text)
    time.sleep(1)
    press('Tab')
    time.sleep(1)
    press('Enter')
