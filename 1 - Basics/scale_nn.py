# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:27:11 2016

@author: caramelkoala
"""

import import_img  as ii

[size,mx,pixels] = ii.import_img('original.ppm')

xscale = 5.5
yscale = 5.5

nsize = [int(size[0]*xscale), int(size[1]*yscale)]
    
header = "P3\n{0} {1}\n{2}\n".format(nsize[0],nsize[1],mx)

nn = open('o1_scale_nn.ppm','w')

nn.write(header)

q = [0]*nsize[0]*nsize[1]

for i in range(nsize[1]):
    for j in range(nsize[0]):
        x = int(j / xscale)
        y = int(i / yscale)
        q[(i*nsize[0])+j] = pixels[y*size[0]+x]
        
for p in q:
    nn.write("{0}\n{1}\n{2}\n".format(p[0],p[1],p[2]))
        
nn.close