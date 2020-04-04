import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep

cadoh = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_California'

caClient = req(cadoh)

site_parse = soup(caClient.read(), 'lxml')
caClient.close()

tables = site_parse.find("div", {"class": "tp-container"}).find_all('tbody')

ca = "CALIFORNIA"
liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

csvfile = "COVID-19_cases_caWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)

for h in hold[:52]:
    locale = liegen.geocode(h.split('\n')[1].strip('[c]') + ", " + ca)
    take = h.split('\n')
    file.write(take[1] + ", " + ca + ", " + str(locale.latitude) + ", " + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
    sleep(1)
            

file.close()

if (hold[0].split('\n')[1]) == 'Los Angeles' and (hold[51].split('\n')[1]) == 'Tuolumne':
    print("California scraper is complete.\n")
else:
    print("ERROR: Must fix California scraper.\n")

