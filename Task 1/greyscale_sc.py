# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 09:42:25 2016

@author: caramelkoala
"""

import import_img  as ii

[size,mx,pixels] = ii.import_img('original.ppm')
    
header = "P2\n{0} {1}\n{2}\n".format(size[0],size[1],mx)

r = open('o1_gc_sc_r.pgm','w')
g = open('o1_gc_sc_g.pgm','w')
b = open('o1_gc_sc_b.pgm','w')

r.write(header)
g.write(header)
b.write(header)

for i in pixels:
    r.write("%d\n"%(i[0]))
    g.write("%d\n"%(i[1]))
    b.write("%d\n"%(i[2]))
    
r.close
g.close
b.close