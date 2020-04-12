from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import geocoder

wvWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_West_Virginia'

wvClient = req(wvWiki)

site_parse = soup(wvClient.read(), "lxml")
wvClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
wv = "WEST VIRGINIA"

csvfile = "COVID-19_cases_wvdoh.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if hold[43].split('\n')[1] == 'Barbour County' and hold[85].split('\n')[1] == 'Wyoming County':

    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[43:86]:
        take = h.split('\n')
        locale = geocoder.opencage(take[1] + ", " + wv, key='bf1344578b6f462c9183655c80b12d1e')
        #catch_TimeOut(take[1] + ", " + wv)
        file.write(take[1] + ", " + wv + ", " + str(locale.latlng).strip('[]') + ", "
                   + take[3] + ", " + take[5] + "\n")
        #sleep(1)
    
    file.close()

    print("West Virginia scraper is complete.")
else:
    print("ERROR: Must fix West Virginia scraper.")


