#!/usr/bin/env python
__metaclass__ = type

from xgoogle.search import GoogleSearch, SearchError
import sys
import urllib2
import urlparse
from bs4 import BeautifulSoup
import getimageinfo
import socket
import httplib

from pprint import pprint

class decanvaEngine:
    def __init__(self, mapKeeper):
        self.hdr = {'User-Agent': 'Mozilla/5.0'}
        self.mapKeeper = mapKeeper
    
    def search(self, search):
        g = GoogleSearch(search)
        g.results_per_page = 50
        g.page = 1
        searchNot = self.mapKeeper.searchNot(search.replace(' ', '_'))
        results = g.get_results()
        print "number of results: ", len(results)
        for res in results:
            url = res.url.encode("utf8")
            base_url = url
            req = urllib2.Request(url,headers=self.hdr)
            try:
                response = urllib2.urlopen(req)
                print "Processing: ", url
            except (UnicodeEncodeError, urllib2.HTTPError, urllib2.URLError, socket.error, httplib.BadStatusLine), e:
                print url+": ", e
                continue
            page = BeautifulSoup(response, "lxml")
            images = page.select('img[alt]')
            for image in images:
                if search in image.get('alt').lower():
                    imageURL = image.get('src')
                    imageURL = urlparse.urljoin(base_url, imageURL)
                    if imageURL in searchNot:
                        print "Image is in searchNot: ", imageURL
                        continue
                    try:
                        imgdata = urllib2.urlopen(imageURL)
                    except urllib2.HTTPError, e:
                            print "Error: "+imageURL+":", e.code
                            self.mapKeeper.addNot(search.replace(' ', '_')+" "+imageURL)
                            continue
                    except urllib2.URLError, e:
                            print "Error: "+imageURL+":", e.args
                            self.mapKeeper.addNot(search.replace(' ', '_')+" "+imageURL)
                            continue
                    image_type,width,height = getimageinfo.getImageInfo(imgdata)
                    if image_type == ' ' or (width < 200 and height < 200):
                        print "Image Invalid: ", imageURL
                        self.mapKeeper.addNot(search.replace(' ', '_')+" "+imageURL)
                        continue
                    print "image type:", image_type, "width:", width, "height:", height
                    return imageURL
        return ""
