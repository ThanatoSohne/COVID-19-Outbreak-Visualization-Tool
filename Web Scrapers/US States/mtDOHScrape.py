from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep
import geocoder
import addfips

mtDOH = 'https://dphhs.mt.gov/publichealth/cdepi/diseases/coronavirusmt/demographics'

mtClient = req(mtDOH)

site_parse = soup(mtClient.read(), "lxml")
mtClient.close()

tables = site_parse.find("div", {"id": "dnn_ctr93751_HtmlModule_lblContent"}).findAll("table")[1].find("tbody")

tags = tables.findAll("tr")

mt = "MONTANA"
co = ' County'
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_mtdoh.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths\n"

if tags[0].find('td').text.split('\n')[0] == 'Beaverhead' and tags[28].find('td').text.split('\n')[0] == 'Total':

    file = open(csvfile, "w")
    file.write(headers)
    
    for t in tags[:28]:
        pull = t.findAll("td")
        locale = geocoder.opencage(pull[0].text.split('\n')[0] + co + ", " + mt, key='')
        file.write(pull[0].text.split('\n')[0] + ", " + mt + ", " 
                   + fips.get_county_fips(pull[0].text.split('\n')[0], state=mt) 
                   + ", " + str(locale.latlng).strip('[]') + ", " 
                   + pull[1].text.replace('&nbsp','') + ", " + pull[2].text.replace('&nbsp','') + "\n")
        
    file.close()
    
    print("Montana scraper is complete.")
else:
    print("ERROR: Must fix Montana scraper.")