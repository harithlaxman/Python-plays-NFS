import cv2 as cv
import numpy as np

print(np.__version__)


train_data = np.load('training_data.npy')

for data in train_data:
    img = data[0]
    key_press = data[1]
    cv.imshow('test', img)
    print(key_press)
    if cv.waitKey(25) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break
    
