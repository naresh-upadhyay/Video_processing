#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:38:45 2020

@author: king
"""

import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, exposure
import cv2

#image = data.astronaut()
image = cv2.imread("hog_car_logos.jpg")
fd, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1",
                    visualize=True, multichannel=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Input image')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 255))

ax2.axis('off')
#cv2.imwrite("carlogo.jpg",hog_image_rescaled)
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()



"""
import numpy as np
from skimage import exposure
from skimage import feature
import cv2
logo = cv2.imread("image1.jpg")
(H, hogImage) = feature.hog(logo, orientations=9, pixels_per_cell=(8, 8),
	cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1-sqrt",
	visualize=True)
hogImage = exposure.rescale_intensity(hogImage, out_range=(0, 255))
hogImage = hogImage.astype("uint8")
 
cv2.imshow("HOG Image", hogImage)
"""