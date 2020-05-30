import cv2 as cv
from get_keys import key_check
import numpy as np
from grabscreen import grab_screen
import time
import os

for i in list(range(4))[::-1]:
     print(i+1)
     time.sleep(1)

def key_array(key):
    output = [0,0,0]
    if 'A' in key:
        output[0] = 1
    elif 'D' in key:
        output[2] = 1
    else:
        output[1] = 1
    return output

file_name = 'training_data.npy'
if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []


while True:
    screen = grab_screen(region=(0,40,800,640))
    screen = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
    screen = cv.resize(screen, (80,60))

    keys = key_check()
    key = key_array(keys)
    training_data.append([screen,key])
    
    if cv.waitKey(25) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break
    if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name,training_data)
    
