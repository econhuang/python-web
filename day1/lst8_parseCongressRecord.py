from bs4 import BeautifulSoup
import urllib2
import codecs
import re

baseURL = "http://beta.congress.gov"
#URL = "http://beta.congress.gov/congressional-record/browse-by-date/"
URL = baseURL + "/congressional-record/browse-by-date/"
soup = BeautifulSoup(urllib2.urlopen(URL).read())

table = soup.find("table")

childRows = table.find_all("tr")

for childRow in childRows[1:]:
    childColumns = childRow.find_all("td")
    try:
        print("Senate section link: %s%s\n" \
                % (baseURL,childColumns[2].find(href=re.compile(".*")).get("href")))
    except:
        pass
