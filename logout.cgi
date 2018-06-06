#!/bin/bash

if [ ! -f session ]; then
        /tmp/www/html/login.cgi
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
echo 'Bye Bye!!:'
echo '<pre>'
rm  session
echo '</pre>'

echo '</body>'
echo '</html>'

exit 0
