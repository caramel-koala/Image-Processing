# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:43:34 2016

@author: caramelkoala
"""

import import_img  as ii

import math

[size,mx,pixels] = ii.import_img('original.ppm')

c       = [int(size[0]/2),int(size[1]/2)]
angle   = 225
rad     = ((360-angle)/float(180))*math.pi

nsize   = [int(math.ceil(abs(size[0]*math.cos(rad))+abs(size[1]*math.sin(rad)))),int(math.ceil(abs(size[1]*math.cos(rad))+abs(size[0]*math.sin(rad))))]
cn      = [int(nsize[0]/2),int(nsize[1]/2)]
cdiff   = [cn[0]-c[0],cn[1]-c[1]]

q       = [[0,0,0]]*(nsize[0]*nsize[1])

for i in range(nsize[1]):
    for j in range(nsize[0]):
        x2 = int(math.cos(rad)*(j-cn[0]) - math.sin(rad)*(i-cn[1])) + cn[0]-1
        y2 = int(math.sin(rad)*(j-cn[0]) + math.cos(rad)*(i-cn[1])) + cn[1]-1
        if (x2-cdiff[0] < size[0]) and (x2-cdiff[0] >= 0) and (y2-cdiff[1] < size[1]) and (y2-cdiff[1] >= 0):
            q[i*nsize[0]+j] = pixels[(y2-cdiff[1])*size[0]+(x2-cdiff[0])]
        
header = "P3\n{0} {1}\n{2}\n".format(nsize[0],nsize[1],mx)

rot = open('o1_rotate.ppm','w')

rot.write(header)

for p in q:
    rot.write("{0}\n{1}\n{2}\n".format(p[0],p[1],p[2]))
        
rot.close