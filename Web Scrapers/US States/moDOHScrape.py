from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep
import geocoder

moDOH = 'https://health.mo.gov/living/healthcondiseases/communicable/novel-coronavirus/results.php'

moClient = req(moDOH)

site_parse = soup(moClient.read(), "lxml")
moClient.close()

tables = site_parse.find("div", {"class": "panel-group"}).findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
mo = "MISSOURI"
co = ' County'

csvfile = "COVID-19_cases_modoh.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths\n"

if (tables[1].find('td').text) == 'Adair' and (tables[134].find('td').text) == 'TBD':

    file = open(csvfile, "w")
    file.write(headers)
    
    #Pull from the county case table
    for t in tables[1:92]:
        pull = t.findAll('td')
        locale = geocoder.opencage(pull[0].text + co + ", " + mo, key='')
        #locale = liegen.geocode(pull[0].text + co + ", " + mo)
        #catch_TimeOut(pull[0].text + co + ", " + mo)
        file.write(pull[0].text + ", " + mo + ", " + str(locale.latlng).strip('[]')
                    + ", " + pull[1].text + "\n")
        
    file.write(tables[92].findAll('td')[0].text + ", " + mo + ", " + str(geocoder.opencage(mo, key='').latlng).strip('[]')
               + ", " + tables[92].findAll('td')[1].text + "\n")
    
    #Pull from the county death table
    for t in tables[110:134]:
        pull = t.findAll('td')
        locale = geocoder.opencage(pull[0].text + co + ", " + mo, key='')
        #locale = liegen.geocode(pull[0].text + co + ", " + mo)
        #catch_TimeOut(pull[0].text + co + ", " + mo)
        file.write(pull[0].text + ", " + mo + ", " + str(locale.latlng).strip('[]')
                   + ", " + "" + ", " + pull[1].text + "\n")
        
    file.write(tables[134].findAll('td')[0].text + ", " + mo + ", " + str(geocoder.opencage(mo, key='').latlng).strip('[]')
               + ", " + "" + ", " + tables[134].findAll('td')[1].text + "\n")
    
    file.close()

    print("Missouri scraper is complete.")
else:
    print("ERROR: Must fix Missouri scraper.")