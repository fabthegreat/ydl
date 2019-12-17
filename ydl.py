from __future__ import unicode_literals
import youtube_dl
from feedgen.feed import FeedGenerator
import os
import sys

class ydl_object:
    def __init__(self,args):
        self.args = args
        self.infos = self.fetch_info()
#        print(self.args)

    def fetch_info(self):
        print('Fetching Youtube Link informations...')
        return youtube_dl.YoutubeDL({'quiet':True,'ignoreerrors':True}).extract_info(self.args.youtube_url, False)

    def create_feed(self):
        """
        replace results by info
        #results keys
        _type entries id title uploader uploader_id uploader_url extractor webpage_url webpage_url_basename extractor_key
        """
        fg = FeedGenerator()
        fg.load_extension('podcast')
        fg.podcast.itunes_category('Podcasting')

        fg.title(self.infos['title'])
        fg.description('none')
        fg.link(href=self.args.podcast_url,rel='self')

        for item in self.infos['entries']:
            """
            #infos['entries'] keys
            id uploader uploader_id uploader_url channel_id channel_url upload_date license creator title alt_title thumbnail description categories tags subtitles automatic_captions duration
            """
            fe = fg.add_entry()
            fe.id(item['id'])
            fe.title(item['title'])
            fe.description(item['description'])
            item_full_path = self.args.podcast_url +'/'+self.infos['title']+'/'+item['title']+'.mp3'
            fe.enclosure(item_full_path,str(item['duration']),'audio/mpeg')

        fg.rss_str(pretty=True)
        # create folder of feed if it doesn't exists
        os.makedirs(self.args.dir+'/'+self.infos['title'], exist_ok=True)
        fg.rss_file(self.args.dir+'/'+self.infos['title']+'/podcast.xml')

        return True

    def my_hook(self,d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    def yt_download(self,ydl_opts):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print('Downloading Videos...')
            print('Depending on number of files, it can take a while...')
            results = ydl.extract_info(self.args.youtube_url, not self.args.simulate)
            print('Done')

    def create_opts(self,type):
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
                'progress_hooks': [self.my_hook],
            }
        elif type=='video':
            ydl_opts= {}


        # if youtube url  is a list, then download archive 
        print('Fetching Url properties...')
        if 'entries' in self.infos:
            ydl_opts['download_archive']= self.args.dir+'/archive.txt'
            ydl_opts['outtmpl']= self.args.dir+'/%(playlist_title)s/%(title)s.%(ext)s'
        else:
            ydl_opts['download_archive']= self.args.dir+'/archive.txt'
            ydl_opts['outtmpl']= self.args.dir+'/%(title)s.%(ext)s'
        print('Done')

        return ydl_opts

    def print_infos(self):
        print('Downloads folder name: {}'.format(self.args.dir))
        if 'entries' in self.infos:
            print('')
            print('List of episodes online:')
            for k,i in enumerate(self.infos['entries']):
                print('Episode {}: {}, Durée:{}'.format(k+1,i['title'],i['duration']))

    def process_args(self):
        if 'entries' in self.infos:
            if self.args.feed:
                print('')
                print('Feed creation...{}'.format("Done" if self.create_feed() else "Error"))
            else:
                print('')
                print('Warning: no podcast feed has been created, please add --feed argument.')
        else:
            if self.args.feed:
                print('')
                print('In spite of --feed argument, as you specified contradictory options, no feed can be created!')

        if self.args.simulate:
            print('Downloads...Not requested!')
        else:
            self.yt_download(self.create_opts(type='audio' if not self.args.video else 'video'))




