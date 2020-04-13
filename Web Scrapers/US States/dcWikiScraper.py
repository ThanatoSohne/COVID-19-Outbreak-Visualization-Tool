from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep
import addfips

dcWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

dcClient = req(dcWiki)

site_parse = soup(dcClient.read(), "lxml")
dcClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_dcWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

dc = "WASHINGTON DC"
fips = addfips.AddFIPS()

dcGeo = liegen.geocode(dc)

sleep(1)

hold = []

for t in tables:
    pull = t.findAll('tr')
    for p in pull:
        take = p.get_text()
        hold.append(take)

if hold[26].split('\n')[3] == "Washington D.C.":

    file = open(csvfile, "w")
    file.write(headers)
        
    file.write(hold[26].split('\n')[3] + ", " + dc + ", " 
               + fips.get_county_fips("Washington", state= "DC") + ", " + str(dcGeo.latitude) 
               + ", " + str(dcGeo.longitude) + ", " + hold[26].split('\n')[5].replace(',','') 
               + ", " + hold[26].split('\n')[7].replace(',','') + ", " 
               + hold[26].split('\n')[9].replace(',','') + "\n")
    
    file.close()

    print("DC scraper is complete.")
else:
    print("ERROR: Must fix DC scraper.")