from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep
import addfips

ilWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Illinois'

ilClient = req(ilWiki)

site_parse = soup(ilClient.read(), "lxml")
ilClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
il = "ILLINOIS"
co = ' County'
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_ilWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"

hold = []

for t in tables:
    pull = t.findAll('tr')
    for p in pull[2:]:
        take = p.get_text()
        hold.append(take)

if (hold[69].split('\n')[1]) == 'Adams' and (hold[154].split('\n')[1]) == 'Woodford':

    file = open(csvfile, "w")
    file.write(headers)
                
    for h in hold[69:155]:
        take = h.split('\n')
        file.write(take[1] + ", " + il + ", " + fips.get_county_fips(take[1], state=il) + ", "
                   + str(geocoder.opencage(h.split('\n')[1] + co + ", " + il, key='bf1344578b6f462c9183655c80b12d1e').latlng).strip('[]') 
                   + ", " + take[9].replace(',','') + ", " 
                   + take[5].replace(',','') + ", " + take[7].replace(',','') + "\n")
    
    file.write(hold[155].split('\n')[1] + ", " + il + ", " + fips.get_state_fips(il) + ", " + str(liegen.geocode(il).latitude) + ", "
                   + str(liegen.geocode(il).longitude) + ", " + hold[155].split('\n')[9] + ", " + hold[155].split('\n')[5] + ", " 
                   + hold[155].split('\n')[7] + "\n")
    
    file.close()
    
    print("Illinois scraper is complete.")
else:
    print("ERROR: Must fix Illinois scraper.")
