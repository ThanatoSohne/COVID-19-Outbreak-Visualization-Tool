from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep
import geocoder

ioWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Iowa'

ioClient = req(ioWiki)

site_parse = soup(ioClient.read(), "lxml")
ioClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
io = "IOWA"
co = ' County'

csvfile = "COVID-19_cases_ioWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)
            
if (hold[54].split('\n')[1]) == 'Adair' and (hold[133].split('\n')[1]) == 'Wright':

    file = open(csvfile, "w")
    file.write(headers)

    for h in hold[54:134]:
        #locale = liegen.geocode(h.split('\n')[1] + co + ", " + io)
        #catch_TimeOut(h.split('\n')[1] + co + ", " + io)
        take = h.split('\n')
        file.write(take[1] + ", " + io + ", " 
                   + str(geocoder.opencage(h.split('\n')[1] + co + ", " + io, key='').latlng).strip('[]') 
                   + ", " + take[3] + ", " + take[5] + "\n")
        #sleep(1)
        
    file.close()

    print("Iowa scraper is complete.")
else:
    print("ERROR: Must fix Iowa Scraper.")



