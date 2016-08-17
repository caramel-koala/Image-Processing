# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 12:31:51 2016

@author: caramelkoala
"""
import os

def export_vid(vid,name):
    
    for i in range(len(vid)):
        header = "P3\n{0} {1}\n{2}\n".format(640,360,255)
        filename = 'Frames/{0}{1}.ppm'.format(name,str(i).zfill(4))
        fwrite = open(filename,'w')
        fwrite.write(header)
        for rows in vid[i]:
            for p in rows:
                fwrite.write("{0}\n{1}\n{2}\n".format(p[0],p[1],p[2]))
        fwrite.close
       
    os.system("ffmpeg -f image2 -i Frames/{0}%04d.ppm {0}.mp4".format(name))
    os.system("rm Frames/{0}*".format(name))