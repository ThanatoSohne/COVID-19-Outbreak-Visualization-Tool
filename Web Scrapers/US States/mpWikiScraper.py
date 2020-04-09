from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep

mpWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

mpClient = req(mpWiki)

site_parse = soup(mpClient.read(), "lxml")
mpClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_mpWiki.csv"
headers = "Region, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

mp = "NORTHERN MARIANA ISLANDS"

mpGeo = liegen.geocode(mp)

sleep(1)

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

file.write(hold[116].split('\n')[3] + ", " + mp + ", " + str(mpGeo.latitude) 
           + ", " + str(mpGeo.longitude) + ", " + hold[116].split('\n')[5].replace(',','') 
           + ", " + hold[116].split('\n')[7].replace(',','') + ", " 
           + hold[116].split('\n')[9].replace(',','') + "\n")

file.close()

if hold[116].split('\n')[3] == "Northern Mariana Islands":
    print("Northern Mariana Islands scraper is complete.")
else:
    print("ERROR: Must fix Northern Mariana Islands scraper.")