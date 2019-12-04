import win32api
import win32con
import time
import keyboard
import PIL.ImageGrab
from PIL import Image


NOTE_REF_IMAGE = Image.open('note.png').histogram()
ERR_REF_IMAGE = Image.open('error.png').histogram()
GRAY_REF_IMAGE = Image.open('gray.png').histogram()
PDF_REF_IMAGE = Image.open('pdf_ref.png').histogram()
SEARCH_REF_IMAGE = Image.open('search_ref.png').histogram()
PRINT_REF_IMAGE = Image.open('print.png').histogram()
CLOSED_REF_IMAGE = Image.open('closed.png').histogram()


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def write(text):
    keyboard.write(text)


def get_pos(t):
    for i in range(int(t)):
        print(f'{t - i}')
        time.sleep(1)
    print(win32api.GetCursorPos())


def get_rx_list():
    rx_number_list = []
    with open('ord_2019_v2.csv', newline='\r\n') as file:
        for line in file:
            rx_number = line.split(';')[0].split('\n')[0][1:]
            rx_number_list.append(rx_number)

    rx_number_list = rx_number_list[2:]
    return rx_number_list


def has_note():
    image = PIL.ImageGrab.grab(bbox=(940, 170, 1015, 199)).histogram()
    return NOTE_REF_IMAGE == image


def has_error():
    image = PIL.ImageGrab.grab(bbox=(1033, 100, 1035, 102)).histogram()
    if GRAY_REF_IMAGE == image:
        return False
    return ERR_REF_IMAGE != image


def is_pdf():
    image = PIL.ImageGrab.grab(bbox=(836, 985, 896, 1032)).histogram()
    return PDF_REF_IMAGE == image


def has_search_res():
    image = PIL.ImageGrab.grab(bbox=(1091, 195, 1093, 197)).histogram()
    return SEARCH_REF_IMAGE == image


def has_pdf():
    image = PIL.ImageGrab.grab(bbox=(1559, 312, 1592, 339)).histogram()
    return PRINT_REF_IMAGE == image


def is_closed():
    image = PIL.ImageGrab.grab(bbox=(1667, 141, 1707, 163)).histogram()
    return CLOSED_REF_IMAGE == image
