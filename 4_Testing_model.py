# test_model.py
##################################################################
#
# Author: Paulius Brickus
# Date: 22/05/2020
# 
# Description: This code takes the cretated model and feeds it live frames then takes the 
#              models perdiction out puts control commands Forward, LeftTurn, RightTurn.
# References:
#        - Evan Juras
#        - Harrison Kinsley / Sentdex
#        - Christopher Barnatt / ExplainingComputer.com
#        - Alex Krizhevsky, Ilya Sutskever & Geoffrey E. Hinton. ImageNet
#          Classification with Deep Convolutional Neural Networks. NIPS, 2012.
# Links:
#     - https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi
#     - https://github.com/sentdex/pygta5/
#     - https://www.explainingcomputers.com/rasp_pi_robotics.html
#     - [AlexNet Paper](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D
from alexnet import alexnet
from getkeys import key_check

import random

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'Assisted_driving2.00-car-{}-{}-{}-epochs-300K-data.model'.format(LR, 'alexnetv2',EPOCHS)

t_time = 0.5

def Forward():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(W)

def LeftTurn():
    PressKey(A)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(A)
    

def RightTurn():
    PressKey(D)
    ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(D)
    
model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():
    Time_Last = time.time()
    for i in list(range(10))[::-1]:
        print(i+1)
        time.sleep(2)

    pause = False
    while(True):
        
        if not pause:
            # 800x640 that lets the model see the road real time 
            frame = grab_screen(region=(0,40,800,640))
            print('loop took {} seconds'.format(time.time()-Time_Last))
            Time_Last = time.time()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame, (160,120))

            #taking the prediction from the model and printing them 
            predicted_value = model.predict([frame.reshape(160,120,1)])[0]
            print(predicted_value)

            #setting up minimum amount that the prediction needs to be
            #before a command is sent 
            turn_minimum = 0.70
            fwd_minimum = 0.75

            if predicted_value[1] > fwd_minimum:
                Forward()
            elif predicted_value[0] > turn_minimum:
                LeftTurn()
            elif predicted_value[2] > turn_minimum:
                RightTurn()
         

        Key = key_check()

        # pauses system from runing.
        if 'T' in Key:
            if pause:
                pause = False
                time.sleep(1)
            else:
                pause = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)

main()       










