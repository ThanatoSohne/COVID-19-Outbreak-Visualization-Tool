from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

viDOH = 'https://doh.vi.gov/covid19usvi'

viClient = req(viDOH)

site_parse = soup(viClient.read(), "lxml")
viClient.close()

tables = site_parse.find("div", {"class": "field field-name-body field-type-text-with-summary field-label-hidden"}).find("div", {"class":"row"})

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
vi = "US VIRGIN ISLANDS"

csvfile = "COVID-19_cases_vidoh.csv"
headers = "State/Territory, State/Territory, Latitude, Longitude, No. of Cases, Deaths, Recovered, , , , Pending \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('p')

pos = tags[3].text.split(': ')[0]
posNo = tags[3].text.split(': ')[1].split('\xa0')[0]

recov = tags[6].text.split(': ')[0]
recNo = tags[6].text.split(': ')[1].split('/')[0]

pend = tags[5].text.split(': ')[0]
pendNo = tags[5].text.split(': ')[1].split(' ')[0]

mort = tags[7].text.split(':\xa0')[0]
mortNo = tags[7].text.split(':\xa0')[1]

locale = liegen.geocode(vi)
sleep(1)
file.write(vi + ", " + vi + ", " + str(locale.latitude) + ", " 
           + str(locale.longitude) + posNo + ", " + mortNo + ", " 
           + recNo + ", " + "" + ", " + "" + ", " + pendNo + "\n")

file.close()

if (pos == 'Positive') and (pend == 'Pending'):
    print("US Virgin Islands scraper is complete.")
else:
    print("ERROR: Must fix US Virgin Islands scraper.")

