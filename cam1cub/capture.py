#! /usr/bin/python3	  

import os
from time import sleep
import picamera
import datetime

camera = picamera.PiCamera()
camera.resolution = (2592,1944)
camera.rotation=90
i=1
while i<=120:  
	camera.capture('/home/pi/Desktop/Image/img%02d.jpg' %i)
	sleep(3600)  
	i=i+1
