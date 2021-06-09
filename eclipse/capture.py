#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import time
import datetime as dt
import picamera

cwd = os.path.dirname(os.path.abspath(__file__))
with picamera.PiCamera(resolution=(1280, 720)) as camera:

    camera.awb_mode = 'sunlight'
    camera.annotate_background = picamera.Color('black')
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(2)
    for filename in camera.capture_continuous(cwd+'/gallery/img{counter:04d}.jpg'):
        time.sleep(5)
