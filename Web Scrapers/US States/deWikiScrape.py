from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import addfips

deWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Delaware'

deClient = req(deWiki)

site_parse = soup(deClient.read(), 'lxml')
deClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).findAll('tbody')[2]

pull = tables.findAll('td')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
de = "DELAWARE"
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_deWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases\n"

kent = pull[2].text.strip() + " County"
kentC = pull[3].text.strip()
kLocale = liegen.geocode(kent + ", " + de)
sleep(1)
newCastle = pull[0].text.strip() + " County"
newC = pull[1].text.strip()
nLocale = liegen.geocode(newCastle + ", " + de)
sleep(1)
suss = pull[4].text.strip() + " County"
sussC = pull[5].text.strip() 
sLocale = liegen.geocode(suss + ", " + de)

if kent == 'Kent County' and suss == 'Sussex County':
 
    file = open(csvfile, "w")
    file.write(headers)
    
    file.write(kent + ", "+ de + ", " + fips.get_county_fips(kent, state = de) + ", " + str(kLocale.latitude) + ", " + str(kLocale.longitude) + ", " + kentC + "\n")
    file.write(newCastle + ", "+ de + ", " + fips.get_county_fips(newCastle, state = de) + ", " + str(nLocale.latitude) + ", " + str(nLocale.longitude) + ", " + newC + "\n")
    file.write(suss + ", "+ de + ", " + fips.get_county_fips(suss, state = de) + ", " + str(sLocale.latitude) + ", " + str(sLocale.longitude) + ", " + sussC + "\n")
    
    file.close()

    print("Delaware scraper is complete.")
else:
    print("ERROR: Must fix Delaware scraper.")





