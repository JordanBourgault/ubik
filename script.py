from main import click, write, has_note, get_rx_list, has_error
import time
from PIL import ImageGrab
import keyboard

BASE_DELAY = 1
LOAD_DELAY = 2

rx_list = get_rx_list()[870:]

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
        time.sleep(8)
        im = ImageGrab.grab(bbox=(593, 27, 1322, 969))
        im.save(f'Z:\\recettes\\{str(num)}.png')
        click(1894, 8)
        time.sleep(BASE_DELAY*2)
    click(1903, 151)
    time.sleep(LOAD_DELAY*2)
