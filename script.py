from main import click, write, has_note, has_error, is_pdf, has_search_res, has_pdf, is_closed
import time
from PIL import ImageGrab
import keyboard
import pickle

BASE_DELAY = 1
LOAD_DELAY = 2

with open('data.pickle', 'rb') as file:
    rx_list = pickle.load(file)

rx_list = rx_list[1220:]

# Setup
time.sleep(BASE_DELAY*2)
click(187, 1058)
time.sleep(BASE_DELAY*2)
click(80, 179)

for num in rx_list:
    time.sleep(0.5)
    write(str(num))

    counter = 0
    while counter <= 30:
        if has_search_res():
            click(343, 199)
            time.sleep(0.015)
            click(343, 199)
            break
        counter += 1
        time.sleep(0.1)
    if counter >= 30:
        continue

    time.sleep(1)
    count = 0
    while count <= 10:
        if has_error():
            keyboard.press_and_release('esc')
            time.sleep(BASE_DELAY*2)

        if has_note():
            click(977, 187)

            time.sleep(0.5)
            count_print = 0
            while count_print <= 30:
                if has_pdf():
                    click(1562, 328)
                    break
                count_print += 1
                time.sleep(0.1)

            time.sleep(2)
            counter = 0
            while counter <= 10:
                if is_pdf():
                    im = ImageGrab.grab(bbox=(593, 27, 1322, 969))
                    im.save(f'Z:\\recettes\\{str(num)}.png')
                    time.sleep(0.1)
                    click(1894, 8)
                    time.sleep(BASE_DELAY * 2)
                    break
                else:
                    counter += 1
                    time.sleep(0.5)
            break
        count += 1
        time.sleep(0.5)

    click(1903, 151)

    counter = 0
    while counter < 40:
        if is_closed():
            break
        counter += 1
        time.sleep(0.1)
