# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import re
import urllib2
from bs4 import BeautifulSoup

url = "http://www.senate.gov/general/contact_information/senators_cfm.xml"
xml = urllib2.urlopen(url).read()
soup = BeautifulSoup(xml)

#print soup.prettify()

#members = soup.find_all("member")
#print("Found %d senate members." % len(members)")

#members = soup.find_all("member")
#first_name = members[0].first_name.string
#last_name = members[0].last_name.string
#party = members[0].party.string
#state = members[0].state.string

for member in soup.find_all("member"):
    first_name = member.first_name.string
    last_name = member.last_name.string
    party = member.party.string
    state = member.state.string
    print ("%s\t%s\t%s\t%s" % (first_name,last_name,party,state))
