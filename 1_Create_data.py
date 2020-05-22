# Create_data.py
# author: Paulius Brickus
# date 3/05/2020
# project: Assisted Driving
#
#This codes made to capture the topself corner of the screen size of 800x640
#and read inputs from the user and store everthing in a file called driving_data

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os

def keys_to_output(keys):
#   set up the keys used as an array
#   output = [A,W,D]
    output = [0,0,0]
    
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output

file_name = 'Driving_data.npy'
#check to see if the file exists. If not create the file 
if os.path.isfile(file_name):
    print('File already exist loading!')
    train_data = list(np.load(file_name))
else:
    print('No file with that name, creating file!')
    train_data = []

def main():
#count down for program to start 
    for i in list(range(10))[::-1]:
        print(i+1)
        time.sleep(2)

    pause = False
    while(True):
#the screen grab, after which change it to gray scale
#and output the frames and output from user to the file created 
        if not paused:
            frame = grab_screen(region=(0,40,800,640))
            last_time = time.time()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame, (160,120))
            keys = key_check()
            output = keys_to_output(keys)
            train_data.append([frame,output])
            
            if len(train_data) % 1000 == 0:
                print(len(train_data))
                np.save(file_name,train_data)
#pause the code 
        keys = key_check()
        if 'T' in keys:
            if paused:
                pause = False
                print('resume!')
                time.sleep(1)
            else:
                print('pausing!')
                pause = True
                time.sleep(1)


main()
