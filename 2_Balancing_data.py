# balance_data.py
# author: Paulius Brickus
# date 3/05/2020
# project: Assisted Driving
#
#This code is ment to balance the data before runing the training model
#as if unbalaced data is sent the model might be byass to one spacific command

from random import shuffle
import numpy as np
import pandas as pd
from collections import Counter


Collected_data = np.load('Driving_data.npy')
#print out the data to see if balanced or how unbalanced 
df = pd.DataFrame(Collected_data)
print(df.head())
print(Counter(df[1].apply(str)))

left = []
right = []
forward = []

for data in Collected_data:
    frame = data[0]
    output = data[1]
# choice and data[1] is the input data from user
# data[0] is the frames from the grabscreen
    if output == [1,0,0]:
        left.append([frame,output])
    elif output == [0,1,0]:
        forward.append([frame,output])
    elif output == [0,0,1]:
        right.append([frame,output])
    else:
        print('invalid input')

#fowards = forwards till the lenghts of lefts or rights
#lefts and rights till the lenghts of forwards
forward = forward[:len(left)][:len(right)]
left = left[:len(forward)]
right = right[:len(forward)]

All_data = forward + left + right
shuffle(All_data)
# save changes to file
np.save('Driving_data.npy', All_data)
