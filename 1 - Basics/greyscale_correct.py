# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:08:04 2016

@author: caramelkoala
"""

import import_img  as ii

[size,mx,pixels] = ii.import_img('original.ppm')
    
header = "P2\n{0} {1}\n{2}\n".format(size[0],size[1],mx)

avg = open('o1_gc_correct.pgm','w')

avg.write(header)

for i in pixels:
    avg.write("%d\n"%((0.21*i[0])+(0.72*i[1])+(0.07*i[2])))
    
avg.close