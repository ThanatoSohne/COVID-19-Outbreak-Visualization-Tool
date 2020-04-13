from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep
import geocoder
import addfips

ioWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Iowa'

ioClient = req(ioWiki)

site_parse = soup(ioClient.read(), "lxml")
ioClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
io = "IOWA"
co = ' County'
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_ioWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)
            
if (hold[56].split('\n')[1]) == 'Adair' and (hold[135].split('\n')[1]) == 'Wright':

    file = open(csvfile, "w")
    file.write(headers)

    for h in hold[56:136]:
        take = h.split('\n')
        file.write(take[1] + ", " + io + ", " + fips.get_county_fips(take[1],state=io) + ", " 
                   + str(geocoder.opencage(h.split('\n')[1] + co + ", " + io, key='').latlng).strip('[]') 
                   + ", " + take[3] + ", " + take[5] + "\n")
        
    file.close()

    print("Iowa scraper is complete.")
else:
    print("ERROR: Must fix Iowa Scraper.")


