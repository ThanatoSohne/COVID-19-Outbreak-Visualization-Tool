from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

nmDOH = 'https://cv.nmhealth.org/cases-by-county/'

nmClient = req(nmDOH)

site_parse = soup(nmClient.read(), "lxml")
nmClient.close()

tables = site_parse.find("div", {"class": "et_pb_section et_pb_section_2 et_pb_with_background et_section_regular"}).find("tbody")

tags = tables.findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
nm = "NEW MEXICO"
co = ' County'

csvfile = "COVID-19_cases_nmdoh.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[1:]:
    pull = tag.findAll('td')
    locale = liegen.geocode(pull[0].text + ", " + nm)
    file.write(pull[0].text + ", " + nm + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")
    sleep(2)

file.close()
    
if (tags[1].find('td').text) == 'Bernalillo County' and (tags[33].find('td').text) == 'Valencia County':
    print("New Mexico scraper is complete.")
else:
    print("ERROR: Must fix New Mexico scraper.")

