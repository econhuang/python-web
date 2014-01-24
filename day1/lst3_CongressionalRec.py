# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import urllib2
import sys
import os
import time

"""Download "Entire Issue" of the Congressional Record for the period January 1- 10 2014."""

month = 1

# try downloading the Congressional Record for the first ten days of Jan 2014
for day in range(1,11):

    # construct the URL from which we will try to retrieve the record
    fileName = "CREC-2014-%02d-%02d.pdf" % (month,day)
    fileURL="http://beta.congress.gov/crec/2014/%02d/%02d/%s"  % (month,day,fileName)

    try:
        # use the urllib2 module to access the Congressional URL (PDF document) 
        resp = urllib2.urlopen(fileURL)

        # write the record to a local file
        fout = open(fileName,"wb")
        fout.write(resp.read())
        fout.close()

        print("Downloaded file %s." % fileURL)

    except:
        # if the Record is unavailable, ignore and try the next day
        pass

    time.sleep(2)
