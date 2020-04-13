from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from time import sleep
import geocoder
import addfips

def catch_TimeOut(locale):
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    try:
        return liegen.geocode(locale)
    except GeocoderTimedOut:
        return catch_TimeOut(locale)

flWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Florida'

flClient = req(flWiki)

site_parse = soup(flClient.read(), "lxml")
flClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_flWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths,,,Hospitalizations \n"

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

fl = "FLORIDA"
co = ' County'
fips = addfips.AddFIPS()

hold = []

for t in tables:
    pull = t.findAll('tr')
    for p in pull:
        take = p.get_text()
        hold.append(take)

if (hold[58].split('\n')[1]) == 'Alachua' and (hold[124].split('\n')[1]) == 'Washington':

    file = open(csvfile, "w")
    file.write(headers)
        
    for h in hold[58:125]:
        take = h.split('\n')
        file.write(take[1] + ", " + fl + ", " + fips.get_county_fips(take[1], state = fl) + ", "
                   + str(geocoder.opencage(h.split('\n')[1] + ", " + fl, key='').latlng).strip('[]') 
                   + ", " + take[3] + ", " + take[7] + ", " 
                   + "" + ", " + "" + ", " + take[5] +"\n")
    file.write(hold[125].split('\n')[1] + ", " + fl + ", " + fips.get_state_fips(fl) 
               + ", " + str(liegen.geocode(fl).latitude) + ", " 
               + str(liegen.geocode(fl).longitude) + ", " + hold[125].split('\n')[3] 
               + ", " + hold[125].split('\n')[7] + ", " + "" + ", " + "" 
               + ", " + hold[125].split('\n')[5] +"\n")
    
    file.close()

    print("Florida scraper is complete.")
else:
    print("ERROR: Must fix Florida scraper.")