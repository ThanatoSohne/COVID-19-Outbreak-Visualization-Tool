from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import geocoder

waWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Washington_(state)'

waClient = req(waWiki)

site_parse = soup(waClient.read(), "lxml")
waClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
wa = "WASHINGTON"
co = ' County'

csvfile = "COVID-19_cases_waWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[50].split('\n')[1]) == 'Adams' and (hold[87].split('\n')[1]) == '(Unassigned by county)':

    file = open(csvfile, "w")
    file.write(headers)    

    for h in hold[50:87]:
        take = h.split('\n')
        locale = geocoder.opencage(take[1] + co + ", " + wa, key='')
        #catch_TimeOut(take[1] + co + ", " + wa)
        file.write(take[1] + ", " + wa + ", " + str(locale.latlng).strip('[]') + ", " 
                   + take[3].split('[')[0].replace(',','') 
                   + ", " + take[5].split('[')[0].replace(',','') + "\n")
        #sleep(1)
        
    file.write(hold[87].split('\n')[1] + ", " + wa + ", " + str(liegen.geocode(wa).latitude) + ", " 
                   + str(liegen.geocode(wa).longitude) + ", " + hold[87].split('\n')[3].split('[')[0].replace(',','') 
                   + ", " + hold[87].split('\n')[5].split('[')[0].replace(',','') + "\n")
    
    file.close()

    print("Washington scraper is complete.")
else:
    print("ERROR: Must fix Washington scraper.")

