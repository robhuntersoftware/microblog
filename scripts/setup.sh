#!/usr/bin/env bash

cd ~/Personal/github/microblog
source venv/bin/activate

pip install wheel
pip install flask
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-migrate
