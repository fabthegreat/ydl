# YDL: Youtube Downloader

Ydl is a simple python program that downloads youtube videos, converts them into
audio file and creates an xml file to listen to them as a podcast. 

Another project, far more advanced can be found there:
https://github.com/MrS0m30n3/youtube-dl-gui. But this one cannot create feed
files to listen to audio files as podcast.

## Getting Started

* Run install.sh under Debian based distribution.
* Run runGUI.sh , or python core/core.py -i from virtual environment. 
* Run python core/core.py -h from terminal from virtual environment for more CLI options.

### Prerequisites

Please check requirements.txt.

### Installing

* Install a virtual environment:
virtualenv --python=/usr/bin/python3 venv

* Activate virtual environment:
source venv/bin/activate

* Install requirements:
pip install -r requirements.txt

## Authors

* **fabthegreat** - *Initial work* - fabthegreat@lutix.org

## License

This project is not yet licensed. 

## Acknowledgments

* youtube-dl library.

