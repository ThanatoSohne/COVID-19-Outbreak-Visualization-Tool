from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import addfips
import geocoder

gadoh = 'https://d20s4vd27d0hk0.cloudfront.net/?initialWidth=616&childId=covid19dashdph&parentTitle=COVID-19%20Daily%20Status%20Report%20%7C%20Georgia%20Department%20of%20Public%20Health&parentUrl=https%3A%2F%2Fdph.georgia.gov%2Fcovid-19-daily-status-report'

gaClient = req(gadoh)

site_parse = soup(gaClient.read(), 'lxml')
gaClient.close()

tables = site_parse.find("div", {"id": "summary"}).findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ga = "GEORGIA"
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_gadoh.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths\n"

if (tables[5].find('td').text) == 'Fulton' and (tables[162].find('td').text) == 'Unknown':

    file = open(csvfile, "w")
    file.write(headers)
    
    for t in tables[5:162]:
            pull = t.findAll('td')
            file.write(pull[0].text + ", "+ ga + ", " + fips.get_county_fips(pull[0].text, state = ga) + ", "
                       + str(geocoder.opencage(pull[0].text + " County" + ", " + ga, key='').latlng).strip('[]')
                       + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.write(tables[162].find('td').text + ", "+ ga + ", " + fips.get_state_fips(ga) 
               + ", " + str(liegen.geocode(ga).latitude) + ", " 
               + str(liegen.geocode(ga).longitude) + ", " + tables[162].findAll('td')[1].text.strip() 
               + ", " + tables[162].findAll('td')[2].text.strip() + "\n")
    
    file.close()

    print("Georgia scraper is complete.")
else:
    print("ERROR: Must fix Georgia scraper.")