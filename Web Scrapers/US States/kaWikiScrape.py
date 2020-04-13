from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import geocoder
import addfips

kaWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Kansas'

kaClient = req(kaWiki)

site_parse = soup(kaClient.read(), "lxml")
kaClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ka = "KANSAS"
co = ' County'
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_kaWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths\n"

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[55].split('\n')[1]) == 'Anderson' and (hold[117].split('\n')[1]) == 'Wyandotte':
   
    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[55:118]:
        take = h.split('\n')
        file.write(take[1] + ", " + ka + ", " + fips.get_county_fips(take[1],state=ka) + ", "
                   + str(geocoder.opencage(h.split('\n')[1] + co + ", " + ka, key='').latlng).strip('[]') 
                   + ", " + take[3].split(' (')[0] + ", " + take[4].replace('-','0') + "\n")        
    file.close()

    print("Kansas scraper is complete.")
else:
    print("ERROR: Must fix Kansas scraper.")

