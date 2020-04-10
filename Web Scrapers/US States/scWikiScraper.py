from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

scWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_South_Carolina'

scClient = req(scWiki)

site_parse = soup(scClient.read(), "lxml")
scClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
sc = "SOUTH CAROLINA"
co = ' County'

csvfile = "COVID-19_cases_scWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[51:97]:
    take = h.split('\n')
    locale = liegen.geocode(take[1] + co + ", " + sc)
    file.write(take[1] + ", " + sc + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
    sleep(1.1)

file.close()

if (hold[51].split('\n')[1]) == 'Abbeville' and (hold[96].split('\n')[1]) == 'York':
    print("South Carolina scraper is complete.")
else:
    print("ERROR: Must fix South Carolina scraper.")




