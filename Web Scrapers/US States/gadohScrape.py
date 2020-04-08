from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

gadoh = 'https://d20s4vd27d0hk0.cloudfront.net/?initialWidth=616&childId=covid19dashdph&parentTitle=COVID-19%20Daily%20Status%20Report%20%7C%20Georgia%20Department%20of%20Public%20Health&parentUrl=https%3A%2F%2Fdph.georgia.gov%2Fcovid-19-daily-status-report'

gaClient = req(gadoh)

site_parse = soup(gaClient.read(), 'lxml')
gaClient.close()

tables = site_parse.find("div", {"id": "summary"}).findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ga = "GEORGIA"

csvfile = "COVID-19_cases_gadoh.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for t in tables[5:159]:
        pull = t.findAll('td')
        locale = liegen.geocode(pull[0].text +  " County" + ", " + ga )
        file.write(pull[0].text + ", "+ ga + ", " + str(locale.latitude) + ", " 
                   + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")
        sleep(1)

file.write(tables[159].find('td').text + ", "+ ga + ", " + "" + ", " 
                   + "" + ", " + tables[152].findAll('td')[1].text.strip() 
                   + ", " + tables[152].findAll('td')[2].text.strip() + "\n")

file.close()

if (tables[5].find('td').text) == 'Fulton' and (tables[159].find('td').text) == 'Unknown':
    print("Georgia scraper is complete.\n")
else:
    print("ERROR: Must fix Georgia scraper.\n")