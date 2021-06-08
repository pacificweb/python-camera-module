#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import picamera

with picamera.PiCamera(resolution=(1280, 720)) as camera:
    time.sleep(2)
    camera.start_preview()
    camera.exposure = "night"
    for filename in camera.capture_continuous('./gallery/img{counter:04d}.jpg'):
        time.sleep(5)
