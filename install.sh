#!/bin/bash

## Save current virtual environment
## activate current venv
#source ./venv/bin/activate

## pip freeze requirements
#pip freeze > requirements.txt

## deactivate current venv
#source ./venv/bin/deactivate

# Clone from repo
git clone http://github.com/fabthegreat/ydl

# Enter in the newly created dir
cd ydl

# Create new venv 
virtualenv --python=/usr/bin/python3 venv

#activate new venv
source venv/bin/activate

# pip install
pip install -r requirements.txt

# Optional
sudo apt-get install ffmpeg xterm
