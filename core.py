from __future__ import unicode_literals
import youtube_dl
from feedgen.feed import FeedGenerator
import os
import sys
import argparse
import ydl
import interface

#TODO:
# offer download video option
# create good README.md
# .gitignore
# LICENSE

parser = argparse.ArgumentParser()
parser.add_argument("-i","--interface", help="Launch GUI (beta)",action="store_true")
parser.add_argument("-s","--simulate", help="Do not download videos, just do as if",action="store_true")
parser.add_argument("-q","--quiet", help="Very quiet option for youtube-dl",action="store_true")
parser.add_argument("-f","--feed", help="Create Podcast feed",action="store_true")
parser.add_argument("-video", help="Download videos instead of creating audio",action="store_true")
parser.add_argument("-d","--dir", help="Define download directory for files, default value:'~/Vidéos'", default="~/Vidéos")
parser.add_argument("-url", help="Define base url for podcasts, default value:'http://podcasts.lutix.org'", default="http://podcasts.lutix.org")
parser.add_argument("-yturl","--youtube_url", help="Define youtube url to fetch", default ="https://www.youtube.com/watch?v=xJO5GstqTSY&list=PLxzM9a5lhAumFRpcigmGY1QLDYxb4-P2B")
args = parser.parse_args()



if __name__ == "__main__":
    if args.interface:
        ydlo = ydl.ydl_object(args)
        ydlo.print_infos()
        ydlo.process_args()
    else:
        print('Waiting for interface to be loaded...')
