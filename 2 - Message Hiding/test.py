# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 14:45:01 2016

@author: caramelkoala
"""

import Image_hiding as ih

ih.encode('original.ppm','Stuff goes here')

msg = ih.decode('msgimg.ppm','original.ppm')