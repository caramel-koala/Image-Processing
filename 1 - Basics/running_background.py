# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:32:28 2016

@author: caramelkoala
"""

import import_vid as iv
import os

vid = iv.import_vid('video1.mp4')

B   = vid[0]
a   = 0.9

thresh = 25

for h in xrange(len(vid)):
    header = "P3\n{0} {1}\n{2}\n".format(640,360,255)
    filename = 'Frames/run_back{0}.ppm'.format(str(h).zfill(4))
    fwrite = open(filename,'w')
    fwrite.write(header)
    
    for i in xrange(len(vid[h])):
        for j in xrange(len(vid[h][i])):
            diff = abs((0.21*B[i][j][0]+0.72*B[i][j][1]+0.07*B[i][j][2])-(0.21*vid[h][i][j][0]+0.72*vid[h][i][j][1]+0.07*vid[h][i][j][2]))
            if diff > thresh:
                fwrite.write("{0}\n{1}\n{2}\n".format(vid[h][i][j][0],vid[h][i][j][1],vid[h][i][j][2]))
            else:
                fwrite.write("0\n0\n0\n")

    B   = a*vid[h]+(1-a)*B
os.system("ffmpeg -f image2 -i Frames/run_back%04d.ppm run_back.mp4")
os.system("rm Frames/run_back*")