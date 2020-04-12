from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

neWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Nebraska'

neClient = req(neWiki)

site_parse = soup(neClient.read(), "lxml")
neClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ne = "NEBRASKA"
co = ' County'

csvfile = "COVID-19_cases_neWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[50].split('\n')[1]) == 'Adams' and (hold[91].split('\n')[1]) == 'TBD':
                        
    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[50:91]:
        take = h.split('\n')
        locale = geocoder.opencage(take[1] + co + ", " + ne, key='')
        #locale = liegen.geocode(take[1] + co + ", " + ne)
        #catch_TimeOut(take[1] + co + ", " + ne)
        file.write(take[1] + ", " + ne + ", " + str(locale.latlng).strip('[]') + ", " 
                   + take[3] + ", " + take[5] + "\n")
        #sleep(1.1)
    
    file.write(hold[91].split('\n')[1] + ", " + ne + ", " + str(liegen.geocode(ne).latitude)
               + ", " + str(liegen.geocode(ne).longitude) + ", " 
               + hold[91].split('\n')[3] + ", " + hold[91].split('\n')[5] + "\n")
    
    file.close()

    print("Nebraska scraper is complete.")
else:
    print("ERROR: Must fix Nebraska scraper.")
