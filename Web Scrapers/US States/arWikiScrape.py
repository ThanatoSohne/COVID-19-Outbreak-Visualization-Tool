from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep

arWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Arkansas'

arClient = req(arWiki)

site_parse = soup(arClient.read(), "lxml")
arClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_arWiki.csv"
headers = "County/Region, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[50:119]:
    locale = liegen.geocode(h.split('\n')[1] + ", " + "ARKANSAS")
    take = h.split('\n')
    file.write(take[1] + ", " + "ARKANSAS" + ", " + str(locale.latitude) + ", " + str(locale.longitude) + ", " + take[3] + ", " + take[5] + ", " + take[7] +"\n")
    sleep(1)

file.write(hold[119].split('\n')[1] + ", " + "ARKANSAS" +  ", " + "" + ", " + "" + ", " + hold[119].split('\n')[3] + ", " + hold[119].split('\n')[5] + ", " + hold[119].split('\n')[7] +"\n")
    

file.close()

if (hold[50].split('\n')[1]) == 'Arkansas' and (hold[1189].split('\n')[1]) == 'Missing county information':
    print("Arkansas scraper is complete.\n")
else:
    print("ERROR: Must fix Arkansas scraper.\n")