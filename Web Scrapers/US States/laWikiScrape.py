from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep
import geocoder
import addfips

laWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Louisiana'

laClient = req(laWiki)

site_parse = soup(laClient.read(), "lxml")
laClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
la = "LOUISIANA"
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_laWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths\n"

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)
    
if (hold[92].split('\n')[1]) == 'Acadia' and (hold[156].split('\n')[1]) == 'Under Investigation':
        
    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[92:156]:
        take = h.split('\n')
        file.write(take[1] + ", " + la + ", " + fips.get_county_fips(take[1],state=la) + ", "
                   + str(geocoder.opencage(h.split('\n')[1] + ", " + la, key='').latlng).strip('[]') 
                   + ", " + take[3].replace(',','') + ", " 
                   + take[5].replace(',','') + "\n")
    
    file.write(hold[156].split('\n')[1] + ", " + la + ", " + fips.get_state_fips(la) + ", " + str(liegen.geocode(la).latitude) + ", " 
                   + str(liegen.geocode(la).longitude) + ", " + hold[156].split('\n')[3].replace(',','') + ", " 
                   + hold[156].split('\n')[5].replace(',','') + "\n")
    
    file.close()

    print("Louisiana scraper is complete.")
else:
    print("ERROR: Must fix Louisiana scraper.")