#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from os.path import expanduser
import json
import pycurl
import re
import sys
import urllib
import urllib2
import json
import itertools
import bs4


home = expanduser("~")
directory = './'

class PodcastDownloader():
    def __init__(self, paths):
        self.__init__
        self.urls=paths
    
class PodcastDownloaderPolskieRadio(PodcastDownloader):
    #def __init__(self, paths):
    #    super(PodcastDownloader, self).__init__()
    
    def process(self):
       #print("[process]")   
       for path in self.urls: 
            print '%s'  % path
            page = self.download_page(path)
            data = self.parse(page)
            file_url = data['file']
            self.download_audiofile(file_url)
            self.save_data(data)

    def download_page(self, url):
       sys.stdout.write('  downloading page ...')    
       www = HTMLPage(url)
       www.request()
       html = www.contents
       print ' done.'      
       return html



#print is just a thin wrapper that formats the inputs (space between args and newline at the end) and calls the write function of a given object. By default this object is sys.stdout but you can pass a file for example:
#print >> open('file.txt', 'w'), 'Hello', 'World', 2+3
# #
    def parse(self, html):
        #there are only 2 possible sources of url to file,
        # icon representing a Speaker and another of plus sign
        # which are separet <button> "class": "ico iSpeaker" and "class": "ico iPlus"    
        #title="posluchaj" and  title="dodaj do playlisty"    
        # they are in <div class="wrap-article"> <article> <div class="icons"> <button ..
        #example:
        #<div class="wrap-article">
        # <article>
        #   <div class="icons"><button title="posłuchaj" class="ico iSpeaker" type="button" data-media='{"id":1292167,"file":"http://static.prsa.pl/2a12a6d2-a730-4866-a7d6-b150ef7de6c8.mp3","provider":"audio","uid":"2a12a6d2-a730-4866-a7d6-b150ef7de6c8","length":3305,"autostart":true,"link":"/8/0/Artykul/1414510,Sol-cudownie-sprowadzona-z-Wegier-Sekrety-Wieliczki","title":"S%C3%B3l%20cudownie%20sprowadzona%20z%20W%C4%99gier.%20Sekrety%20Wieliczki","desc":"Legenda%20o%20pocz%C4%85tkach%20s%C5%82ynnej%20kopalni%20soli%20brzmi%20dzi%C5%9B%20nieprawdopodobnie.%20Wystarczy%20jednak%20wybra%C4%87%20si%C4%99%20z%20Dw%C3%B3jk%C4%85%20do%20%22Wieliczki%22%2C%20by%20przekona%C4%87%20si%C4%99%2C%20%C5%BCe%20to%20miejsce%20magiczne.","advert":0}'></button><button title="dodaj do playlisty" class="ico iPlus" type="button" data-media='{"id":1292167,"file":"http://static.prsa.pl/2a12a6d2-a730-4866-a7d6-b150ef7de6c8.mp3","provider":"audio","uid":"2a12a6d2-a730-4866-a7d6-b150ef7de6c8","length":3305,"autostart":false,"link":"/8/0/Artykul/1414510,Sol-cudownie-sprowadzona-z-Wegier-Sekrety-Wieliczki","title":"S%C3%B3l%20cudownie%20sprowadzona%20z%20W%C4%99gier.%20Sekrety%20Wieliczki","desc":"Legenda%20o%20pocz%C4%85tkach%20s%C5%82ynnej%20kopalni%20soli%20brzmi%20dzi%C5%9B%20nieprawdopodobnie.%20Wystarczy%20jednak%20wybra%C4%87%20si%C4%99%20z%20Dw%C3%B3jk%C4%85%20do%20%22Wieliczki%22%2C%20by%20przekona%C4%87%20si%C4%99%2C%20%C5%BCe%20to%20miejsce%20magiczne.","advert":0}'></button></div>
        #    <a title="Sól cudownie sprowadzona z Węgier. Sekrety Wieliczki" class="a-img fl" href="/8/405/Artykul/1414510,Sol-cudownie-sprowadzona-z-Wegier-Sekrety-Wieliczki"><img width="202" height="110" alt="Sól cudownie sprowadzona z Węgier. Sekrety Wieliczki" src="http://static.prsa.pl/67b034df-8278-4d71-aa76-ee39236a3d02.file?format=202x110"></a>
        #    <h3><a title="Sól cudownie sprowadzona z Węgier. Sekrety Wieliczki" href="/8/405/Artykul/1414510,Sol-cudownie-sprowadzona-z-Wegier-Sekrety-Wieliczki">              Sól cudownie sprowadzona z Węgier. Sekrety Wieliczki            </a></h3>
        #    <p>            Legenda o początkach słynnej kopalni soli brzmi dziś nieprawdopodobnie. Wystarczy jednak wybrać się z Dwójką do "Wieliczki", by przekonać się, że to miejsce magiczne.          </p>
        # </article>
        #<aside class="tags"><ul><li class="title">Tagi:</li><li><a title="Hanna Maria Giza" href="/Hanna-Maria-Giza/Tag166037">Hanna Maria Giza</a>,</li><li><a title="kultura" href="/kultura/Tag895">kultura</a>,</li><li><a title="Skandynawia" href="/Skandynawia/Tag696">Skandynawia</a>,</li><li><a title="Szwecja" href="/Szwecja/Tag119">Szwecja</a>,</li><li><a title="średniowiecze" href="/sredniowiecze/Tag170525">średniowiecze</a></li></ul></aside>
        
        sys.stdout.write('  parsing page ...')    
        #pool = BeautifulSoup(the_page)
        #results = pool.findAll('td', attrs={'class' : 'td7nl'})

        buttons = bs4.BeautifulSoup(html)('button', {"class": "ico iSpeaker"} )
        #print buttons
        #if buttons:
        #    #print buttons[1]['data-media']
        #    button_data = json.loads(buttons[0]['data-media'])
        #    id_media = button_data['id']
        #    file_url = button_data['file']
        #    provider = button_data['provider']        
        #    length = button_data['length']  
        #    title = button_data['title']  
        #    desc = button_data['desc']  
        #    uid = button_data['uid']
        #el
        link = bs4.BeautifulSoup(html)('a', {"class": "ico iSpeaker"} )
        #print link[0]
        if link:
            button_data = json.loads(link[0]['data-media'])
            #id_media = button_data['id']
            #file_url = button_data['file']
            #provider = button_data['provider']        
            #length = button_data['length']  
            #title = button_data['title']  
            #desc = button_data['desc']  
            #uid = button_data['uid']
        else:
            print "[WARNING] could not find any link to audio file on the page"       
            
        #sys.stdout.write( ' ' + str(button_data['uid']) )
        #print ' done.'        
        print ' %s' % button_data['uid']
        return button_data

    def download_audiofile(self, url):
        #sys.stdout.write('  downloading audio file: ')   
        #if(os.path.isfile(file_name)):
        #    print '[!] Plik o tej nazwie istnieje w katalogu docelowym'
        #else:

        #sys.stdout.write(' ' + str(url) + ' ...')
        
        file_name = url.split('/')[-1]
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        #print " %s ... Bytes: %s" % (file_name, file_size)
        #sys.stdout.write( ' ' + file_name + ' ... Bytes: ' + str(file_size))
        #sys.stdout.flush()
        
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
        
            file_size_dl += len(buffer)
            f.write(buffer)
            status = " %10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            #txtline = '\r' +'  downloading audio file: ' + file_name + ' ... Bytes: ' + str(file_size) + ' ' + status
            txtline = '\r' +'  downloading audio file: ... Bytes: ' + str(file_size) + ' ' + status
            sys.stdout.write(txtline)
            sys.stdout.flush()        
        f.close()
        print ''       

    
    def save_data(self, data):
        sys.stdout.write('  saving data results ...')   
        filename = data['uid'] + '.json'
        with open(filename, 'w') as fp:
            json.dump(data, fp)
        print ' done.'    
        
    def cleanup(self):
        print("[cleanup]\n")    
        
