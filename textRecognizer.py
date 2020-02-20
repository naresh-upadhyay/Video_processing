#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 10:52:18 2020

@author: king
"""

from imageExtractor import resizeImage
from imageExtractor import sliding_window
import time 
import cv2

image = cv2.imread("image4.jpg")
h = image.shape[0]
w = image.shape[1]
(windowW, windowH) = (50,50)

for newFrame in resizeImage(image , scale = 1.5):
    for (x,y,newImage) in sliding_window(newFrame, stepincremt = 30 , windsize = (windowW,windowH)):
        if newImage.shape[0] != windowH or newImage.shape[1] != windowW:
            continue
        
        #classifer will come here to work 
        
        cv2.rectangle(newFrame,(x, y), (x + windowW, y + windowH),(0,255,0),2)
        cv2.namedWindow("Window",cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Window", newFrame.shape[1],newFrame.shape[0])#(w,h)
        cv2.imshow("Window",newFrame)
        cv2.waitKey(1)
        time.sleep(0.030)
        
time.sleep(5)
cv2.destroyAllWindows()
