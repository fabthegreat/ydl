#!/bin/bash

## Save current virtual environment
## activate current venv
#source ./venv/bin/activate

## pip freeze requirements
#pip freeze > requirements.txt

## deactivate current venv
#source ./venv/bin/deactivate

# Optional
sudo apt-get install ffmpeg xterm virtualenv python3 python3-tk

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

# create runGUI.sh
rm runGUI.sh
touch runGUI.sh
echo "#!/bin/bash" > runGUI.sh
echo "" >> runGUI.sh
echo cd $(pwd) >> runGUI.sh
echo "./venv/bin/python3 ./core/core.py -i" >> runGUI.sh
chmod u+x runGUI.sh

