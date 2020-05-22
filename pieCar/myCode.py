##################################################################
#
# Author: Paulius Brickus
# Date: 22/05/2020
# 
# Description: this code is made to controlle the car with W, A, S, and D keys.
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



#Import classes, functions, variables, from "mdev" files
import cv2
import curses
import time
from mDev import *

mdev = mDEV()#create object


# Get the curses window,disable echoing of keyboard to the while code is runining screen,
screen = curses.initscr()
curses.noecho() 



try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == ord('w'):
                print ("forward")
                mdev.move(500,500,90)
            elif char == ord('s'):
                print ("reverse")
                mdev.move(-800,-800,90)
            elif char == ord('d'):
                print ("right")
                mdev.move(800,300,120)
            elif char == ord('a'):
                print ("left")
                mdev.move(300,800,50)
            elif char == ord(' '):
                print ("stop")
                mdev.move(0,0)
            
finally:
    #Close down curses properly, turn echo back on!
    curses.echo()
    curses.endwin() 

