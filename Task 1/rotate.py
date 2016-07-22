# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:43:34 2016

@author: caramelkoala
"""

import import_img  as ii

import math

[size,mx,pixels] = ii.import_img('original.ppm')

c       = [int(size[0]/2),int(size[1]/2)]
cp      = c[1]*size[0]+c[0]

angle   = 60
rad     = (angle/float(180))*math.pi

nsize   = [int(math.ceil(abs(size[0]*math.cos(rad)+size[1]*math.sin(rad)))),int(math.ceil(abs(size[1]*math.cos(rad)+size[0]*math.sin(rad))))]

q       = [[0,0,0]]*(nsize[0]*nsize[1])

for i in range(size[1]):
    for j in range(size[0]):
        x2 = int(math.cos(rad)*(j-c[0]) - math.sin(rad)*(i-c[1])) + c[0]-1
        y2 = int(math.sin(rad)*(j-c[0]) + math.cos(rad)*(i-c[1])) + c[1]-1
        q[y2*nsize[0]+x2] = pixels[i*size[0]+j]
        
        
header = "P3\n{0} {1}\n{2}\n".format(nsize[0],nsize[1],mx)

rot = open('o1_rotate.ppm','w')

rot.write(header)

for p in q:
    rot.write("{0}\n{1}\n{2}\n".format(p[0],p[1],p[2]))
        
rot.close