#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import time
import picamera

cwd = os.path.dirname(os.path.abspath(__file__))
with picamera.PiCamera(resolution=(1280, 720)) as camera:
    time.sleep(2)
    camera.start_preview()
    camera.exposure_mode = "night"
    for filename in camera.capture_continuous(cwd+'/gallery/img{counter:04d}.jpg'):
        time.sleep(5)
