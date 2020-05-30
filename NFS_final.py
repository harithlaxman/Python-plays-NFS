import numpy as np
from PIL import ImageGrab
import cv2
import time
from directxkeys import PressKey,ReleaseKey, W, A, S, D
from alexnet import alexnet

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'pygta5-car-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',EPOCHS)

def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def left():
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(W)

def right():
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(W)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

from get_keys import key_check

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        
        if not paused:
            # 800x600 windowed mode
            screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (80,60))
            moves = list(np.around(model.predict([screen.reshape(80,60,1)])[0]))
            if moves == [1,0,0]:
                left()
            elif moves == [0,1,0]:
                straight()
            elif moves == [0,0,1]:
                right()
   
        keys = key_check()

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)
main()
