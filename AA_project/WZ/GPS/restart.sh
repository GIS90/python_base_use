#!/bin/bash
ps -ef | grep gps_server.py | grep -v grep | awk '{print $2}' | xargs kill -9
echo "we wait the system release port about 40 second..."
sleep 40
/opt/Python-2.7.10/python gps_server.py


