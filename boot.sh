#!/bin/bash
export PATH=/usr/local/texlive/2020/bin/x86_64-linux:$PATH
export PATH=/opt/pandoc-crossref/bin:$PATH

# start node
cd /home/mur2/npm || exit
node ./src/index.js &
cd /home/mur2 || exit

# bash flask.sh
bash waitress_server.sh
# bash gunicorn.sh