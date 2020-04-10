from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

njWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_New_Jersey'

njClient = req(njWiki)

site_parse = soup(njClient.read(), "lxml")
njClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
nj = "NEW JERSEY"
co = ' County'

csvfile = "COVID-19_cases_njWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[54:75]:
    take = h.split('\n')
    locale = liegen.geocode(take[1] + co + ", " + nj)
    file.write(take[1] + ", " + nj + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " +take[3].replace(',','') + ", " 
               + take[5].replace(',','') + ", " + take[7].replace(',','') + "\n")
    sleep(1.1)

file.write(hold[75].split('\n')[1] + ", " + nj + ", " + "" + ", " + "" + ", " 
           + hold[75].split('\n')[3].replace(',','') + ", " + hold[75].split('\n')[5].replace(',','') 
           + ", " + hold[75].split('\n')[7].replace(',','') + "\n")

file.close()

if (hold[54].split('\n')[1]) == 'Atlantic' and (hold[75].split('\n')[1]) == 'Under investigation':
    print("New Jersey scraper is complete.")
else:
    print("ERROR: Must fix New Jersey scraper.")
