# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import re
import urllib2
import json

""" Execute a query using the World Bank API and parse the returned JSON document.
    Here the query executed on the World Bank database requests for the
    Solar energy consumption (% in TFEC) for United States from 2000 to 2010.
    The JSON response consists of an array. The second element of the array contains
    values for the indicator between 2000-2010. """

url="http://api.worldbank.org/countries/USA/indicators/2.1.6_SHARE.SOLAR?per_page=10&date=2000:2010&format=json"

jsonResponse = json.loads(urllib2.urlopen(url).read())

# uncomment the following print statement if you want to see JSON returned from
# the World Bank
#print json.dumps(jsonResponse,indent=4)

print "\n========================================================================================"
print "World Bank API Query response: U.S. Solar energy consumption for the period (2000-2010)."
print "========================================================================================="
print "\nDate/Period\tSolar energy consumption (% in TFEC)"

# loop over the results for each year, which are in a list in the second element of the
# JSON object
for obj in jsonResponse[1]:
    print "%s\t%s" % (obj["date"],obj["value"])

