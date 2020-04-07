from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep

moDOH = 'https://health.mo.gov/living/healthcondiseases/communicable/novel-coronavirus/results.php'

moClient = req(moDOH)

site_parse = soup(moClient.read(), "lxml")
moClient.close()

tables = site_parse.find("div", {"class": "panel-group"}).findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
mo = "MISSOURI"
co = ' County'

csvfile = "COVID-19_cases_modoh.csv"
headers = "County, State, Latitude, Longitude, Cases \n"
sHeaders = "County, State, Latitude, Longitude,  Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for t in tables[1:40]:
    pull = t.findAll('td')
    locale = liegen.geocode(pull[0].text + co + ", " + mo)
    file.write(pull[0].text + ", " + mo + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + pull[1].text + "\n")
    sleep(1.1)

sleep(1)

for t in tables[40:80]:
    pull = t.findAll('td')
    locale = liegen.geocode(pull[0].text + co + ", " + mo)
    file.write(pull[0].text + ", " + mo + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + pull[1].text + "\n")
    sleep(1.1)


for t in tables[80:118]:
    pull = t.findAll('td')
    locale = liegen.geocode(pull[0].text + co + ", " + mo)
    file.write(pull[0].text + ", " + mo + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + pull[1].text + "\n")
    sleep(1)


file.write(tables[118].find('td').text + ", " + mo + ", " + "" + ", "
               + "" + ", " + tables[118].findAll('td')[1].text + "\n")

tablesDe = site_parse.find("div", {"id": "collapseDeaths"}).findAll('tr')

file.write("\n")
file.write(sHeaders)

for ta in tablesDe[1:11]:
    pullDe = ta.findAll('td')
    localeD = liegen.geocode(pullDe[0].text + co + ", " + mo)
    file.write(pullDe[0].text + ", " + mo + ", " + str(localeD.latitude) + ", "
               + str(localeD.longitude) + ", " + pullDe[1].text + "\n")
    sleep(1)

file.write(tablesDe[11].find('td').text + ", " + mo + ", " + "" + ", "
               + "" + ", " + tablesDe[11].findAll('td')[1].text + "\n")

file.close()

if (tables[1].find('td').text) == 'Adair' and (tables[118].find('td').text) == 'TBD':
    print("Missouri scraper is complete.")
else:
    print("ERROR: Must fix Missour scraper.")