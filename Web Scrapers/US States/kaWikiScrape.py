from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

kaWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Kansas'

kaClient = req(kaWiki)

site_parse = soup(kaClient.read(), "lxml")
kaClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ka = "KANSAS"
co = ' County'

csvfile = "COVID-19_cases_kaWiki.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[50:103]:
    locale = liegen.geocode(h.split('\n')[1] + co + ", " + ka)
    take = h.split('\n')
    file.write(take[1] + ", " + ka + ", " + str(locale.latitude) + ", " +  
               str(locale.longitude) + ", " + take[3] + ", " + take[4] + "\n")
    sleep(2)

file.close()

if (hold[50].split('\n')[1]) == 'Atchison' and (hold[102].split('\n')[1]) == 'Wyandotte':
    print("Kansas scraper is complete.\n")
else:
    print("ERROR: Must fix Kansas scraper.\n")


