# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 09:53:15 2016

@author: caramelkoala
"""

import import_vid as iv
import export_vid as ev

vid = iv.import_vid('video1.mp4')

ev.export_vid('back_sub.mp4',vid)