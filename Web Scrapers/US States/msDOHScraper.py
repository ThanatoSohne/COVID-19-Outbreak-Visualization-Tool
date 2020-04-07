from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

msDOH = 'https://msdh.ms.gov/msdhsite/_static/14,0,420.html'

msClient = req(msDOH)

site_parse = soup(msClient.read(), "lxml")
msClient.close()

tables = site_parse.find("table", {"id": "msdhTotalCovid-19Cases"}).find("tbody").findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ms = "MISSISSIPPI"
co = ' County'

csvfile = "COVID-19_cases_msdoh.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for t in tables[:80]:
    pull = t.findAll('td')
    locale = liegen.geocode(pull[0].text + co + ", " + ms)
    file.write(pull[0].text + ", " + ms + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")
    sleep(2)

file.close()

if (tables[0].find('td').text) == 'Adams' and (tables[79].find('td').text) == 'Yazoo':
    print("Mississippi scraper is complete.")
else:
    print("ERROR: Must fix Mississippi scraper.")




