#!/bin/bash
botName="ASCyRespond"
pidFileName="pidASCy.txt"
lastOutputFileName="lastOutputASCy.txt"

start() {
	if [ -f ./$botName/$pidASCy ]
    then
        echo
        echo "Already started. PID: [$( cat ./$botName/$pidASCy )]"
    else
        source ./env/bin/activate
		./env/bin/python3 ./$botName/main.py 2>> ./$botName/$lastOutputFileName &
		echo $! > ./$botName/$pidASCy
        fi
}

status() {
	echo
    echo "==== Status"
    if [ -f ./$botName/$pidASCy ]
    then
        echo
        echo "Pid file: $( cat ./$botName/$pidASCy ) [./$botName/$pidASCy]"
        echo
        ps -ef | grep -v grep | grep $( cat ./$botName/$pidASCy )
    else
        echo
        echo "No Pid file"
    fi
}

stop() {
	kill $(< ./$botName/$pidASCy)
	rm ./$botName/$pidASCy
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
