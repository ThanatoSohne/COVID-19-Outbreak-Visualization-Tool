from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

tndoh = 'https://www.tn.gov/health/cedep/ncov.html'

tnClient = req(tndoh)

site_parse = soup(tnClient.read(), 'lxml')
tnClient.close()

tables = site_parse.find("div", {"class": "containers tn-accordion parbase"}).find("div", {"class": "tn-simpletable parbase"})

colTable = site_parse.find("div", {"class": "row parsys_column tn-3cols"}).findAll("div", {"class": "tn-simpletable parbase"})[2]

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
tn = "TENNESSEE"

fatal = colTable.find('tr')
fa = fatal.get_text().split('\n')
faStr = fa[0]
faNo = fa[1]

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_tndoh.csv"
headers = "County, State, Latitude, Longitude, Positive Cases \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[1:96]:
    pull = tag.findAll('p')
    locale = liegen.geocode(pull[0].text + ", " + tn)
    file.write(pull[0].text + ", " + tn + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + pull[1].text.replace(',','') + "\n")
    sleep(1)
    
file.write(tags[96].find('p').text + ", " + "" + ", " + "" + ", " 
           + tags[96].findAll('p')[1].text.replace(',','') + "\n")

file.write(tags[97].find('p').text + ", " + "" + ", " + "" + ", " 
           + tags[97].findAll('p')[1].text.replace(',','') + "\n")

file.write("\n")
file.write(faStr + ", " + faNo + "\n")

file.close()

if (tags[1].find('p').text) == 'Anderson County' and (tags[97].find('p').text) == 'Out of state':
    print("Tennessee scraper is complete.")
else:
    print("ERROR: Must fix Tennessee scraper.")





