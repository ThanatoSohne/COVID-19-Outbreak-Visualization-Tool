from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

vaWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Virginia'

vaClient = req(vaWiki)

site_parse = soup(vaClient.read(), "lxml")
vaClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
va = "VIRGINIA"

csvfile = "COVID-19_cases_vaWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[47:69]:
    take = h.split('\n')
    locale = liegen.geocode(take[1] + ", " + va)
    file.write(take[1] + ", " + va + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + take[3].split('[')[0] 
               + ", " + take[5].split('[')[0] + "\n")
    sleep(1)
    
for h in hold[71:73]:
    take = h.split('\n')
    locale = liegen.geocode(take[1] + ", " + va)
    file.write(take[1] + ", " + va + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + take[3].split('[')[0] 
               + ", " + take[5].split('[')[0] + "\n")
    sleep(1)

for h in hold[74:124]:
    take = h.split('\n')
    locale = liegen.geocode(take[1] + ", " + va)
    file.write(take[1] + ", " + va + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + take[3].split('[')[0] 
               + ", " + take[5].split('[')[0] + "\n")
    sleep(1.2)

for h in hold[125:135]:
    take = h.split('\n')
    locale = liegen.geocode(take[1] + ", " + va)
    file.write(take[1] + ", " + va + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + take[3].split('[')[0] 
               + ", " + take[5].split('[')[0] + "\n")
    sleep(1)

for h in hold[136:163]:
    take = h.split('\n')
    locale = liegen.geocode(take[1] + ", " + va)
    file.write(take[1] + ", " + va + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + take[3].split('[')[0] 
               + ", " + take[5].split('[')[0] + "\n")
    sleep(1)

file.close()

if (hold[47].split('\n')[1]) == 'Accomack County' and (hold[162].split('\n')[1]) == 'York County':
    print("Virginia scraper is complete.")
else:
    print("ERROR: Must fix Virginia scraper.")






