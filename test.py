from main import get_pos, is_closed
import time
import keyboard
import PIL.ImageGrab
import pickle

# get_pos(4)
# print(is_closed())

with open('new_data.pickle', 'rb') as file:
    rx_list = pickle.load(file)

for i in range(len(rx_list)):
    if rx_list[i] == '448538':
        print(i)
