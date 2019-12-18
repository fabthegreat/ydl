#!/bin/bash

## Save current virtual environment
## activate current venv
#source ./venv/bin/activate

## pip freeze requirements
#pip freeze > requirements.txt

## deactivate current venv
#source ./venv/bin/deactivate

# Export virtual environment
# Create new venv 
#virtualenv --python=/usr/bin/python<version of python> <path/to/new/virtualenv/>
# or 
python3 -m venv venv # to be tested

#activate new venv
source ./venv/bin/activate # to be tested wit python3 -m venv

# pip install
pip install -r requirements.txt
