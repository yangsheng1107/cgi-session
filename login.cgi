#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Environment Variables</title>'
echo '</head>'
echo '<body>'
if [ ! -f session ]; then
    echo 'Welcome '$REMOTE_ADDR' !!'
    echo '<pre>'
    echo 'SESSION_RM_ADDR='$REMOTE_ADDR > session
    timestamp=`date +"%s"`
    echo 'SESSION_TIMESTAMP='$timestamp >> session
    echo '</pre>'
else
    . session
    echo 'SESSION_RM_ADDR = '$SESSION_RM_ADDR
    echo 'SESSION_TIMESTAMP = '$SESSION_TIMESTAMP
    if [ $SESSION_RM_ADDR == $REMOTE_ADDR ]; then
        echo 'You has been login!!'
        echo 'SESSION_RM_ADDR='$SESSION_RM_ADDR > session
        timestamp=`date +"%s"`
        echo 'SESSION_TIMESTAMP='$timestamp >> session
    else
        echo 'You has been login by other device!!'
    fi
        echo '<pre>'
        echo '</pre>'
fi

echo '</body>'
echo '</html>'

exit 0
