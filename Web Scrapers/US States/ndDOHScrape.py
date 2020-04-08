from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

ndDOH = 'https://www.health.nd.gov/diseases-conditions/coronavirus/north-dakota-coronavirus-cases'

ndClient = req(ndDOH)

site_parse = soup(ndClient.read(), "lxml")
ndClient.close()

tables = site_parse.find("div", {"class":"paragraph paragraph--type--bp-accordion-section paragraph--view-mode--default paragraph--id--3613"}).find('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
nd = "NORTH DAKOTA"
co = ' County'

csvfile = "COVID-19_cases_nddoh.csv"
headers = "County, State, Latitude, Longitude, Positive Cases, , , , ,  Total Tests \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('tr')

for tag in tags[:52]:
    pull = tag.findAll('td')
    locale = liegen.geocode(pull[0].text + co + ", " + nd)
    file.write(pull[0].text + ", " + nd + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + pull[2].text + ", " +
               "" + ", " + "" + ", " + "" + ", " + "" + ", " + pull[1].text + "\n")
    sleep(1.2)

file.close()

if (tags[0].find('td').text) == 'Adams' and (tags[51].find('td').text) == 'Williams':
    print("North Dakota scraper is complete.")
else:
    print("ERROR: Must fix North Dakota Scraper.")




