# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:04:48 2016

@author: caramelkoala
"""

import import_img  as ii

[size,mx,pixels] = ii.import_img('original.ppm')
    
header = "P2\n{0} {1}\n{2}\n".format(size[0],size[1],mx)

avg = open('o1_gc_avg.pgm','w')

avg.write(header)

for i in pixels:
    avg.write("%d\n"%((i[0]+i[1]+i[2])/3))
    
avg.close