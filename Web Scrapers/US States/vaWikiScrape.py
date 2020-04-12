from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

vaWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Virginia'

vaClient = req(vaWiki)

site_parse = soup(vaClient.read(), "lxml")
vaClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
va = "VIRGINIA"

csvfile = "COVID-19_cases_vaWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[52].split('\n')[1]) == 'Accomack County' and (hold[176].split('\n')[1]) == 'York County':

    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[52:76]:
        take = h.split('\n')
        locale = geocoder.opencage(take[1] + ", " + va, key='')
        #catch_TimeOut(take[1] + ", " + va)
        file.write(take[1] + ", " + va + ", " + str(locale.latlng).strip('[]') + ", "
                   + take[3].split('[')[0] + ", " + take[5].split('[')[0] + "\n")
        #sleep(1)
        
    for h in hold[78:82]:
        take = h.split('\n')
        locale = geocoder.opencage(take[1] + ", " + va, key='')
        #catch_TimeOut(take[1] + ", " + va)
        file.write(take[1] + ", " + va + ", " + str(locale.latlng).strip('[]') + ", "
                   + take[3].split('[')[0] + ", " + take[5].split('[')[0] + "\n")
        #sleep(1)
    
    for h in hold[83:136]:
        take = h.split('\n')
        locale = geocoder.opencage(take[1] + ", " + va, key='')
        #catch_TimeOut(take[1] + ", " + va)
        file.write(take[1] + ", " + va + ", " + str(locale.latlng).strip('[]') + ", "
                   + take[3].split('[')[0] + ", " + take[5].split('[')[0] + "\n")
        #sleep(1.1)
    
    for h in hold[137:148]:
        take = h.split('\n')
        locale = geocoder.opencage(take[1] + ", " + va, key='')
        #catch_TimeOut(take[1] + ", " + va)
        file.write(take[1] + ", " + va + ", " + str(locale.latlng).strip('[]') + ", "
                   + take[3].split('[')[0] + ", " + take[5].split('[')[0] + "\n")
        #sleep(1)
    
    for h in hold[149:177]:
        take = h.split('\n')
        locale = geocoder.opencage(take[1] + ", " + va, key='')
        #catch_TimeOut(take[1] + ", " + va)
        file.write(take[1] + ", " + va + ", " + str(locale.latlng).strip('[]') + ", "
                   + take[3].split('[')[0] + ", " + take[5].split('[')[0] + "\n")
        #sleep(1)
    
    file.close()

    print("Virginia scraper is complete.")
else:
    print("ERROR: Must fix Virginia scraper.")