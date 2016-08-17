# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:21:42 2016

@author: caramelkoala
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

#get image
bgr_img = cv2.imread('original.ppm',1)
b,g,r   = cv2.split(bgr_img)
img     = cv2.merge([r,g,b])

#get text
msg     = "Hello World"

#convert to bit array



plt.imshow(img)