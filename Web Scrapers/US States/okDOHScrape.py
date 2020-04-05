from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

okDOH = 'https://coronavirus.health.ok.gov/'

okClient = req(okDOH)

site_parse = soup(okClient.read(), "lxml")
okClient.close()

tables = site_parse.find("table", {"summary": "COVID-19 Cases by County"}).find("tbody")

tags = tables.findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ok = "OKLAHOMA"
co = ' County'

csvfile = "COVID-19_cases_okdoh.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[:56]:
    pull = tag.findAll('td')
    locale = liegen.geocode(pull[0].text + co + ", " + ok)
    file.write(pull[0].text + ", " + ok + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")
    sleep(1)
    
file.close()

if (tags[0].find('td').text) == 'Adair' and (tags[55].find('td').text) == 'Woodward':
    print("Oklahoma scraper is complete.")
else:
    print("ERROR: Must fix Oklahoma scraper.")