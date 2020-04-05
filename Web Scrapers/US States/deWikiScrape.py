from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

dedoh = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Delaware'

deClient = req(dedoh)

site_parse = soup(deClient.read(), 'lxml')
deClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).findAll('tbody')[3]

pull = tables.findAll('td')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
de = "DELAWARE"

csvfile = "COVID-19_cases_deWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

kent = pull[0].text.strip() + " County"
kentC = pull[1].text.strip()
kLocale = liegen.geocode(kent + ", " + de)
newCastle = pull[2].text.strip() + " County"
newC = pull[3].text.strip()
nLocale = liegen.geocode(newCastle + ", " + de)
suss = pull[4].text.strip() + " County"
sussC = pull[5].text.strip() 
sLocale = liegen.geocode(suss + ", " + de)


file.write(kent + ", "+ de + ", " + str(kLocale.latitude) + ", " + str(kLocale.longitude) + ", " + kentC + "\n")
sleep(1)
file.write(newCastle + ", "+ de + ", " + str(nLocale.latitude) + ", " + str(nLocale.longitude) + ", " + newC + "\n")
sleep(1)
file.write(suss + ", "+ de + ", " + str(sLocale.latitude) + ", " + str(sLocale.longitude) + ", " + sussC + "\n")
sleep(1)

file.close()

if kent == 'Kent County' and suss == 'Sussex County':
    print("Delaware scraper is complete.\n")
else:
    print("ERROR: Must fix Delaware scraper\n")





