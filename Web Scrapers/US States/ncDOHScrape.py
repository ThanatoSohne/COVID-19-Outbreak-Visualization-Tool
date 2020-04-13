from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import addfips

ncDOH = 'https://www.ncdhhs.gov/covid-19-case-count-nc#nc-counties-with-cases'

ncClient = req(ncDOH)

site_parse = soup(ncClient.read(), 'lxml')
ncClient.close()

tables = site_parse.find("div", {"class": "content band-content landing-wrapper"}).find('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
nc = "NORTH CAROLINA"
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_ncdoh.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths \n"

tags = tables.findAll('tr')

if (tags[0].find('td').text) == 'Alamance County' and (tags[90].find('td').text) == 'Yadkin County':

    file = open(csvfile, "w")
    file.write(headers)
    
    for tag in tags:
        pull = tag.findAll('td')
        locale = geocoder.opencage(pull[0].text + ", " + nc, key='')
        file.write(pull[0].text + ", " + nc + ", " + fips.get_county_fips(pull[0].text, state = nc) 
                   + ", " + str(locale.latlng).strip('[]') + ", " 
                   + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()

    print("North Carolina scraper is complete.")
else:
    print("ERROR: Must fix North Carolina scraper.")