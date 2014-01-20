# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import re
import urllib2
import json

url="https://www.govtrack.us/data/congress/113/bills/hr/hr41/data.json"
jsonResponse = json.loads(urllib2.urlopen(url).read())
print json.dumps(jsonResponse,indent=4)
print("=================================")
print("Bill id: %s" % jsonResponse["bill_id"])
print("Bill introduced at: %s" % jsonResponse["introduced_at"]) 
print("Official title: %s" % jsonResponse["official_title"])
print("Number of actions = %d." % len(jsonResponse["actions"]))
