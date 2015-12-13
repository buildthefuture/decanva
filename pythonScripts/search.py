#!/usr/bin/env python

import sys
#for line in sys.path:
#    print line
#    print "--------------"
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from mapKeeper import mapKeeper
#from decanvaEngine import decanvaEngine
#from decanvaEngine_usingxgoogle import decanvaEngine
from decanvaEngine_usingmgoogle import decanvaEngine

search = sys.argv[1]
search = search.lower()
print "search="+search
fileDir = os.path.dirname(os.path.realpath(__file__))
myMapKeeper = mapKeeper(fileDir+"/searchMap.txt", fileDir+"/searchMapNot.txt")

if len(sys.argv) == 2:
    result = myMapKeeper.search(search)
    if result != "":
        print "From repository: ", ">>>>"+result
        sys.exit()
elif len(sys.argv) == 3:
    myMapKeeper.delete(search)

myDecanvaEngine = decanvaEngine(myMapKeeper)
result = myDecanvaEngine.search(search.replace('_', ' '))
if result != "":
    myMapKeeper.add(search+" "+result)
    myMapKeeper.save()
print "Googled: ", ">>>>"+result