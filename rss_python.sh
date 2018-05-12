#!/usr/bin/env bash

ps_out=`ps -ef | grep $1 | grep -v 'grep' | grep -v $0`
result=$(echo $ps_out | grep "$1")
if [ "$result" != "" ];then
    echo "Server already Running"
else
    ~/Documents/Personal/RSS_python/RSS_python/bin/python3 ~/Documents/Personal/RSS_python/rss_app.py &>/dev/null &
fi


# sleep 2
# google-chrome http://localhost:5000/
