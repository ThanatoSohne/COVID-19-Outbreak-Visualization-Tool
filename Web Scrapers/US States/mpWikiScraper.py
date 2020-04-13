from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep
import addfips

mpWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

mpClient = req(mpWiki)

site_parse = soup(mpClient.read(), "lxml")
mpClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_mpWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

mp = "NORTHERN MARIANA ISLANDS"
fips = addfips.AddFIPS()

mpGeo = liegen.geocode(mp)

sleep(1)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if hold[54].split('\n')[3] == "Northern Mariana Islands":

    file = open(csvfile, "w")
    file.write(headers)
    
    file.write(hold[54].split('\n')[3] + ", " + mp + ", " + fips.get_county_fips("Rota",state=mp) + ", "  + str(mpGeo.latitude) 
               + ", " + str(mpGeo.longitude) + ", " + hold[54].split('\n')[5].replace(',','') 
               + ", " + hold[54].split('\n')[7].replace(',','') + ", " 
               + hold[54].split('\n')[9].replace(',','') + "\n")
    
    file.close()

    print("Northern Mariana Islands scraper is complete.")
else:
    print("ERROR: Must fix Northern Mariana Islands scraper.")