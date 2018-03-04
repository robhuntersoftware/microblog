#!/usr/bin/env bash

cd ~/Personal/github/microblog
export FLASK_APP=microblog.py
source venv/bin/activate
flask run

