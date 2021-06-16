#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import time
import datetime as dt
import picamera

cwd = os.path.dirname(os.path.abspath(__file__))
with picamera.PiCamera(resolution=(1296, 972)) as camera:

    time.sleep(2)
    camera.exposure_mode = 'night'
    camera.annotate_background = picamera.Color('black')
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for filename in camera.capture_continuous(cwd + '/gallery/img{counter:04d}.jpg'):
        time.sleep(12)
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
