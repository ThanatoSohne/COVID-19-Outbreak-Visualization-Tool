from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep
import geocoder

mtDOH = 'https://dphhs.mt.gov/publichealth/cdepi/diseases/coronavirusmt/demographics'

mtClient = req(mtDOH)

site_parse = soup(mtClient.read(), "lxml")
mtClient.close()

tables = site_parse.find("div", {"id": "dnn_ctr93751_HtmlModule_lblContent"}).findAll("table")[1].find("tbody")

tags = tables.findAll("tr")

mt = "MONTANA"
co = ' County'

csvfile = "COVID-19_cases_mtdoh.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths \n"

if tags[0].find('td').text == 'Beaverhead' and tags[28].find('td').text == 'Total':

    file = open(csvfile, "w")
    file.write(headers)
    
    for t in tags[:28]:
        pull = t.findAll("td")
        locale = geocoder.opencage(pull[0].text + co + ", " + mt, key='')
        file.write(pull[0].text + ", " + mt + ", " + str(locale.latlng).strip('[]') + ", " 
                       + pull[1].text.replace('&nbsp','') + ", " + pull[2].text.replace('&nbsp','') + "\n")
        
    file.close()
    
    print("Montana scraper is complete.")
else:
    print("ERROR: Must fix Montana scraper.")