class HTMLPage:
    def __init__(self, url):
        self.contents = ''        
        self.url = url
        self.c = pycurl.Curl()
        
    def body_callback(self, buf):
        self.contents = self.contents + buf
        
    def request(self):  
        c = self.c                 
        c.setopt(c.URL, sys.argv[1])
        c.setopt(c.WRITEFUNCTION, self.body_callback)
        headers = ['Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language: pl,en-us;q=0.7,en;q=0.3','Accept-Charset: ISO-8859-2,utf-8;q=0.7,*;q=0.7','Content-Type: application/x-www-form-urlencoded']#,'Content-Length: 65']
        c.setopt(c.HEADER, 1);
        c.setopt(c.HTTPHEADER, headers)
        c.setopt(c.FOLLOWLOCATION, 1)
        c.setopt(c.USERAGENT,'Mozilla/5.0 (X11; U; Linux i686; pl; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3')
        c.setopt(c.REFERER, sys.argv[1])        
        c.setopt(c.COOKIEFILE, '')
        c.perform()
    

#
#  one url path or -f -i list of url file
# ... or given by - so pipeline then line by line

# -a -A --all or go through all links on page and download them

# -r go recursive through all links and traversing download all audio

# -v verbose, else 
# -d output dir

def main(paths):
    downloader = PodcastDownloaderPolskieRadio(paths)
    downloader.process();


def usage():
     print("usage: pr_dl [url_path [more_url_path ...]]")
     #print("usage: pr_dl [url_path [more_url_path ...]]", file=sys.stderr)     
     sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        
    if(sys.argv[1].find("http://www.polskieradio.pl")==0):
        try:
            main(sys.argv[1:])
        except KeyboardInterrupt:
            PodcastDownloaderPolskieRadio.cleanup()
            raise
    else:
        print("[WARNING] program only accepts url from National Polish Radio web page: http://www.polskieradio.pl/<subpage>/\n")
        usage()
            



# Parametry podstawowe:
#if '-y' in sys.argv or '-Y' in sys.argv:
#    SAVE_ALL = 1
#if '-f' in sys.argv or '-F' in sys.argv:
#    FORCED_SEARCH = True
        
    #    if len(sys.argv) > 1:


