# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:21:42 2016

@author: caramelkoala
"""

import numpy as np
import cv2

img = cv2.imread('original.ppm',1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()