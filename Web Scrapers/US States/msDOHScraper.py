from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import addfips

msDOH = 'https://msdh.ms.gov/msdhsite/_static/14,0,420.html'

msClient = req(msDOH)

site_parse = soup(msClient.read(), "lxml")
msClient.close()

tables = site_parse.find("table", {"id": "msdhTotalCovid-19Cases"}).find("tbody").findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ms = "MISSISSIPPI"
co = ' County'
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_msdoh.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths \n"

if (tables[0].find('td').text) == 'Adams' and (tables[80].find('td').text) == 'Yazoo':

    file = open(csvfile, "w")
    file.write(headers)
    
    for t in tables[:81]:
        pull = t.findAll('td')
        locale = geocoder.opencage(pull[0].text + co + ", " + ms, key='')
        file.write(pull[0].text + ", " + ms + ", " + fips.get_county_fips(pull[0].text, state=ms) + ", " + str(locale.latlng).strip('[]') + ", " 
                   + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()

    print("Mississippi scraper is complete.")
else:
    print("ERROR: Must fix Mississippi scraper.")


