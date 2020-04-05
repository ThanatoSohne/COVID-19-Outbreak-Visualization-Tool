from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

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

file = open(csvfile, "w")
file.write(headers)

for tag in tags[:70]:
    pull = tag.findAll('td')
    locale = liegen.geocode(pull[0].text + co + ", " + mi)
    sleep(1)
    file.write(pull[0].text + ", " + mi + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.write(tags[70].find('td').text.strip() + ", " + mi + ", " + "" + ", " 
           + "" + ", " + tags[70].findAll('td')[1].text.strip() + ", " 
           + tags[70].findAll('td')[2].text.strip() + "\n")

file.write(tags[71].find('td').text.strip() + ", " + mi + ", " + "" + ", " 
           + "" + ", " + tags[71].findAll('td')[1].text.strip() + ", " 
           + tags[71].findAll('td')[2].text.strip() + "\n")

file.write(tags[72].find('td').text.strip() + ", " + mi + ", " + "" + ", " 
           + "" + ", " + tags[72].findAll('td')[1].text.strip() + ", " 
           + tags[72].findAll('td')[2].text.strip() + "\n")

file.close()

if (tags[0].find('td').text.strip()) == 'Allegan' and (tags[72].find('td').text.strip()) == 'Out of State':
    print("Michigan scraper is complete.")
else:
    print("ERROR: Must fix Michigan scraper.")