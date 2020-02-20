#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 04:34:05 2020

@author: king
"""

import imutils

def resizeImage(image,scale=1.5,minImagesize = (30,30)):
    yield image
    
    while(True):
        w = int(image.shape[1]/scale)
        image = imutils.resize(image, width = w)
        if image.shape[1] < minImagesize[0] or image.shape[0] < minImagesize[1] :
            break
        yield image
        
def sliding_window(image, stepincremt , windsize):
    for y in range(0,image.shape[0],stepincremt):
        for x in range(0,image.shape[1] , stepincremt):
            yield (x , y, image[y:y + windsize[1] , x:x + windsize[0]])
            
