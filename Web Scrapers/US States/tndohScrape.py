from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

tndoh = 'https://www.tn.gov/health/cedep/ncov.html'

tnClient = req(tndoh)

site_parse = soup(tnClient.read(), 'lxml')
tnClient.close()

tables = site_parse.findAll("div", {"class": "tn-simpletable parbase"})[8].find('tbody')   
colTable = site_parse.find("div", {"class": "fifth-color bgimg"}).findAll("div", {"class": "tn-simpletable parbase"})

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
tn = "TENNESSEE"

#Fatalities 
faNo = colTable[1].find('tr').find('td').text
#Recoveries
recNo = colTable[3].find('tr').find('td').text
#Hospitalizations
hosNo = colTable[5].find('tr').find('td').text

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_tndoh.csv"
headers = "County, State, Latitude, Longitude, Positive Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[1:96]:
    pull = tag.findAll('p')
    locale = liegen.geocode(pull[0].text + ", " + tn)
    file.write(pull[0].text + ", " + tn + ", " + str(locale.latitude) 
               + ", " +  str(locale.longitude) + ", " + pull[1].text + ", " 
               + pull[3].text.replace('\xa0','0') + "\n")
    sleep(1)
    
file.write(tags[96].find('p').text + ", " + tn + ", " + "" + ", " + "" + ", "
           + tags[96].findAll('p')[1].text.replace(',','') + ", " + 
           tags[96].findAll('p')[3].text.replace(',','').replace('\xa0', '0') + "\n")

file.write(tags[97].find('p').text + ", " + tn + ", " + "" + ", " + "" + ", "
           + tags[97].findAll('p')[1].text.replace(',','') + ", " + 
           tags[97].findAll('p')[3].text.replace(',','').replace('\xa0', '0') + "\n")

file.write(tn + ", " + tn + ", " + str(liegen.geocode(tn).latitude) + ", " 
           + str(liegen.geocode(tn).longitude) + ", " + "" + ", " + "" 
           + recNo + ", " + "" + ", " + hosNo + "\n")


file.close()

if (tags[1].find('p').text) == 'Anderson County' and (tags[96].find('p').text) == 'Out of State':
    print("Tennessee scraper is complete.")
else:
    print("ERROR: Must fix Tennessee scraper.")




