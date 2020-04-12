from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

ohWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Ohio'

ohClient = req(ohWiki)

site_parse = soup(ohClient.read(), "lxml")
ohClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
oh = "OHIO"
co = ' County'

csvfile = "COVID-19_cases_ohWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[52].split('\n')[1]) == 'Adams' and (hold[136].split('\n')[1]) == 'Wyandot':
            
    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[52:137]:
        take = h.split('\n')
        locale = geocoder.opencage(take[1] + co + ", " + oh, key='')
        #locale = liegen.geocode(take[1] + co + ", " + oh)
        #catch_TimeOut(take[1] + co + ", " + oh)
        file.write(take[1] + ", " + oh + ", " + str(locale.latlng).strip('[]') + ", " 
                   + take[3] + ", " + take[5] + "\n")
        #sleep(1)
    
    file.close()

    print("Ohio scraper is complete.")
else:
    print("ERROR: Must fix Ohio scraper.")




