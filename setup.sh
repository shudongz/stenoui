#!/bin/bash
#
# Script to be run once to set up flask.
# Assumed to run on Ubuntu.

install_flask() {
    virtualenv flask
    flask/bin/pip install flask &> /dev/null
    flask/bin/pip install flask-wtf &> /dev/null
    flask/bin/pip install pytz &> /dev/null
}

sudo apt-get install python-virtualenv python-tz
install_flask
