
import numpy as np

import cv2
import time

import os

data_read = np.load('Driving_data.npy')

for data in data_read:
    img = data[0]
    choice = data[1]
    cv2.imshow('test',img)
    print(choice)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
