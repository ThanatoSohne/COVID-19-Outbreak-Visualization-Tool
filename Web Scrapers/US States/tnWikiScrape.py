from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep
import geocoder 

tnWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Tennessee'

tnClient = req(tnWiki)

site_parse = soup(tnClient.read(), "lxml")
tnClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_tnWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"
tn = "TENNESSEE"
co = ' County'

hold = []
    
for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[129].split('\n')[1]) == 'Anderson' and (hold[218].split('\n')[1]) == 'Pending':
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[129:217]:
        take = h.split('\n').split('[')[0]
        locale = geocoder.opencage(take[1] + co + ", " + tn, key='bf1344578b6f462c9183655c80b12d1e')
        file.write(take[1] + ", " + tn + ", " + str(locale.latlng).strip('[]') 
                   +  ", " + take[3] + ", " + take[5] + ", " + take[7] +"\n")
    
    file.write(hold[217].split('\n')[1].split('[')[0] + ", " + tn +  ", "  
               + str(geocoder.opencage(tn, key='bf1344578b6f462c9183655c80b12d1e').latlng).strip('[]') 
               +", "+ hold[217].split('\n')[3] + ", " + hold[217].split('\n')[5] + ", " + hold[217].split('\n')[7] +"\n")
    file.write(hold[218].split('\n')[1].split('[')[0] + ", " + tn +  ", "  
               + str(geocoder.opencage(tn, key='bf1344578b6f462c9183655c80b12d1e').latlng).strip('[]') 
               +", "+ hold[218].split('\n')[3] + ", " + hold[218].split('\n')[5] + ", " + hold[218].split('\n')[7] +"\n")
        
    file.close()
    
    print("Tennessee scaper is complete.")
else:
    print("ERROR: Must fix Tennessee scraper.")
    