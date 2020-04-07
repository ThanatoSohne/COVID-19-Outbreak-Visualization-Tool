from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

orDOH = 'https://govstatus.egov.com/OR-OHA-COVID-19'

orClient = req(orDOH)

site_parse = soup(orClient.read(), "lxml")
orClient.close()

tables = site_parse.find("div", {"id": "collapseOne"}).find("tbody")

tags = tables.findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
orG = "OREGON"
co = ' County'

csvfile = "COVID-19_cases_ordoh.csv"
headers = "County, State, Latitude, Longitude, Positive Cases, Deaths, Negative Test Results \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[:36]:
    pull = tag.findAll('td')
    locale = liegen.geocode(pull[0].text + co + ", " + orG)
    file.write(pull[0].text + ", " + orG + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + pull[1].text + ", " 
               + pull[2].text + ", " + pull[3].text + "\n")
    sleep(1)

file.close()

if (tags[0].find('td').text) == 'Baker' and (tags[36].find('td').text) == 'Total':
    print("Oregon Scraper is complete.")
else:
    print("ERROR: Must fix Oregon scraper.")

