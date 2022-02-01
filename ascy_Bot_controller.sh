#!/bin/bash
botName="ASCyRespond"

start() {
	if [ -f ./$botName/pidASCy.txt ]
    then
        echo
        echo "Already started. PID: [$( cat ./$botName/pidASCy.txt )]"
    else
        source ./env/bin/activate
		./env/bin/python3 ./$botName/main.py 2>> ./$botName/lastOutputASCy.txt &
		echo $! > ./$botName/pidASCy.txt
        fi
}

status() {
	echo
    echo "==== Status"
    if [ -f ./$botName/pidASCy.txt ]
    then
        echo
        echo "Pid file: $( cat ./$botName/pidASCy.txt ) [./$botName/pidASCy.txt]"
        echo
        ps -ef | grep -v grep | grep $( cat ./$botName/pidASCy.txt )
    else
        echo
        echo "No Pid file"
    fi
}

stop() {
	kill $(< ./$botName/pidASCy.txt)
	rm ./$botName/pidASCy.txt
}

case "$1" in
    'start')
            start
            ;;
    'stop')
            stop
            ;;
    'restart')
            stop ; sleep 1 ;
            start
            ;;
    'status')
            status
            ;;
    *)
            echo
            echo "Usage: $0 { start | stop | restart | status }"
            echo
            exit 1
            ;;
esac

exit 0
