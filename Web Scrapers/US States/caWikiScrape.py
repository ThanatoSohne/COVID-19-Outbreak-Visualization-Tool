from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep
import addfips

caWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_California'

caClient = req(caWiki)

site_parse = soup(caClient.read(), 'lxml')
caClient.close()

tables = site_parse.find("div", {"class": "tp-container"}).find_all('tbody')

ca = "CALIFORNIA"
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_caWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"

hold = []

for t in tables:
    pull = t.findAll('tr')
    for p in pull[2:]:
        take = p.get_text()
        hold.append(take)

if (hold[0].split('\n')[1]) == 'Los Angeles' and (hold[52].split('\n')[1]) == 'Tuolumne':

    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[:53]:
        take = h.split('\n')
        file.write(take[1] + ", " + ca + ", " + fips.get_county_fips(take[1], state = ca) 
        + ", " + str(geocoder.opencage(h.split('\n')[1].strip('[c]') + ", " + ca, key='').latlng).strip('[]')  
        + ", " + take[3] + ", " + take[5] + "\n")
                
    file.close()
    print("California scraper is complete.")
else:
    print("ERROR: Must fix California scraper.")

