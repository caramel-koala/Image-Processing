# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:27:11 2016

@author: caramelkoala
"""

import import_img  as ii

import math

[size,mx,pixels] = ii.import_img('original.ppm')

xscale = 2
yscale = 2
    
header = "P3\n{0} {1}\n{2}\n".format(size[0]*xscale,size[1]*yscale,mx)

nn = open('o1_scale_nn.ppm','w')

nn.write(header)

q = []

for i in range(size[0]*xscale):
    for j in range(size[1]*yscale):
        q[(i*xscale*size[0])+j] = pixels[ int(math.floor(i*yscale*size[0]*xscale + xscale*j)) ]
        
for p in q:
    nn.write("{0}\n{1}\n{2}\n".format(p[0],p[1],p[2]))
        
nn.close