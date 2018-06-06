#!/bin/bash

if [ ! -f session ]; then
        /tmp/www/html/login.cgi
        exit 0
fi

. session
timestamp=`date +"%s"`
diff=`expr $timestamp - $SESSION_TIMESTAMP`
if [ $diff -gt 10 ]; then
    /tmp/www/html/logout.cgi
    exit 0
fi
echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Environment Variables</title>'
echo '</head>'
echo '<body>'
echo 'Environment Variables:'
echo '<pre>'
echo 'SESSION_RM_ADDR = '$SESSION_RM_ADDR
echo 'SESSION_TIMESTAMP = '$SESSION_TIMESTAMP
echo 'timestamp = '$timestamp
echo 'diff = '$diff
echo 'SESSION_RM_ADDR='$SESSION_RM_ADDR > session
echo 'SESSION_TIMESTAMP='$timestamp >> session
echo '</pre>'

echo '</body>'
echo '</html>'

exit 0
