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

nn = open('o1_scale_int.ppm','w')

nn.write(header)

q = [0]*nsize[0]*nsize[1]

for i in range(nsize[1]):
    for j in range(nsize[0]):
        x = int(j / xscale)
        y = int(i / yscale)
        
        xd = (j/xscale)-x
        yd = (i/yscale)-y        
        
        ind = y*size[0]+x
        a = pixels[ind]
        b = pixels[(ind+1)%len(pixels)]
        c = pixels[(ind+size[0])%len(pixels)]
        d = pixels[(ind+size[0]+1)%len(pixels)]

        r = int(a[0]*(1-xd)*(1-yd) + b[0]*xd*(1-yd) + c[0]*(1-xd)*yd + d[0]*xd*yd)
        g = int(a[1]*(1-xd)*(1-yd) + b[1]*xd*(1-yd) + c[1]*(1-xd)*yd + d[1]*xd*yd)
        b = int(a[2]*(1-xd)*(1-yd) + b[2]*xd*(1-yd) + c[2]*(1-xd)*yd + d[2]*xd*yd)
        
        
        q[(i*nsize[0])+j] = [r,g,b]
        
for p in q:
    nn.write("{0}\n{1}\n{2}\n".format(p[0],p[1],p[2]))
        
nn.close