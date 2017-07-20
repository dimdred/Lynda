import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        # separate the path part from the file name
        head, tail = path.split(src)
        print "head: " + head
        print "tail: " + tail

        # make a backup copy by appending ".bak"
        dst = src + ".bak"
        # use the shell to make a copy
        shutil.copy(src,dst)

        # copy over the permissions, modification time and other info
        shutil.copystat(src,dst)

        # rename the original file
        #os.rename("textfile.txt","new_file.txt")

        # put things into a ZIP archive
        #root_dir, tail = path.split(src)
        #shutil.make_archive("archive", "zip", root_dir) # bad example, without control which files would be include into archive

        # more fine control over ZIP files
        with ZipFile("testzip.zip","w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")

main()