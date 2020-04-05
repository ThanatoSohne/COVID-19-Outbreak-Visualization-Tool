from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

nyWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_New_York_(state)'

nyClient = req(nyWiki)

site_parse = soup(nyClient.read(), "lxml")
nyClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ny = "NEW YORK"
co = ' County'

csvfile = "COVID-19_cases_nydoh.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries\n"

file = open(csvfile, "w", encoding = 'utf-8')
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[111:168]:
    take = h.split('\n')
    locale = liegen.geocode(take[1].split('[')[0] + co + ", " + ny)
    file.write(take[1].split('[')[0] + ", " + ny + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + take[3].split('[')[0].replace(',','') + ", " + take[5].replace(',','')
               + ", " + take[7].replace(',','') + "\n")
    sleep(1)
    
nycLocale = (hold[169].split('\n')[1] + ", " + ny)
file.write(hold[169].split('\n')[1] + ", " + ny + ", " + str(locale.latitude) 
           + ", " + str(locale.longitude) + ", " + hold[169].split('\n')[3] 
           + ", " + hold[169].split('\n')[5] + ", " + hold[169].split('\n')[7] + "\n")    

file.close()

if (hold[111].split('\n')[1]) == 'Albany' and (hold[167].split('\n')[1]) == 'Yates':
    print("New York scraper is complete.")
else:
    print("ERROR: Must fix New York scraper.")


