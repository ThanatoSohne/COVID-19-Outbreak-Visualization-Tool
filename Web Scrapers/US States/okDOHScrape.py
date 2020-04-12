from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import geocoder

okDOH = 'https://coronavirus.health.ok.gov/'

bypass = {'User-Agent': 'Mozilla/5.0'}
okClient = Request(okDOH, headers=bypass)
okPage = req(okClient)

site_parse = soup(okPage.read(), "lxml")
okPage.close()

tables = site_parse.find("table", {"summary": "COVID-19 Cases by County"}).find("tbody")

tags = tables.findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ok = "OKLAHOMA"
co = ' County'

csvfile = "COVID-19_cases_okdoh.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths \n"

if (tags[0].find('td').text) == 'Adair' and (tags[61].find('td').text) == 'Woodward':

    file = open(csvfile, "w")
    file.write(headers)
    
    for tag in tags[:62]:
        pull = tag.findAll('td')
        locale = geocoder.opencage(pull[0].text + co + ", " + ok, key='')
        #locale = liegen.geocode(pull[0].text + co + ", " + ok)
        #catch_TimeOut(pull[0].text + co + ", " + ok)
        file.write(pull[0].text + ", " + ok + ", " + str(locale.latlng).strip('[]') + ", "
                   + pull[1].text + ", " + pull[2].text + "\n")
        #sleep(1)
        
    file.close()

    print("Oklahoma scraper is complete.")
else:
    print("ERROR: Must fix Oklahoma scraper.")