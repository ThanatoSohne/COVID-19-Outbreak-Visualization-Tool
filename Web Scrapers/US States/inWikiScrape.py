from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep
import addfips

inWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Indiana'

inClient = req(inWiki)

site_parse = soup(inClient.read(), "lxml")
inClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
inD = "INDIANA"
co = ' County'
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_inWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths\n"

hold = []

for t in tables:
    pull = t.findAll('tr')
    for p in pull:
        take = p.get_text()
        hold.append(take)

if (hold[51].split('\n')[1]) == 'Adams' and (hold[142].split('\n')[1]) == 'Whitley':

    file = open(csvfile, "w")
    file.write(headers)
        
    for h in hold[51:143]:
        take = h.split('\n')
        file.write(take[1] + ", " + inD + ", " + fips.get_county_fips(take[1],state=inD) + ", "
                   + str(geocoder.opencage(h.split('\n')[1] + co + ", " + inD, key='bf1344578b6f462c9183655c80b12d1e').latlng).strip('[]') 
                   + ", " + take[2] + ", " + take[3] + "\n")        
    file.close()

    print("Indiana scraper is complete.")
else:
    print("ERROR: Must fix Indiana scraper.")



