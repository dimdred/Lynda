import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

# print name of OS
print os.name

# check for item existence and type
print "Item exist: " + str(path.exists("textfile.txt"))
print "Item is a file: " + str(path.isfile("textfile.txt"))
print "Item is a directory: " + str(path.isdir("textfile.txt"))

# work with real paths
print "Item`s paths: " + str(path.realpath("textfile.txt"))
print "Item`s paths and name: " + str(path.split(path.realpath("textfile.txt")))

# get the modification time
t = time.ctime(path.getmtime("textfile.txt"))
print t
print datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))

# calculate how long ago the item was modified
td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
print "It has been " + str(td) + "The file was modified"
print "Or," + str(td.total_seconds()) + "seconds"