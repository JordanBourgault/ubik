from main import click, write, has_note, get_rx_list, has_error, is_pdf
import time
from PIL import ImageGrab
import keyboard
import pickle

BASE_DELAY = 1
LOAD_DELAY = 2

with open('data.pickle', 'rb') as file:
    rx_list = pickle.load(file)

rx_list = rx_list[1010:]

# Setup
time.sleep(BASE_DELAY*2)
click(187, 1058)
time.sleep(BASE_DELAY*2)

for num in rx_list:
    click(80, 179)
    time.sleep(0.7*2)
    write(str(num))
    time.sleep(LOAD_DELAY*2)
    click(343, 199)
    time.sleep(0.015)
    click(343, 199)
    time.sleep((LOAD_DELAY+1)*2)

    if has_error():
        keyboard.press_and_release('esc')
        time.sleep(BASE_DELAY*2)

    if has_note():
        click(977, 187)
        time.sleep(BASE_DELAY*2)
        click(1562, 328)
        time.sleep(3)
        counter = 0
        while counter < 15:
            if is_pdf():
                im = ImageGrab.grab(bbox=(593, 27, 1322, 969))
                im.save(f'Z:\\recettes\\{str(num)}.png')
                click(1894, 8)
                time.sleep(BASE_DELAY * 2)
                break
            else:
                counter += 1
                time.sleep(1)

    click(1903, 151)
    time.sleep(LOAD_DELAY*2)
