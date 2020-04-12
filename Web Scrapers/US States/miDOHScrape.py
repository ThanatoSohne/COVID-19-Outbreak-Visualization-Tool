from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import geocoder

miDOH = 'https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html'

miClient = req(miDOH)

site_parse = soup(miClient.read(), "lxml")
miClient.close()

tables = site_parse.find("div", {"class": "fullContent"}).find("tbody")

tags = tables.findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
mi = "MICHIGAN"
co = ' County'

csvfile = "COVID-19_cases_midoh.csv"
headers = "County, State, Latitude, Longitude, Cases, Deaths \n"

if (tags[0].find('td').text.strip()) == 'Allegan' and (tags[78].find('td').text.strip()) == 'Out of State':

    file = open(csvfile, "w")
    file.write(headers)
    
    for tag in tags[0:75]:
        pull = tag.findAll('td')
        #locale = liegen.geocode(pull[0].text + co + ", " + mi)
        #catch_TimeOut(pull[0].text + co + ", " + mi)
        file.write(pull[0].text + ", " + mi + ", " 
                   + str(geocoder.opencage(pull[0].text + co + ", " + mi, key='').latlng).strip('[]') 
                   + ", " + pull[1].text + ", " + pull[2].text + "\n")
        #sleep(1)
    
    file.write(tags[75].find('td').text.strip() + ", " + mi + ", " + str(liegen.geocode(mi).latitude) + ", " 
               + str(liegen.geocode(mi).longitude) + ", " + tags[75].findAll('td')[1].text.strip() + ", " 
               + tags[75].findAll('td')[2].text.strip() + "\n")
    sleep(1)
    file.write(tags[76].find('td').text.strip() + ", " + mi + ", " + str(liegen.geocode(mi).latitude) + ", " 
               + str(liegen.geocode(mi).longitude) + ", " + tags[76].findAll('td')[1].text.strip() + ", " 
               + tags[76].findAll('td')[2].text.strip() + "\n")
    sleep(1)
    file.write(tags[77].find('td').text.strip() + ", " + mi + ", " + str(liegen.geocode(mi).latitude) + ", " 
               + str(liegen.geocode(mi).longitude) + ", " + tags[77].findAll('td')[1].text.strip() + ", " 
               + tags[77].findAll('td')[2].text.strip() + "\n")
    sleep(1)
    file.write(tags[78].find('td').text.strip() + ", " + mi + ", " + str(liegen.geocode(mi).latitude) + ", " 
               + str(liegen.geocode(mi).longitude) + ", " + tags[78].findAll('td')[1].text.strip() + ", " 
               + tags[78].findAll('td')[2].text.strip() + "\n")
    
    file.close()

    print("Michigan scraper is complete.")
else:
    print("ERROR: Must fix Michigan scraper.")