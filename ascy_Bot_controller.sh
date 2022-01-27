#!/bin/bash

botName = "ASCyRespond"
filePath = "./"+$botName+"/main.py"

if [$1 == "start"]
then
	source ./env/bin/activate
	./env/bin/python3 &filePath 2>&1 ./lastOutputASCy.txt &
	echo &! > ./pidASCy.txt
fi

if [$1 == "stop"]
then
	source ./env/bin/deactivate
	kill < ./pidASCy.txt

fi


