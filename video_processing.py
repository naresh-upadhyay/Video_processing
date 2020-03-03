#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:57:38 2020

@author: king
"""
import cv2
import pytesseract
# import Os module to start the audio file
import os 
from gtts import gTTS 


#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
videocap = cv2.VideoCapture('video.mp4')

# FUNCTION TO CONVERT LIST INTO STRING
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

lst = []
# FUNCTION FOR READ TEXT FROM IMAGE USING TESSETACT
def getFrames(sec):
    videocap.set(cv2.CAP_PROP_POS_MSEC , sec*1000)
    hasFrames , images = videocap.read()
    
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg" , images)
        img = cv2.imread("image"+str(count)+".jpg")
        text = pytesseract.image_to_string(images)
        lst.append(text)
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



# CODE FOR AUDIO
mytext = ""
mytext = listToString(lst);
# Language we want to use 
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("output2.mp3") 
# Play the converted file 
os.system("start output2.mp3") 





#img = cv2.imread('textImage.png')
#text = pytesseract.image_to_string(img)
#print(text)