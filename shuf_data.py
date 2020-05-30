import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('training_data.npy')
data_frame = pd.DataFrame(train_data)

W = []
A = []
D = []

print(Counter(data_frame[1].apply(str)))
shuffle(train_data)

for data in train_data:
    game_frame = data[0]
    key = data[1]

    if key == [1,0,0]:
        A.append([game_frame, key])
    if key == [0,1,0]:
        W.append([game_frame, key])
    if key == [0,0,1]:
        D.append([game_frame, key])

w = W[:len(A)][:len(D)]
A = A[:len(W)]
D = D[:len(D)]

final_data = W+A+D
shuffle(final_data)
print(len(final_data))
np.save('final_data.npy', final_data)

