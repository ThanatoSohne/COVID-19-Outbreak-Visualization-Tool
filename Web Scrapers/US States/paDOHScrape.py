from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

paDOH = 'https://www.health.pa.gov/topics/disease/coronavirus/Pages/Cases.aspx'

paClient = req(paDOH)

site_parse = soup(paClient.read(), "lxml")
paClient.close()

tables = site_parse.find("div", {"class": "ms-rtestate-field", "style": "display:inline"}).find("div", {"style": "text-align:center;"}).find("table", {"class": "ms-rteTable-default"})

tags = tables.findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
pa = "PENNSYLVANIA"
co = ' County'

csvfile = "COVID-19_cases_padoh.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[1:]:
    pull = tag.findAll('td')
    locale = liegen.geocode(pull[0].text + co+ ", " + pa)
    file.write(pull[0].text + ", " + pa + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")
    sleep(1)

file.close()

if (tags[1].find('td').text) == 'Adams' and (tags[64].find('td').text.strip()) == 'York':
    print("Pennsylvania scraper is complete.")
else:
    print("ERROR: Must fix Pennsylvania scraper.")



