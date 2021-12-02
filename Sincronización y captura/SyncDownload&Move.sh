#!/bin/bash

for i in {1..60};
do	
	
	parallel -j7 curl -s http://192.168.1.{}:8888/take_photo < ModuleNumbers.txt
	#wget -i DownloadLinks.txt
	aria2c -i DownloadLinks.txt -j7
	curl -s http://192.168.1.184:8888/get?input1=$1
	echo 'moviendose'
	sleep 3
    	curl -s http://192.168.1.184:8888/get?input1=0
    	echo 'se detuvo'
    	sleep 6
done

#mkdir home/pablo/datasets/$2/images/
#mv  *.jpg /home/pablo/datasets/$2/images/

#docker run -ti --rm -v /home/pablo/datasets:/datasets opendronemap/odm --project-path /datasets project
