import json
from urllib.request import urlopen as req
from geopy.geocoders import Nominatim
from time import sleep
import addfips

aldoh = 'https://services7.arcgis.com/4RQmZZ0yaZkGR1zy/arcgis/rest/services/COV19_Public_Dashboard_ReadOnly/FeatureServer/0/query?where=1%3D1&outFields=CNTYNAME%2CCNTYFIPS%2CCONFIRMED%2CDIED&returnGeometry=false&f=pjson'

alClient = req(aldoh).read().decode('utf-8')

rJS = json.loads(alClient)

attr = rJS.get('features')

csvfile = "COVID-19_cases_aldoh.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths\n"
al = "ALABAMA"
fips = addfips.AddFIPS()

test = []

if(attr[0].get('attributes').get('CNTYNAME')) == 'Autauga':
    test = True
else:
    test = False

if test == True:

    file = open(csvfile, "w")
    file.write(headers)
    
    for a in attr:
        file.write(a.get('attributes').get('CNTYNAME') + ", " + "ALABAMA" + ", " + fips.get_county_fips(a.get('attributes').get('CNTYNAME'), state=al) + ", "
                   + str(geocoder.opencage(a.get('attributes').get('CNTYNAME') + " ALABAMA", key='').latlng).strip('[]') + ", " 
                   + str(a.get('attributes').get('CONFIRMED')) + ", " + str(a.get('attributes').get('DIED')) + "\n")
    
    file.close()
    print("Alabama scraper is complete.")
else:
    print("Must fix Alabama scraper.")