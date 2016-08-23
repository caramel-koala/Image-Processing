# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:21:42 2016

@author: caramelkoala
"""

import cv2
import bitarray as ba

def encode(image,msg):
    #get image
    img = cv2.imread(image)
    shape = img.shape
    
    #get text and convert to bitarray
    msg     = msg + "#00#" #add end of string test
    bitmsg  = ba.bitarray()
    bitmsg.fromstring(msg)
    
    for i in xrange(0,len(bitmsg)/3+1):
        if i*3 < len(bitmsg):
            img[i/shape[1],i%shape[1]][0] = img[i/shape[1],i%shape[1]][0]+bitmsg[i*3]
        else:
            break
        if i*3+1 < len(bitmsg):
            img[i/shape[1],i%shape[1]][1] = img[i/shape[1],i%shape[1]][1]+bitmsg[i*3+1]
        else:
            break
        if i*3+2 < len(bitmsg):
            img[i/shape[1],i%shape[1]][2] = img[i/shape[1],i%shape[1]][2]+bitmsg[i*3+2]
            
    cv2.imwrite("msgimg.ppm",img)
    
def decode(msgimg,img):
    #import images
    img1 = cv2.imread(msgimg)
    img2 = cv2.imread(img)
    
    #get end of message key
    key = ba.bitarray()
    key.fromstring("#00#")
    
    #start message bit array
    msg = ba.bitarray()
    
    shape = img1.shape
    
    for i in range(shape[0]):
        for j in range(shape[1]):
            msg.append(img1[i,j][0] - img2[i,j][0])
            if contains(key,msg):
               return ba.bitarray(msg).tostring()[:-4]
            msg.append(img1[i,j][1] - img2[i,j][1])
            if contains(key,msg):
               return ba.bitarray(msg).tostring()[:-4]
            msg.append(img1[i,j][2] - img2[i,j][2])
            if contains(key,msg):
               return ba.bitarray(msg).tostring()[:-4]
                            
    return "No Message in these images"
                
def contains(small, big):
    if len(small) > len(big):
        return False
    for i in xrange(len(big)-len(small)+1):
        for j in xrange(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return True
    return False