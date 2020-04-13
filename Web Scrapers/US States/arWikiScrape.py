from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep
import geocoder 
import addfips

arWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Arkansas'

arClient = req(arWiki)

site_parse = soup(arClient.read(), "lxml")
arClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_arWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
ar = "ARKANSAS"
fips = addfips.AddFIPS()

hold = []
    
for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[54].split('\n')[1]) == 'Arkansas' and (hold[124].split('\n')[1]) == 'Missing county information':
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[54:124]:
        take = h.split('\n')
        file.write(take[1] + ", " + ar + ", " + fips.get_county_fips(take[1], state = ar) + ", "
                   + str(geocoder.opencage(h.split('\n')[1] + ", " + ar, key='').latlng).strip('[]') 
                   +  ", " + take[3] + ", " + take[5] + ", " + take[7] +"\n")
    
    file.write(hold[124].split('\n')[1] + ", " + ar +  ", " + fips.get_state_fips(ar) + ", "
               + str(geocoder.opencage(ar, key='').latlng).strip('[]') 
               +", "+ hold[124].split('\n')[3] + ", " + hold[124].split('\n')[5] + ", " + hold[124].split('\n')[7] +"\n")
        
    file.close()

else:
    print("ERROR: Must fix Arkansas scraper.")