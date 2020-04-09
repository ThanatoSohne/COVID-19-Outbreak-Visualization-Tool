from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from time import sleep

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

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')


csvfile = "COVID-19_cases_flWiki.csv"
headers = "County/Region, State, Latitude, Longitude, Confirmed Cases, Deaths, , , Hospitalizations \n"


fl = "FLORIDA"
co = ' County'

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[56:123]:
    locale = liegen.geocode(h.split('\n')[1] + ", " + fl)
    catch_TimeOut(locale)
    take = h.split('\n')
    file.write(take[1] + ", " + fl + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + take[3] + ", " + take[7] + ", " 
               + "" + ", " + "" + ", " + take[5] +"\n")
    sleep(1)
file.write(hold[123].split('\n')[1] + ", " + fl + ", " + str(liegen.geocode(fl).latitude) + ", " 
           + str(liegen.geocode(fl).longitude) + ", " + hold[123].split('\n')[3] 
           + ", " + hold[123].split('\n')[7] + ", " + "" + ", " + "" 
           + ", " + hold[123].split('\n')[5] +"\n")


file.close()

if (hold[56].split('\n')[1]) == 'Alachua' and (hold[122].split('\n')[1]) == 'Washington':
    print("Florida scraper is complete.")
else:
    print("ERROR: Must fix Florida scraper.")