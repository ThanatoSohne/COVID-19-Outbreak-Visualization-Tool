from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep

asWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

asClient = req(asWiki)

site_parse = soup(asClient.read(), "lxml")
asClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_asWiki.csv"
headers = "Region, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

aSam = "AMERICAN SAMOA"

asGeo = liegen.geocode(aSam)

sleep(1)

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

file.write(hold[19].split('\n')[3] + ", " + aSam + ", " + str(asGeo.latitude) 
           + ", " + str(asGeo.longitude) + ", " + hold[19].split('\n')[5].replace(',','') 
           + ", " + hold[19].split('\n')[7].replace(',','') + ", " 
           + hold[19].split('\n')[9].replace(',','') + "\n")

file.close()

if hold[19].split('\n')[3] == "American Samoa":
    print("American Samoa scraper is complete.")
else:
    print("ERROR: Must fix American Samoa scraper.")
