from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import geocoder

nyWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_New_York_(state)'

nyClient = req(nyWiki)

site_parse = soup(nyClient.read(), "lxml")
nyClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ny = "NEW YORK"
co = ' County'

csvfile = "COVID-19_cases_nydoh.csv"
headers = "County,State,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

j = ''
            
if (hold[118].split('\n')[1]) == 'Albany' and (hold[174].split('\n')[1]) == 'Yates':               
    file = open(csvfile, "w", encoding = 'utf-8')
    file.write(headers)
    
    for h in hold[118:175]:
        take = h.split('\n')
        locale = geocoder.opencage(take[1].split('[')[0] + co + ", " + ny, key='')
        #locale = liegen.geocode(take[1].split('[')[0] + co + ", " + ny)
        #catch_TimeOut(take[1].split('[')[0] + co + ", " + ny)
        file.write(take[1].split('[')[0] + ", " + ny + ", " + str(locale.latlng).strip('[]') + ", " 
                   + take[3].split('[')[0].replace(',','').strip('\n') + ", " + take[5].replace(',','').strip('\n')
                   + ", " + take[7].replace(',','').strip('\n') + "\n")
        #sleep(1)
        
    nycLocale = geocoder.opencage(hold[176].split('\n')[1].strip('(a)').strip() + ", " + ny, key='bf1344578b6f462c9183655c80b12d1e')
    file.write((hold[176].split('\n')[1].strip('(a)').strip() + ", " + ny) + ", " + str(nycLocale.latlng).strip('[]')
               +  ", " + hold[176].split('\n')[3].replace(',','').strip('\n')
               + ", " + hold[176].split('\n')[5].replace(',','').strip('\n')  + ", " + hold[176].split('\n')[7].replace(',','').strip('\n')  + "\n")    
    
    file.close()

    print("New York scraper is complete.")
else:
    print("ERROR: Must fix New York scraper.")

