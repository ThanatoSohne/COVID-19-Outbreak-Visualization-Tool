import json
from urllib.request import urlopen as req
#from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep

aldoh = 'https://services7.arcgis.com/4RQmZZ0yaZkGR1zy/arcgis/rest/services/COV19_Public_Dashboard_ReadOnly/FeatureServer/0/query?where=1%3D1&outFields=CNTYNAME%2CCNTYFIPS%2CCONFIRMED%2CDIED&returnGeometry=false&f=pjson'

alClient = req(aldoh).read().decode('utf-8')

rJS = json.loads(alClient)

attr = rJS.get('features')

csvfile = "COVID-19_cases_aldoh.csv"
headers = "County/Region, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

test = []

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

file = open(csvfile, "w")
file.write(headers)

for a in attr:
    file.write(a.get('attributes').get('CNTYNAME') + ", " + "ALABAMA" + ", " 
               + str(liegen.geocode(a.get('attributes').get('CNTYNAME') + " ALABAMA").latitude) + ", " 
               + str(liegen.geocode(a.get('attributes').get('CNTYNAME') + " ALABAMA").longitude) + ", "
               + str(a.get('attributes').get('CONFIRMED')) + ", " + str(a.get('attributes').get('DIED')) + "\n")
    sleep(1.5)
    
    if(attr[0].get('attributes').get('CNTYNAME')) == 'Autauga':
        test = True
    else:
        test = False

#for tag in tags[2:23]:
#    pull = tag.findAll('p')
#    print("County = %s, Positive Cases = %s" % (pull[0].text, pull[1].text))
#    
#    file.write(pull[0].text + ", " + pull[1].text + "\n")
#
file.close()

if test == True:
    print("Alabama scraper is complete.\n")
else:
    print("Must fix Alabama scraper.\n")