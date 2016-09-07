# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:42:24 2016

@author: caramelkoala
"""

#import csv
import numpy as np
import cv2
import func
for i in xrange(3,4):
    img = cv2.imread('Sheets/MCQ_600dpi_2016-{0}.png'.format(str(i).zfill(2)))#,cv2.CV_LOAD_IMAGE_GRAYSCALE)
###############################################################################
    #rotate to correct orientation
    sq = func.find_squares(img)
    r = 4 #width to height ratio
    mark = [(0,0),(0,0)]
    for s in sq:
        sw  = func.dist(s[0],s[1])
        sh  = func.dist(s[1],s[2])
        if (func.nearly_equal(sh/sw,r)) or (func.nearly_equal(sw/sh,r)):
#            cv2.rectangle(img,tuple(s[0]),tuple(s[2]),(255,0,0),2)
            mark = s
            break
    d,w,h = img.shape[::-1]
    top = (0,0)
    bot = (w,h)
    if func.dist(mark[0],top) > func.dist(mark[0],bot):
        M = cv2.getRotationMatrix2D((w/2,h/2),180,1)
        img = cv2.warpAffine(img,M,(w,h))
###############################################################################    
    #find corners
    template = cv2.imread('marker.png')
    td, tw, th = template.shape[::-1]

    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    tl = (w/2,h/2)  #top left
    tr = (w/2,h)    #top right
    for pt in zip(*loc[::-1]):
#        cv2.rectangle(img, pt, (pt[0] + tw, pt[1] + th), (0,0,255), 2)
        if (pt[0]<tl[0]) and (pt[1]<tl[1]):
            tl = pt
            continue
        if (pt[0]>tr[0]) and (pt[1]<tr[1]):
            tr = pt
#    cv2.rectangle(img, tl, (tl[0] + tw, tl[1] + th), (0,255,0), 2)
#    cv2.rectangle(img, tr, (tr[0] + tw, tr[1] + th), (0,255,255), 2)
###############################################################################   
# grey and threshold image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(~img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,15,-2)
###############################################################################
# fine rotation for alignment    
    ttr = (tr[0],tl[1])     #true top right
    a = func.dist(ttr,tr)
    b = func.dist(tl,ttr)
    theta = ((np.arctan(a/b))/np.pi)*180
    M = cv2.getRotationMatrix2D((w/2,h/2),theta,1)
    img = cv2.warpAffine(img,M,(w,h))
###############################################################################
# scale image to perfect width and height
    if(b != 1061):
        scale = 1060/b
        img = cv2.resize(img,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
    else:
        img = img
###############################################################################
#find answer blocks
    ansblock = [[412,727], [46, 265, 483, 710, 924, 1147]]
    bw  = 233
    bh  = 225
    for x in ansblock[0]:
        for y in ansblock[1]:
            crop_img = img[tl[1]+y:tl[1] + y + bh,tl[0]+x:tl[0] + x + bw]
            horizontalsize = 180;
            horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize,2))
            er = cv2.erode(crop_img,horizontalStructure,iterations = 1)
            di = cv2.dilate(er,horizontalStructure,iterations = 1)
            cv2.imwrite("answer{0}{1}.png".format(x,y),di)
            
        
###############################################################################
# write image
    cv2.imwrite('Score/score{0}.jpg'.format(str(i).zfill(2)),img)
