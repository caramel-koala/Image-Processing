# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:18:58 2016

@author: caramelkoala
"""

import numpy as np
import cv2
 
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
img = cv2.imread('test3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imwrite('vj.jpg',img)