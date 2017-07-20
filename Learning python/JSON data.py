import urllib2
import json

def PrintResult(data):
    # JSON load the string data into a dictionary
    theJSON = json.loads(data)
    # access to contents of JSON like any other Python object (look into JSON file for clarification)
    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]
    # output the number of events, the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print str(count) + " events recorded"

    # place where it occurred
    for i in theJSON["features"]:
        print i["properties"]["place"]

    # the events have magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["place"] >= 4.0:
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"] # 2.1f decimal print

    # the events where at least 1 person reported something
    print "\nEvents that were felt:"
    for i in theJSON["features"]:
        feltReport = i["properties"]["felt"]
        if (feltReport != None) & (feltReport > 0):
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReport) + " times"


def main():
    # URL for getting JSON
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # open URL and read the data
    webUrl = urllib2.urlopen(urlData)
    print webUrl.getcode()
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        PrintResult(data)
    else:
        print "Error from server" + str(webUrl.getcode())

if __name__ == '__main__':
    main()