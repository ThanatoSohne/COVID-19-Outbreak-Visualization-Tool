from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

codoh = 'https://covid19.colorado.gov/case-data'

coClient = req(codoh)

site_parse = soup(coClient.read(), 'lxml')
coClient.close()

tables = site_parse.findAll("div", {"class": "field field--name-field-card-body field--type-text-long field--label-hidden field--item"})[1]

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
co = "COLORADO"

test = tables.findAll('tr')

hold = []

adamsTest = test[1].find('td').text
outTest = test[56].find('td').text

csvfile = "COVID-19_cases_coDOH.csv"
headers = "County/Region, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for t in test[1:55]:
        pull = t.findAll('td')
        locale = liegen.geocode(test[1].find('td').text + ", " + co)
        file.write(pull[0].text + ", " + co + ", " + str(locale.latitude) +
                   ", " + str(locale.longitude) + ", " + pull[1].text + 
                   ", " + pull[2].text + "\n")
        sleep(1)

file.write(test[55].find('td').text + ", " + co + ", " + "" + ", " + "" + ", " +
           test[55].findAll('td')[1].text.strip()+", " +test[55].findAll('td')[2].text.strip()+ "\n")

file.write(test[56].find('td').text + ", " + co + ", " + "" + ", " + "" + ", " +
           test[56].findAll('td')[1].text.strip()+", " +test[56].findAll('td')[2].text.strip()+ "\n")

file.close()

if adamsTest == 'Adams' and outTest == 'Out of state':
    print("Colorado scraper is complete.")
else:
    print("ERROR: Must fix Colorado scraper.")


