from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep

inWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Indiana'

inClient = req(inWiki)

site_parse = soup(inClient.read(), "lxml")
inClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
inD = "INDIANA"
co = ' County'

csvfile = "COVID-19_cases_inWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[49:123]:
    locale = liegen.geocode((h.split('\n')[1] + co) + ", " + inD)
    take = h.split('\n')
    file.write(take[1] + ", " + inD + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + take[2] + ", " + take[3] + "\n")
    sleep(1)

file.write(hold[123].split('\n')[1] + ", " + inD + ", " + "" + ", " 
               + "" + ", " + hold[123].split('\n')[2] + ", " + hold[123].split('\n')[3] + "\n")

for h in hold[124:141]:
    locale = liegen.geocode((h.split('\n')[1] + co) + ", " + inD)
    take = h.split('\n')
    file.write(take[1] + ", " + inD + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + take[2] + ", " + take[3] + "\n")
    sleep(1)

file.close()

if (hold[49].split('\n')[1]) == 'Adams' and (hold[140].split('\n')[1]) == 'Whitley':
    print("Indiana scraper is complete.")
else:
    print("ERROR: Must fix Indiana scraper.")




