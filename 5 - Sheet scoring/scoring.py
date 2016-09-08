# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:42:24 2016

@author: caramelkoala
"""

import csv
import numpy as np
import cv2
import func
###############################################################################
for i in xrange(1,22):
    img = cv2.imread('Sheets/MCQ_600dpi_2016-{0}.png'.format(str(i).zfill(2)))
###############################################################################
    #rotate to correct orientation
    sq = func.find_squares(img)
    r = 4 #width to height ratio
    mark = [(0,0),(0,0)]
    for s in sq:
        sw  = func.dist(s[0],s[1])
        sh  = func.dist(s[1],s[2])
        if (func.nearly_equal(sh/sw,r)) or (func.nearly_equal(sw/sh,r)):
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
        if (pt[0]<tl[0]) and (pt[1]<tl[1]):
            tl = pt
            continue
        if (pt[0]>tr[0]) and (pt[1]<tr[1]):
            tr = pt
    if tl == (w/2,h/2) or tr == (w/2,h):
        print "Invalid Paper #{0}".format(i)
        continue
###############################################################################   
# grey and threshold image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(~img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,-2)
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
# get student number and task number
    roi = img[tl[1]+214:tl[1]+1197,tl[0]+71:tl[0]+340]
    iden = "{0} ".format(i)
    year = [roi[0:384,0:36],roi[0:384,36:2*36]]
    for y in year:
        yw, yh = y.shape[::-1]
        for j in xrange(10):
            start = j*38
            cell = y[start:start+38,0:yw]
            wp = cv2.countNonZero(cell)
            tp = 38*yw*(np.pi/4)
            if wp/float(tp) > 0.65:
                iden += "{0}".format(j) 
                break
    letter = roi[0:roi.shape[::-1][1],36*2:36*3+5]
    lw, lh = letter.shape[::-1]
    for j in xrange(26):
        start = j*38
        cell = letter[start:start+38,0:lw]
        wp = cv2.countNonZero(cell)
        tp = 38*yw*(np.pi/4)
        if wp/float(tp) > 0.65:
            iden += "{0}".format(chr(j+65)) 
            break
    code = [roi[0:384,37*3:37*4],roi[0:384,37*4:37*5],roi[0:384,37*5:37*6],roi[0:384,37*6:37*7]]
    for c in code:
        cw, ch = y.shape[::-1]
        for j in xrange(10):
            start = j*38
            cell = c[start:start+38,0:cw]
            wp = cv2.countNonZero(cell)
            tp = 38*yw*(np.pi/4)
            if wp/float(tp) > 0.65:
                iden += "{0}".format(j) 
                break
            
    iden+= "_"
            
    task = [roi[473:846,178:218],roi[473:846,218:258]]
    for t in task:
        tw, th = t.shape[::-1]
        for j in xrange(10):
            start = j*38
            cell = t[start:start+38,0:yw]
            wp = cv2.countNonZero(cell)
            tp = 38*yw*(np.pi/4)
            if wp/float(tp) > 0.6:
                iden += "{0}".format(j) 
                break
        
###############################################################################
#find answer blocks
    answers = np.zeros((60,5))
    ansblock = [[412,727], [46, 265, 483, 710, 924, 1147]]
    bw  = 233
    bh  = 225
    for o,x in enumerate(ansblock[0]):
        for p,y in enumerate(ansblock[1]):
            crop_img = img[tl[1]+y:tl[1] + y + bh,tl[0]+x:tl[0] + x + bw]
            horizontalsize = 100;
            horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize,2))
            er = cv2.erode(crop_img,horizontalStructure,iterations = 1)
            di = cv2.dilate(er,horizontalStructure,iterations = 1)
            ###################################################################
            # get line for reference
            line = np.nonzero(di)
            frame = (line[1][0],line[0][0])
            for l in xrange(len(line[1])):
                if line[1][l] < frame[0]:
                    frame = (line[1][l],line[0][l])
            fdim = [[46,204],[180,145,113,77,43]]
            for q,fy in enumerate(fdim[1]):
                row = crop_img[frame[1]-fy:frame[1]-fy+35,frame[0]+fdim[0][0]:frame[0]+fdim[0][1]]
                rw, rh = row.shape[::-1]
                for j in xrange(5):
                    start = j*31
                    cell = row[0:rh,start:start+31]
                    wp = cv2.countNonZero(cell)
                    tp = 31*rh*(np.pi/4)
                    if wp/float(tp) > 0.4:
                        answers[(o*6+p)*5 + q, j] = 1     
###############################################################################
# write results to csv
    with open('{0}.csv'.format(iden), 'w') as csvfile:
        fieldnames = ['Question', 'Answer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for r, row in enumerate(answers):
            output = ""
            if row[0] == 1: output += "A"
            if row[1] == 1: output += "B"
            if row[2] == 1: output += "C"
            if row[3] == 1: output += "D"
            if row[4] == 1: output += "E"
            writer.writerow({'Question': r+1, 'Answer': output})
###############################################################################
