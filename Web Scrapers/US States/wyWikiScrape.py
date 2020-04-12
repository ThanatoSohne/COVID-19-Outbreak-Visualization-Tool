from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

wyWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Wyoming'

wyClient = req(wyWiki)

site_parse = soup(wyClient.read(), "lxml")
wyClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
wy = "WYOMING"
co = ' County'

csvfile = "COVID-19_cases_wyWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[50].split('\n')[1]) == 'Albany' and (hold[72].split('\n')[1]) == 'Weston':
            
    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[50:73]:
        take = h.split('\n')
        locale = geocoder.opencage(take[1] + co + ", " + wy, key='')
        #catch_TimeOut(locale)
        file.write(take[1] + ", " + wy + ", " + str(locale.latlng).strip('[]') + ", " 
                   + take[3] + ", " + take[5] + "\n")
        #sleep(1.1)
    
    file.close()

    print("Wyoming scraper is complete.")
else:
    print("ERROR: Must fix Wyoming scraper.")




