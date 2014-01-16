from bs4 import BeautifulSoup 
import urllib2

URL = "http://beta.congress.gov/congressional-record/browse-by-date/" 
soup = BeautifulSoup(urllib2.urlopen(URL).read())

table = soup.find("table") 

childRows = table.find_all("tr")
for i in range(1,5):
    print(childRows[i]) 
