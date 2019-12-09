# YDL: Youtube Downloader

Ydl is a simple python program that downloads youtube videos, converts them into
audio file and creates an xml file to listen to them as a podcast. 

## Getting Started

usage: ydl.py [-h] [-s] [-q] [-f] [-video] [-d DIR] [-url URL]
              [-yturl YOUTUBE_URL]

optional arguments:
  -h, --help            show this help message and exit
  -s, --simulate        Do not download videos, just do as if
  -q, --quiet           Very quiet option for youtube-dl
  -f, --feed            Create Podcast feed
  -video                Download videos instead of creating audio
  -d DIR, --dir DIR     Define download directory for files, default
                        value:'~/Vidéos'
  -url URL              Define base url for podcasts, default
                        value:'http://podcasts.lutix.org'
  -yturl YOUTUBE_URL, --youtube_url YOUTUBE_URL
                        Define youtube url to fetch


### Prerequisites

Please check requirements.txt.

### Installing

Either use binary ydl in dist folder (under Linux OS only) or run python3 over ydl.py.

## Authors

* **fabthegreat** - *Initial work* - fabthegreat@lutix.org

## License

This project is not yet licensed. 

## Acknowledgments

* youtube-dl library.

