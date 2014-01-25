# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

from bs4 import BeautifulSoup
import urllib2
import codecs

"""Extract and print link information from the Senate Section column."""

URL = "http://beta.congress.gov/congressional-record/browse-by-date/"
soup = BeautifulSoup(urllib2.urlopen(URL).read())

table = soup.find("table")

childRows = table.find_all("tr")

fout = codecs.open("SenateSectionLinks.txt",mode="w",encoding="utf-8")
for childRow in childRows[1:]:
    childColumns = childRow.find_all("td")
    try:
        fout.write("%s,%s\n" \
                % (childColumns[2].find("a").text,childColumns[2].find("a").get("href")))
    except:
        #fout.write("--,--\n")
        pass

fout.close()
