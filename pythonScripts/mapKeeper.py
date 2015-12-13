#!/usr/bin/env python
__metaclass__ = type

from pprint import pprint

class mapKeeper:
    def __init__(self, mapFile, mapNotFile):
        self.mapFile = mapFile
        self.mapNotFile = mapNotFile
        self.map = {}
        with open(mapFile) as searchMap:
            entries = searchMap.read().rstrip('>>>>\n').split('>>>>\n')
            if entries != ['']:
                for entry in entries:
                    itemGroup = entry.split('\n')
                    self.map[itemGroup[0].strip()] = itemGroup[1].strip()
        self.mapNot = {}
        with open(mapNotFile) as searchMapNot:
            entries = searchMapNot.read().rstrip('>>>>\n').split('>>>>\n')
            if entries != ['']:
                for entry in entries:
                    itemGroup = entry.rstrip('\n').split('\n')
                    itemGroup = [x.strip() for x in itemGroup]
                    self.mapNot[itemGroup[0]] = itemGroup[1:]

    def search(self, search):
        try:
            return self.map[search]
        except KeyError:
            return ""

    def searchNot(self, search):
        try:
            return self.mapNot[search]
        except KeyError:
            return []

    def add(self, line):
        print "Add: ", line
        search, url = line.split(' ')
        self.map[search] = url

    def delete(self, search):
        print "Delete: ", search
        try:
            self.mapNot.setdefault(search, []).append(self.map[search])
            del self.map[search]
        except KeyError:
            print "No entry"
            pass

    def addNot(self, line):
        search, url = line.split(' ')
        print "Add not: ", search, "->", url
        self.mapNot.setdefault(search, []).append(url)
    

    def save(self):
        with open(self.mapFile, 'w') as searchMap:
            for search, url in self.map.iteritems():
                searchMap.write(search+'\n')
                searchMap.write("    "+url+'\n')
                searchMap.write(">>>>\n")
        with open(self.mapNotFile, 'w') as searchMapNot:
            for search, urls in self.mapNot.iteritems():
                searchMapNot.write(search+'\n')
                for url in urls:
                    searchMapNot.write("    "+url+'\n')
                searchMapNot.write(">>>>\n")
