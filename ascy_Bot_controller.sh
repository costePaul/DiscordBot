#!/bin/bash

botName="ASCyRespond"

if [ $1 = "start" ]
then
	source ./env/bin/activate
	./env/bin/python3 ./$botName/main.py 2> ./$botName/lastOutputASCy.txt &
	echo $! > ./$botName/pidASCy.txt
fi

if [ $1 = "stop" ]
then
	kill $(< ./$botName/pidASCy.txt)

fi
