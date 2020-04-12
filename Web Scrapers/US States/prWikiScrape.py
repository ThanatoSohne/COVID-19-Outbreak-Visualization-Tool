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

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[48].split('\n')[1]) == 'Arecibo' and (hold[56].split('\n')[1]) == 'Not available':
            
    file = open(csvfile, "w")
    file.write(headers)
                
    aLocale = liegen.geocode(hold[48].split('\n')[1] + ", PR")
    file.write(hold[48].split('\n')[1] + ", " + pr + ", " + str(aLocale.latitude)
               + ", " + str(aLocale.longitude) + ", " + hold[48].split('\n')[5] + "\n")
    sleep(1)
    bLocale = liegen.geocode(hold[49].split('\n')[1] + ", PR")
    file.write(hold[49].split('\n')[1] + ", " + pr + ", " + str(bLocale.latitude)
               + ", " + str(bLocale.longitude) + ", " + hold[49].split('\n')[5] + "\n")
    sleep(1)
    cLocale = liegen.geocode(hold[50].split('\n')[1] + ", PR")
    file.write(hold[50].split('\n')[1] + ", " + pr + ", " + str(cLocale.latitude)
               + ", " + str(cLocale.longitude) + ", " + hold[50].split('\n')[5] + "\n")
    sleep(1)
    fLocale = liegen.geocode(hold[51].split('\n')[1] + ", PR")
    file.write(hold[51].split('\n')[1] + ", " + pr + ", " + str(fLocale.latitude)
               + ", " + str(fLocale.longitude) + ", " + hold[51].split('\n')[5] + "\n")
    sleep(1)
    maLocale = liegen.geocode(hold[52].split('\n')[1] + ", PR")
    file.write(hold[52].split('\n')[1] + ", " + pr + ", " + str(maLocale.latitude)
               + ", " + str(maLocale.longitude) + ", " + hold[52].split('\n')[5] + "\n")
    sleep(1)
    meLocale = liegen.geocode("Canovanas, PR")
    file.write(hold[53].split('\n')[1] + ", " + pr + ", " + str(meLocale.latitude)
               + ", " + str(meLocale.longitude) + ", " + hold[53].split('\n')[5] + "\n")
    sleep(1)
    pLocale = liegen.geocode(hold[54].split('\n')[1] + ", PR")
    file.write(hold[54].split('\n')[1] + ", " + pr + ", " + str(pLocale.latitude)
               + ", " + str(pLocale.longitude) + ", " + hold[54].split('\n')[5] + "\n")
    sleep(1)
    file.write(hold[55].split('\n')[1] + ", " + pr + ", " + ""
               + ", " + "" + ", " + hold[55].split('\n')[5] + "\n")
    file.write(hold[56].split('\n')[1] + ", " + pr + ", " + str(liegen.geocode(pr).latitude)
               + ", " + str(liegen.geocode(pr).longitude) + ", " + hold[56].split('\n')[5] + "\n")
    
    file.close()
    print("Puerto Rico scraper is complete.")
else:
    print("ERROR: Must fix Puerto Rico scraper.")

