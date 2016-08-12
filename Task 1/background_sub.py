# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:30:27 2016

@author: caramelkoala
"""

import import_vid as iv
import os

vid = iv.import_vid('video1.mp4')

back = vid[0]

thresh = 200

for h in range(len(vid)):
    header = "P3\n{0} {1}\n{2}\n".format(640,360,255)
    filename = 'Frames/back_sub{0}.ppm'.format(str(h).zfill(4))
    fwrite = open(filename,'w')
    fwrite.write(header)
    
    for i in range(len(vid[h])):
        for j in range(len(vid[h][i])):
            diff = abs((back[i][j][0]+back[i][j][1]+back[i][j][2])-(vid[h][i][j][0]+vid[h][i][j][1]+vid[h][i][j][2]))
            if diff > thresh:
                fwrite.write("{0}\n{1}\n{2}\n".format(vid[h][i][j][0],vid[h][i][j][1],vid[h][i][j][2]))
            else:
                fwrite.write("0\n0\n0\n")

os.system("ffmpeg -f image2 -i Frames/back_sub%04d.ppm back_sub.mp4")
os.system("rm Frames/back_sub*")