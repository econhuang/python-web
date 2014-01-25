# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import re
import urllib2
from bs4 import BeautifulSoup

"""This Python script reads Senators' contact information from
   http://www.senate.gov/general/contact_information/senators_cfm.xml.
   It parses the Senator first and last names, party and state
   and prints this information to screen for all the Senators."""


# Download the XML document from Senate website and create a BeautifulSoup
# object
url = "http://www.senate.gov/general/contact_information/senators_cfm.xml"
xml = urllib2.urlopen(url).read()
soup = BeautifulSoup(xml)

#print soup.prettify()

print "List of Senators and affiliations obtained from www.senate.gov:"

# Find all the member tag objects in the XML document using find_all()
for member in soup.find_all("member"):

    # for each member print out relevant propertie
    first_name = member.first_name.string
    last_name = member.last_name.string
    party = member.party.string
    state = member.state.string

    print ("%s %s (%s), %s" % (first_name,last_name,party,state))
