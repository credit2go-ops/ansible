#!/bin/bash
SED=/bin/sed

LOGFILE="/var/log/tomcat6/catalina.out"
STARTNUM=`wc -l $LOGFILE | awk '{print $1}'`

for((i=1;i<=5;i++));
    do
        NEWNUM=`wc -l $LOGFILE | awk '{print $1}'`
        if [ "${STARTNUM}" = "${NEWNUM}" ];then
            echo "error log is not writing"
        elif [ "${STARTNUM}" = "${NEWNUM}" ];then
            echo "file is Archiving"
        else
            echo "writing"
        fi
        sleep 10
    done

NEWLINE=`wc -l $LOGFILE | awk '{print $1}'`

${SED} -n "${STARTNUM},${NEWLINE}p " $LOGFILE

