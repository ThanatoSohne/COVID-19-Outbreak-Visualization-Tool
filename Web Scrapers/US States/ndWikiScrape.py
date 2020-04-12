from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
#from geopy.geocoders import Nominatim
from time import sleep
from geocoder

ndWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_North_Dakota'

ndClient = req(ndWiki)

site_parse = soup(ndClient.read(), "lxml")
ndClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
nd = "NORTH DAKOTA"
co = ' County'

csvfile = "COVID-19_cases_ndWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases \n"

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if hold[47].split('\n')[1] == 'Barnes' and hold[77].split('\n')[1] == 'Williams':

    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[47:78]:
        #locale = liegen.geocode(h.split('\n')[1] + co + ", " + nd)
        locale = geocoder.opencage(h.split('\n')[1] + co + ", " + nd, key='')
        take = h.split('\n')
        file.write(take[1] + ", " + nd + ", " + str(locale.latlng).strip('[]') + ", " + take[3] + "\n")
        #sleep(1.1)
    
    file.close()

    print("North Dakota scraper is complete.")
else:
    print("ERROR: Must fix North Dakota Scraper.")