import numpy as np
import cv2
from random import shuffle
import pandas as pd

train_data = np.load('training_data.npy')
shuffle(train_data)
W = []
A = []
D = []
for data in train_data:
    image = data[0]
    key = data[1]
    if key == [1,0,0]:
        A.append([key, image])
    elif key == [0,1,0]:
        W.append([key, image])
    elif key == [0,0,1]:
        D.append([key, image])
    cv2.imshow('sample', image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


