#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:57:38 2020

@author: king
"""

import cv2
import pytesseract
#pytesseract.pytesseract.pytesseract_cmd = r'/home/king/.cache/pip/wheels/c2/60/55/ec507bce8e8ccb516954accf661ee60c8b34198fafdfb81872'
videocap = cv2.VideoCapture('video.mp4')
def getFrames(sec):
    videocap.set(cv2.CAP_PROP_POS_MSEC , sec*1000)
    hasFrames , images = videocap.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg" , images)
        img = cv2.imread("image"+str(count)+".jpg")
        text = pytesseract.image_to_string(img)
        print(text,end = '\n')
    return hasFrames

sec = 0
count = 1
framesPerSec = 2
sucess = getFrames(sec)
while sucess:
    count = count +1
    sec = sec + framesPerSec
    sec = round(sec,2)
    sucess = getFrames(sec)




#img = cv2.imread('news.png')
#text = pytesseract.image_to_string(img)
#print(text)