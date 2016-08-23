# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:42:22 2016

@author: caramelkoala
"""

import cv2
import numpy as np

def hide(image):
    #load image and get dimensions
    img = cv2.imread(image)
    shape = img.shape
    
    #generate new blank images with the same dimesnions
    img1 = np.zeros((shape[0],shape[1],shape[2]), np.uint8)
    img2 = np.zeros((shape[0],shape[1],shape[2]), np.uint8)
    
    for i in xrange(shape[0]):
        for j in xrange(shape[1]):
            for k in range(shape[2]):
                n0 = img[i,j][k]
                n1 = (int)(np.random.random()*255)
                n2 = (n0-n1)%255
                img1[i,j][k] = n1
                img2[i,j][k] = n2
    
    cv2.imwrite("cript1.ppm",img1)
    cv2.imwrite("cript2.ppm",img2)
    
def unhide(image1,image2):
    #load images
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    shape = img1.shape
    
    #generate new blank image with the same dimesnions
    img = np.zeros((shape[0],shape[1],shape[2]), np.uint8)
    
    for i in xrange(shape[0]):
        for j in xrange(shape[1]):
            for k in range(shape[2]):
                img[i,j][k] = (img1[i,j][k]+img2[i,j][k])%255
                
    cv2.imwrite("decript.ppm",img)
    