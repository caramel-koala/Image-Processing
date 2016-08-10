# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:30:27 2016

@author: caramelkoala
"""

import import_vid as iv
import export_vid as ev

vid = iv.import_vid('video1.mp4')

back = vid[0]

thresh = 20

sub = []

for frame in vid:
    temp = []
    for i in range(len(frame)):
        rtemp = []
        for j in range(len(frame[i])):
            diff = abs((back[i][j][0]+back[i][j][1]+back[i][j][2])-(frame[i][j][0]+frame[i][j][1]+frame[i][j][2]))
            if diff > thresh:
                rtemp.append(frame[i][j])
            else:
                rtemp.append([0,0,0])
        temp.append(rtemp)
    sub.append(temp)

ev.export_vid(sub,'back_sub')