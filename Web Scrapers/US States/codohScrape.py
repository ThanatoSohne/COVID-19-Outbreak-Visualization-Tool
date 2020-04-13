from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import addfips
import geocoder

codoh = 'https://covid19.colorado.gov/case-data'

coClient = req(codoh)

site_parse = soup(coClient.read(), 'lxml')
coClient.close()

tables = site_parse.findAll("div", {"class": "field field--name-field-card-body field--type-text-long field--label-hidden field--item"})[1]

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
co = "COLORADO"
fips = addfips.AddFIPS()

test = tables.findAll('tr')

adamsTest = test[1].find('td').text
outTest = test[58].find('td').text

csvfile = "COVID-19_cases_coDOH.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths\n"

if adamsTest == 'Adams' and outTest == 'Out of state':

    file = open(csvfile, "w")
    file.write(headers)
    
    for t in test[1:57]:
            pull = t.findAll('td')
            file.write(pull[0].text + ", " + co + ", " + fips.get_county_fips(pull[0].text, state = co) + ", "
                       + str(geocoder.opencage(test[1].find('td').text + ", " + co, key='').latlng).strip('[]') 
                       + ", " + pull[1].text + 
                       ", " + pull[2].text + "\n")
    
    file.write(test[57].find('td').text + ", " + co + ", " + fips.get_state_fips(co) + ", " 
               + str(liegen.geocode(co).latitude) + ", " + str(liegen.geocode(co).longitude) + ", " +
               test[57].findAll('td')[1].text.strip()+", " +test[57].findAll('td')[2].text.strip()+ "\n")
    
    file.write(test[58].find('td').text + ", " + co + ", " + fips.get_state_fips(co) + ", " 
               + str(liegen.geocode(co).longitude) + ", " + str(liegen.geocode(co).longitude) + ", " +
               test[58].findAll('td')[1].text.strip()+", " +test[58].findAll('td')[2].text.strip()+ "\n")
    
    file.close()
    print("Colorado scraper is complete.")
else:
    print("ERROR: Must fix Colorado scraper.")

