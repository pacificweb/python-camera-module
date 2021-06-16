#!/usr/bin/python3

#
# Helper script for recording until interrupt, usefull for youtube
# Auteur : Stephane Gagnon
#

import picamera
import os
import sys
import time
from datetime import datetime

class Recorder:

	# CONSTRUCTEUR
	def __init__(self):

		self.timeout = 2147483647	
		self.IsRecording = False
		
		# CAMERA
		self.camera = picamera.PiCamera()
		#self.camera.meter_mode = "average"	# Values are: average, spot, matrix, backlit
	
	# Start crecording process
	def StartRecording(self):
	
		if not self.IsRecording:
		
			timenow = datetime.now()
			self.filename = "%04d%02d%02d%02d%02d%02d.h264" % ( timenow.year, timenow.month, timenow.day, timenow.hour, timenow.minute, timenow.second )
			
			print ("Started recording", self.filename)
			
			self.camera.exposure_mode = "auto"
			#self.camera.image_effect = "none"
			#self.camera.exposure_compensation = 0
			#self.camera.ISO = 0
			#self.camera.brightness = 50
			#self.camera.contrast = 0
			self.camera.resolution = (640,480)
			self.camera.start_recording(self.filename)
			self.camera.wait_recording(self.timeout)
			print ("Recording...")
			self.IsRecording = True
			
	# Stop recording process
	def StopRecording(self):
		if self.IsRecording:
			self.camera.stop_recording()
			#self.camera.stop_preview()
		self.camera.close()
		print ("Recording terminated")

#
#
# Main
#
#
print ("Preparing camera...")	
recorder = Recorder()
time.sleep(2)
input("Camera ready, press enter to start recording. Use ctrl+c to stop recording")
try:
	#recorder.camera.start_preview()
	recorder.timeout = 10
	recorder.StartRecording()
	recorder.StopRecording()
except KeyboardInterrupt:
		recorder.StopRecording()
		sys.exit(1)