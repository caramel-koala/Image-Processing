# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:42:24 2016

@author: caramelkoala
"""

#import csv
import numpy as np
import cv2
###############################################################################
def find_squares(img):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    squares = []
    for gray in cv2.split(img):
        for thrs in xrange(0, 255, 26):
            if thrs == 0:
                bin = cv2.Canny(gray, 0, 50, apertureSize=5)
                bin = cv2.dilate(bin, None)
            else:
                retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
            contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                cnt_len = cv2.arcLength(cnt, True)
                cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
                if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                    if max_cos < 0.1:
                        squares.append(cnt)
    return squares
###############################################################################
def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def nearly_equal(a,b,sig_fig=1):
    return ( a==b or 
             int(a*10**sig_fig) == int(b*10**sig_fig)
           )
###############################################################################           
def dist(x,y):
    return np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2);
###############################################################################
for i in xrange(1,22):
    img = cv2.imread('Sheets/MCQ_600dpi_2016-{0}.png'.format(str(i).zfill(2)),cv2.CV_LOAD_IMAGE_GRAYSCALE)
    #sq = find_squares(img)
    #r = 1.33 #width to height ratio
    #for s in sq:
    #    sw  = dist(s[0],s[1])
    #    sh  = dist(s[1],s[2])
    #    if (nearly_equal(sh/sw,r)) or (nearly_equal(sw/sh,r)):
    #        cv2.rectangle(img,tuple(s[0]),tuple(s[2]),(255,0,0),2)
    #        break

    template = cv2.imread('marker.png',0)
    w, h = template.shape[::-1] 
    
#    thi = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,11,2)
#             
#    tht = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,11,2)
    
    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
    cv2.imwrite('Score/score{0}.jpg'.format(str(i).zfill(2)),img)
    
