# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 09:42:42 2016

@author: caramelkoala
"""

def import_vid(vid):
    import subprocess as sp
    import numpy
    
    FFMPEG_BIN = "ffmpeg" # on Linux ans Mac OS

    command = [ FFMPEG_BIN,
                '-i', vid,
                '-f', 'image2pipe',
                '-pix_fmt', 'rgb24',
                '-vcodec', 'rawvideo', '-']
    pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)
    
    video = []
    
    while True:
        raw_image = pipe.stdout.read(640*360*3)
        if not raw_image: break
        # transform the byte read into a numpy array
        image =  numpy.fromstring(raw_image, dtype='uint8')
        image = image.reshape((640,360,3))
        # throw away the data in the pipe's buffer.
        pipe.stdout.flush()
        video.append(image)
        
        
    return video