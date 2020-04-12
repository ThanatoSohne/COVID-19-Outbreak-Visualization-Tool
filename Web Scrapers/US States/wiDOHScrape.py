import json
from urllib.request import urlopen as req
from geopy import Nominatim
from time import sleep

widoh = 'https://services1.arcgis.com/ISZ89Z51ft1G16OK/arcgis/rest/services/COVID19_WI/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=NAME%2CPOSITIVE%2CDEATHS%2CDATE&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=NAME+ASC&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token='

wiClient = req(widoh).read().decode('utf-8')

wiJS = json.loads(wiClient)

attr = wiJS.get('features')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
wi = "WISCONSIN"
co = ' County'

csvfile = "COVID-19_cases_widoh.csv"
headers = "County, State, Latitude, Longitude, Positive Cases, Deaths \n"

if attr[0].get('attributes').get('NAME') == 'Adams' and attr[71].get('attributes').get('NAME') == 'Wood':
 
    file = open(csvfile, "w")
    file.write(headers)
    
    for a in attr:
        file.write(a.get('attributes').get('NAME') + ", " + wi + ", " 
                       + str(geocoder.opencage(a.get('attributes').get('NAME') + co + ", " + wi, key='').latlng).strip('[]') + ", " 
                       + str(a.get('attributes').get('POSITIVE')) + ", " + str(a.get('attributes').get('DEATHS')) + "\n")
        #catch_TimeOut(a.get('attributes').get('NAME') + co + ", " + wi)
        
    
    file.close()

    print("Wisconsin scraper is complete.")
else:
    print("ERROR: Must fix Wisconsin scraper.")