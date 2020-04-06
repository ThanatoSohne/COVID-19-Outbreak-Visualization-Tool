from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep

guDOH = 'http://dphss.guam.gov/covid-19/'

guClient = req(guDOH)

site_parse = soup(guClient.read(), "lxml")
guClient.close()

tables = site_parse.find("div", {"class" : "et_pb_row et_pb_row_2"}).findAll('p')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
gu = "GUAM"

csvfile = "COVID-19_cases_guDOH.csv"
headers = "Region, State, Latitude, Longitude, Positive Cases, Deaths, Recoveries \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
    take = t.text
    hold.append(take)

locale = liegen.geocode(gu)
sleep(1)
pos = hold[0]
mort = hold[2]
hope = hold[4]

file.write(gu + ", " + gu + ", " + str(locale.latitude) + ", " 
           + str(locale.longitude) + ", " + pos + ", " + mort + ", " + hope + "\n")

file.close()

if hold[1] == 'POSITIVE':
    print("Guam scraper is complete.")
else:
    print("ERROR: Must fix Guam scraper.")

    
