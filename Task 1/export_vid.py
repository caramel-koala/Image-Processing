# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 12:31:51 2016

@author: caramelkoala
"""

def export_vid(vid,array):
    
#    import subprocess as sp
#
#    vidstr= []
#    for image in array:
#            vidstr.append(image.tostring())
#    
#    st = ' '.join(vidstr)
#    
#    FFMPEG_BIN = "ffmpeg" # on Linux ans Mac OS    
#    
#    command = [ FFMPEG_BIN,
#        '-y', # (optional) overwrite output file if it exists
#        '-f', 'rawvideo',
#        '-vcodec','rawvideo',
#        '-s', '320x240', # size of one frame
#        '-pix_fmt', 'rgb24',
#        '-r', '24', # frames per second
#        '-i', '-', # The imput comes from a pipe
#        '-an', # Tells FFMPEG not to expect any audio
#        '-vcodec', 'mpeg',
#        vid ]
#    
#    pipe = sp.Popen( command, stdin=sp.PIPE, stderr=sp.PIPE)
#
#    pipe.stdin.write(st)
#    
#    pipe.stdin.close()
    import sys

    sys.path.append('/usr/local/lib/python2.7/site-packages')
    
    import cv2
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.cv.CV_FOURCC(*'MPG4')
    # out = cv2.VideoWriter(vid,fourcc, 20.0, (320,240))
    
    # for frame in array:
    #     out.write(frame)
    
    writer = cv2.VideoWriter('video2.mp4',fourcc, 25, (320, 240), False)
    for i in array:
        writer.write(i)
    
    # Release everything if job is finished
    #writer.release()