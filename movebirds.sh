#!/bin/bash
MyDate="`date +'%d%m%Y-%H%M'`"
MyFolder="/mnt/mycloud/Birdbox/$MyDate"
MyFolderp="/mnt/mycloud/Birdbox/Pictures/$MyDate"
MyFolderv="/mnt/mycloud/Birdbox/Video/$MyDate"
MyFile="/home/pi/Webcam/copylog/Copylog"
MyInput="/mnt/motionvideos/"
MYFilecount=0
MyFilecount=$(ls 2>/dev/null -Ub1 -- $MyInput* | wc -l)
echo $MyDate >> $MyFile
echo $MyFilecount files to move >>$MyFile
if [ "$MyFilecount" -gt "0" ]; then
	sudo mount -a
	cd &MyInput &> /dev/null
	MYRV=$?
	if [ $MYRV==0 ]; then
		echo Directory found rv=$MYRV >> $MyFile
		sudo mkdir $MyFolderv
		sudo mkdir $MyFolderp
		sudo cp $MyInput*.avi $MyFolderv #&> /dev/null
		CPRV=$?
		if [ $CPRV==0 ]; then
			echo copy .avi ok rv=$CPRV,$(ls 2>/dev/null -Ub1 -- $MyFolderv/*.avi | wc -l) files copied >> $MyFile
			sudo rm $MyInput*.avi
		else
			echo copy .avi failed $CPRV >> $MyFile
		fi
		sudo cp $MyInput*.jpg $MyFolderp #&> /dev/null
		CPRV=$?
		if [ $CPRV==0 ]; then
			echo copy .jpg ok rv=$CPRV,$(ls 2>/dev/null -Ub1 -- $MyFolderp/*.jpg | wc -l) files copied >> $MyFile
			sudo rm $MyInput*.jpg
		else
			echo copy .jpg failed rv=$CPRV >> $MyFile
		fi
		echo You have $(ls 2>/dev/null -Ub1 -- $MyFolderp* | wc -l) new birdbox pictures and $(ls 2>/dev/null -Ub1 -- $MyFolderv* | wc -l) new birdbox videos | mail -s "Birdbox News" rik.pettman@gmail.com
	else
		echo directory not found $MYRV >> $MyFile
	fi
fi
echo ---------------- >> $MyFile




