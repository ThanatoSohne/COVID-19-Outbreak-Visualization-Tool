from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import geocoder
import addfips

mdWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Maryland'

mdClient = req(mdWiki)

site_parse = soup(mdClient.read(), "lxml")
mdClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
md = "MARYLAND"
co = ' County'
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_mdWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[81].split('\n')[1]) == 'Allegany' and (hold[105].split('\n')[1]) == 'Unassigned':
            
    file = open(csvfile, "w")
    file.write(headers)
        
    for h in hold[81:105]:
        take = h.split('\n')
        file.write(take[1] + ", " + md + ", " + fips.get_county_fips(take[1],state=md) + ", "
                   + str(geocoder.opencage(h.split('\n')[1] + co + ", " + md, key='').latlng).strip('[]') 
                   + ", " + take[3] + ", " + take[5] + ", " 
                   + take[7] + "\n")
        
    file.write(hold[105].split('\n')[1] + ", " + md + ", " + fips.get_state_fips(md) + ", " + str(liegen.geocode(md).latitude) + ", " 
               + str(liegen.geocode(md).longitude) + ", " 
               + hold[105].split('\n')[3] + ", " + hold[105].split('\n')[5] + ", " 
               + hold[105].split('\n')[7] + "\n")
    
    file.close()

    print("Maryland scraper is complete.")
else:
    print("ERROR: Must fix Maryland scraper.")