# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 12:47:26 2016

@author: caramelkoala
"""

def import_img(filename):
    
    o1 = open(filename)
    
    raw = o1.readlines()
    
    sizetxt = raw[2]
    maxtxt = raw[3]    
    imgtxt = raw[4:len(raw)]
    sizetxt = sizetxt.split(' ')
    
    size = map(int,sizetxt)
    mx = int(maxtxt)
    img = map(int,imgtxt)
    
    pixels = [img[3*i:3*(i+1)] for i in range(len(img)/3)]
    
    o1.close    
    
    return [size,mx,pixels]