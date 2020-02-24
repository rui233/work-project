# -*- coding: utf-8 -*-

# First, capture a picture from USB camera of common drink in China.
# Second, predict the name of the drink by loading the trained model(trained by train.py) 

import cv2 as cv 
import torch
import matplotlib.pyplot as plt
import numpy as np 

# When press the space on the keyboard,the code will crop the image at the time of the video from the camera,then save the image in the folder.
def camera_capture():
    capture = cv.VideoCapture(0)

    width,height = capture.get(3),capture.get(4)

    capture.set(cv.CAP_PROP_FRAME_WIDTH,width)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT,width) 

    
    while True:
        ret,frame = capture.read() 
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame) 
        if cv.waitKey(1) == 32:
            cv.imwrite('./capture/0.jpg', frame) 
            image = cv.imread('./capture/0.jpg',cv.IMREAD_COLOR)       
            cv.imshow('capture',frame)
            cv.waitKey(0)
            cv.destroyAllWindows()

        if cv.waitKey(1)&0xFF == ord('f'):
            cv.destroyAllWindows()
            break
            
    if cv.waitKey(1)&0xFF == 27:
        capture.release()
        cv.destroyAllWindows()


img = cv.imread('./capture/0.jpg',cv.IMREAD_COLOR)


if __name__ == '__main__':
    camera_capture()
