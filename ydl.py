from __future__ import unicode_literals
import youtube_dl
from feedgen.feed import FeedGenerator
import os
import sys
import argparse
import main

#TODO:
# offer download video option
# create good README.md
# .gitignore
# LICENSE

parser = argparse.ArgumentParser()
parser.add_argument("-s","--simulate", help="Do not download videos, just do as if",action="store_true")
parser.add_argument("-q","--quiet", help="Very quiet option for youtube-dl",action="store_true")
parser.add_argument("-f","--feed", help="Create Podcast feed",action="store_true")
parser.add_argument("-video", help="Download videos instead of creating audio",action="store_true")
parser.add_argument("-d","--dir", help="Define download directory for files, default value:'~/Vidéos'", default="~/Vidéos")
parser.add_argument("-url", help="Define base url for podcasts, default value:'http://podcasts.lutix.org'", default="http://podcasts.lutix.org")
parser.add_argument("-yturl","--youtube_url", help="Define youtube url to fetch", default ="https://www.youtube.com/watch?v=xJO5GstqTSY&list=PLxzM9a5lhAumFRpcigmGY1QLDYxb4-P2B")
args = parser.parse_args()

ydlo = main.ydl_object(args)

def fetch_info(url_yt):
    print('Fetching Youtube Link informations...')
    infos = youtube_dl.YoutubeDL({'quiet':True,'ignoreerrors':True}).extract_info(url_yt, False)
    print('...Done')
    return infos

def create_feed(results):
    """
    #results keys
    _type entries id title uploader uploader_id uploader_url extractor webpage_url webpage_url_basename extractor_key
    """
    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.podcast.itunes_category('Podcasting')

    fg.title(results['title'])
    fg.description('none')
    fg.link(href=args.url,rel='self')

    for item in results['entries']:
        """
        #results['entries'] keys
        id uploader uploader_id uploader_url channel_id channel_url upload_date license creator title alt_title thumbnail description categories tags subtitles automatic_captions duration
        """
        fe = fg.add_entry()
        fe.id(item['id'])
        fe.title(item['title'])
        fe.description(item['description'])
        item_full_path = args.url +'/'+results['title']+'/'+item['title']+'.mp3'
        fe.enclosure(item_full_path,str(item['duration']),'audio/mpeg')

    fg.rss_str(pretty=True)
    # create folder of feed if it doesn't exists
    os.makedirs(args.dir+'/'+results['title'], exist_ok=True)
    fg.rss_file(args.dir+'/'+results['title']+'/podcast.xml')

    return True

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def yt_download(ydl_opts):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading Videos...')
        print('Depending on number of files, it can take a while...')
        results = ydl.extract_info(args.youtube_url, not args.simulate)
        print('Done')

def create_opts(infos,type):
    if type=='audio':
        ydl_opts = {
            'quiet':args.quiet,
            'format': 'bestaudio/best',
            'ignoreerrors': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [my_hook],
        }
    elif type=='video':
        ydl_opts= {}


    # if youtube url  is a list, then download archive 
    print('Fetching Url properties...')
    if 'entries' in infos:
        ydl_opts['download_archive']= args.dir+'/archive.txt'
        ydl_opts['outtmpl']= args.dir+'/%(playlist_title)s/%(title)s.%(ext)s'
    else:
        ydl_opts['download_archive']= args.dir+'/archive.txt'
        ydl_opts['outtmpl']= args.dir+'/%(title)s.%(ext)s'
    print('Done')

    return ydl_opts

if __name__ == "__main__":
    print('Downloads folder name: {}'.format(args.dir))
    infos = ydlo.infos

    # if youtube url linked to a list
    if 'entries' in infos:
        print('')
        print('List of episodes online:')
        for k,i in enumerate(infos['entries']):
            print('Episode {}: {}, Durée:{}'.format(k+1,i['title'],i['duration']))

        if args.feed:
            print('')
            print('Feed creation...{}'.format("Done" if create_feed(infos) else "Error"))
        else:
            print('')
            print('Warning: no podcast feed has been created, please add --feed argument.')
    else:
        if args.feed:
            print('')
            print('In spite of --feed argument, as you specified contradictory options, no feed can be created!')

    if args.simulate:
        print('Downloads...Not requested!')
    else:
        yt_download(create_opts(infos, type='audio' if not args.video else 'video'))



