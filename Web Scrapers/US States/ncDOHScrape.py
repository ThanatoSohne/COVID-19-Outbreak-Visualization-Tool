from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

ncDOH = 'https://www.ncdhhs.gov/covid-19-case-count-nc#nc-counties-with-cases'

ncClient = req(ncDOH)

site_parse = soup(ncClient.read(), 'lxml')
ncClient.close()

tables = site_parse.find("div", {"class": "content band-content landing-wrapper"}).find('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
nc = "NORTH CAROLINA"

csvfile = "COVID-19_cases_ncdoh.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('tr')

for tag in tags:
    pull = tag.findAll('td')
    locale = liegen.geocode(pull[0].text + ", " + nc)
    file.write(pull[0].text + ", " + nc + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + pull[1].text + ", " 
               + pull[2].text + "\n")
    sleep(1.1)

file.close()

if (tags[0].find('td').text) == 'Alamance County' and (tags[89].find('td').text) == 'Yadkin County':
    print("North Carolina scraper is complete.")
else:
    print("ERROR: Must fix North Carolina scraper.")