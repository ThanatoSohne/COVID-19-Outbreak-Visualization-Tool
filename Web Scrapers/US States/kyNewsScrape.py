from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import addfips

kyNews = 'https://www.courier-journal.com/story/news/2020/03/09/coronavirus-kentucky-how-many-cases-and-where-they-kentucky/5001636002/'

kyClient = req(kyNews)

site_parse = soup(kyClient.read(), "lxml")
kyClient.close()

tables = site_parse.find("div", {"class": "asset-double-wide double-wide p402_premium"})

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ky = "KENTUCKY"
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_kyNews.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths\n"

tag = tables.find_all('p')[12:120]

hold = []

for t in tag:
    take = t.get_text()
    hold.append(take)
    
if (hold[0].split(':')[0]) == 'Adair County' and (hold[101].split(':')[0]) == 'No County Available':

    file = open(csvfile, "w")
    file.write(headers)
        
    for h in hold[:101]: 
        file.write(h.split(':')[0] + ", " + ky + ", " + fips.get_county_fips(h.split(':')[0],state=ky) + ", "
                   + str(geocoder.opencage(h.split('\n')[0] + ", " + ky, key='').latlng).strip('[]') 
                   + ", " + h.split(':')[1].split('c')[0].strip()
                   + ", " + h.split('case')[1].strip('; ').strip(' death').replace('\xa0', '').strip(',').strip('s').strip() + "\n")
    
    file.write(hold[101].split(':')[0] + ", " + ky + ", " + fips.get_state_fips(ky) + ", "
               + str(liegen.geocode(ky).latitude) + ", " 
               + str(liegen.geocode(ky).longitude) + ", "
               + hold[101].split(':')[1].split('c')[0].strip() + ", "
               + hold[101].split('case')[1].strip('; ').strip(' death').replace('\xa0', '').strip(',').strip('s').strip() + "\n")
        
    file.close()

    print("Kentucky scraper is complete.")
else:
    print("ERROR: Must fix Kentucky scraper.")