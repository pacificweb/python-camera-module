#!/bin/bash


raspistill -o %04d.jpg -n -t 21600000 -w 800 -h 600 -tl 3000

	#filename=$(date -u +"%Y%m%d%H%M%S").jpg
	#echo "Shooting $filename"
	#raspistill -o ./$filename -n -w 800 -h 600 -tl 15000
	#raspistill -o ./$filename -n -tl 15000
	#echo "Uploading $filename..."
	#drive-linux-rpi upload -f ./$filename -p 0B-jGOOGLE_KEY
	#echo "Done"
