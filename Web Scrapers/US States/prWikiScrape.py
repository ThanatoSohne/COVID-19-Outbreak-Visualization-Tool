from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

prWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Puerto_Rico'

prClient = req(prWiki)

site_parse = soup(prClient.read(), "lxml")
prClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
pr = "PUERTO RICO"

csvfile = "COVID-19_cases_prWiki.csv"
headers = "Region, State, Latitude, Longitude, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)
            
aLocale = liegen.geocode(hold[42].split('\n')[1] + ", PR")
file.write(hold[42].split('\n')[1] + ", " + pr + ", " + str(aLocale.latitude)
           + ", " + str(aLocale.longitude) + ", " + hold[42].split('\n')[5] + "\n")
sleep(1)
bLocale = liegen.geocode(hold[43].split('\n')[1] + ", PR")
file.write(hold[43].split('\n')[1] + ", " + pr + ", " + str(bLocale.latitude)
           + ", " + str(bLocale.longitude) + ", " + hold[43].split('\n')[5] + "\n")
sleep(1)
cLocale = liegen.geocode(hold[44].split('\n')[1] + ", PR")
file.write(hold[44].split('\n')[1] + ", " + pr + ", " + str(cLocale.latitude)
           + ", " + str(cLocale.longitude) + ", " + hold[44].split('\n')[5] + "\n")
sleep(1)
fLocale = liegen.geocode(hold[45].split('\n')[1] + ", PR")
file.write(hold[45].split('\n')[1] + ", " + pr + ", " + str(fLocale.latitude)
           + ", " + str(fLocale.longitude) + ", " + hold[45].split('\n')[5] + "\n")
sleep(1)
maLocale = liegen.geocode(hold[46].split('\n')[1] + ", PR")
file.write(hold[46].split('\n')[1] + ", " + pr + ", " + str(maLocale.latitude)
           + ", " + str(maLocale.longitude) + ", " + hold[46].split('\n')[5] + "\n")
sleep(1)
meLocale = liegen.geocode("Canovanas, PR")
file.write(hold[47].split('\n')[1] + ", " + pr + ", " + str(meLocale.latitude)
           + ", " + str(meLocale.longitude) + ", " + hold[47].split('\n')[5] + "\n")
sleep(1)
pLocale = liegen.geocode(hold[48].split('\n')[1] + ", PR")
file.write(hold[48].split('\n')[1] + ", " + pr + ", " + str(pLocale.latitude)
           + ", " + str(pLocale.longitude) + ", " + hold[48].split('\n')[5] + "\n")
sleep(1)
file.write(hold[49].split('\n')[1] + ", " + pr + ", " + ""
           + ", " + "" + ", " + hold[49].split('\n')[5] + "\n")
file.write(hold[50].split('\n')[1] + ", " + pr + ", " + ""
           + ", " + "" + ", " + hold[50].split('\n')[5] + "\n")

file.close()

if (hold[42].split('\n')[1]) == 'Arecibo' and (hold[50].split('\n')[1]) == 'Not available':
    print("Puerto Rico scraper is complete.")
else:
    print("ERROR: Must fix Puerto Rico scraper.")




