import urllib2
from HTMLParser import HTMLParser

metacount = 0

# subclass for override the handler methods
class MyHTMLParser(HTMLParser):
    # function to handle an opening tag # this will be called when the closing tag > is reached
    def handle_starttag(self, tag, attrs):
        global metacount
        print "Encountered a start tag:", tag
        if tag == "meta":
            metacount += 1
        pos = self.getpos() # return a tuple indication line and character
        print "At line:", pos[0], " position ", pos[1]
        if attrs.__len__ > 0:
            print "\t Attributes:"
            for a in attrs:
                print "\t", a[0], "=", a[1]

    # function to handle the ending tag
    def handle_endtag(self, tag):
        print "\nEncountered an end tag:", tag
        pos = self.getpos()
        print "At line:", pos[0], " position ", pos[1]

    # handle tag content
    def handle_data(self, data):
        print "\nEncountered some data:", data
        pos = self.getpos()
        print "At line:", pos[0], " position ", pos[1]

    # function to handle the processing of HTML comments
    def handle_comment(self, data):
        print "\nEncountered comment:", data
        pos = self.getpos()
        print "At line:", pos[0], " position ", pos[1]

def main():
    parser = MyHTMLParser()

    # open the HTML and read
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)

    print "%d meta tags encountered" %metacount

if __name__ == '__main__':
    main()