from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

ohWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Ohio'

ohClient = req(ohWiki)

site_parse = soup(ohClient.read(), "lxml")
ohClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
oh = "OHIO"
co = ' County'

csvfile = "COVID-19_cases_ohWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[47:129]:
    take = h.split('\n')
    locale = liegen.geocode(take[1] + co + ", " + oh)
    file.write(take[1] + ", " + oh + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
    sleep(1)

file.close()

if (hold[47].split('\n')[1]) == 'Adams' and (hold[128].split('\n')[1]) == 'Wyandot':
    print("Ohio scraper is complete.")
else:
    print("ERROR: Must fix Ohio scraper.")





