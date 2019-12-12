from __future__ import unicode_literals
import youtube_dl
from feedgen.feed import FeedGenerator
import os
import sys

class ydl_object:
    def __init__(self,args):
        self.args = args
        self.infos = self.fetch_info()
        print(self.args)

    def fetch_info(self):
        print('Fetching Youtube Link informations...')
        return youtube_dl.YoutubeDL({'quiet':True,'ignoreerrors':True}).extract_info(self.args.youtube_url, False)

    def create_feed(self,results):
        """
        replace results by info
        #results keys
        _type entries id title uploader uploader_id uploader_url extractor webpage_url webpage_url_basename extractor_key
        """
        fg = FeedGenerator()
        fg.load_extension('podcast')
        fg.podcast.itunes_category('Podcasting')

        fg.title(results['title'])
        fg.description('none')
        fg.link(href=self.args.url,rel='self')

        for item in results['entries']:
            """
            #results['entries'] keys
            id uploader uploader_id uploader_url channel_id channel_url upload_date license creator title alt_title thumbnail description categories tags subtitles automatic_captions duration
            """
            fe = fg.add_entry()
            fe.id(item['id'])
            fe.title(item['title'])
            fe.description(item['description'])
            item_full_path = self.args.url +'/'+results['title']+'/'+item['title']+'.mp3'
            fe.enclosure(item_full_path,str(item['duration']),'audio/mpeg')

        fg.rss_str(pretty=True)
        # create folder of feed if it doesn't exists
        os.makedirs(self.args.dir+'/'+results['title'], exist_ok=True)
        fg.rss_file(self.args.dir+'/'+results['title']+'/podcast.xml')

        return True

    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    def yt_download(ydl_opts):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print('Downloading Videos...')
            print('Depending on number of files, it can take a while...')
            results = ydl.extract_info(self.args.youtube_url, not self.args.simulate)
            print('Done')

    def create_opts(infos,type):
        if type=='audio':
            ydl_opts = {
                'quiet':self.args.quiet,
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
            ydl_opts['download_archive']= self.args.dir+'/archive.txt'
            ydl_opts['outtmpl']= self.args.dir+'/%(playlist_title)s/%(title)s.%(ext)s'
        else:
            ydl_opts['download_archive']= self.args.dir+'/archive.txt'
            ydl_opts['outtmpl']= self.args.dir+'/%(title)s.%(ext)s'
        print('Done')

        return ydl_opts


