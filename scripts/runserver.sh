#!/usr/bin/env bash

cd ~/Personal/github/microblog
export FLASK_APP=microblog.py
export FLASK_DEBUG=1
source venv/bin/activate
flask run

