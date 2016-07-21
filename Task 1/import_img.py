# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 12:47:26 2016

@author: caramelkoala
"""

def import_img(filename):
    
    o1 = open(filename)
    
    raw = o1.readlines()
    
    imgtxt = raw[3:len(raw)]
    sizetxt = raw[2]
    sizetxt = sizetxt.split(' ')
    
    size = map(int,sizetxt)
    img = map(int,imgtxt)
    
    pixels = [img[3*i:3*(i+1)] for i in range(len(img)/3 + 1)]
    
    return [size, pixels]