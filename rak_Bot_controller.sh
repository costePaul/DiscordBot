#!/bin/bash
botName="RaKMenu"
pidFileName="pidRAK.txt"
lastOutputFileName="lastOutputRAK.txt"

start() {
	if [ -f ./$botName/$pidFileName ]
    then
        echo
        echo "Already started. PID: [$( cat ./$botName/$pidFileName )]"
    else
        source ./env/bin/activate
		./env/bin/python3 ./$botName/main.py 2>> ./$botName/$lastOutputFileName &
		echo $! > ./$botName/$pidFileName
        fi
}

status() {
	echo
    echo "==== Status"
    if [ -f ./$botName/$pidFileName ]
    then
        echo
        echo "Pid file: $( cat ./$botName/$pidFileName ) [./$botName/$pidFileName]"
        echo
        ps -ef | grep -v grep | grep $( cat ./$botName/$pidFileName )
    else
        echo
        echo "No Pid file"
    fi
}

stop() {
	kill $(< ./$botName/$pidFileName)
	rm ./$botName/$pidFileName
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
