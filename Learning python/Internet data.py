import urllib2

def main():
    # open a connection to a URL using urllib2
    webUrl = urllib2.urlopen("http://tut.by")

    # get the result code and print it
    print "result code: " + str(webUrl.getcode())

    # read the data from URL
    data = webUrl.read()
    print data

if __name__ == '__main__':
    main()