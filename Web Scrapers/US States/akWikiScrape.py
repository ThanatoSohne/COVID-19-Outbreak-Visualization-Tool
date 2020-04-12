from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep

akWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Alaska'

akClient = req(akWiki)

site_parse = soup(akClient.read(), "lxml")
akClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_akdoh.csv"
headers = "Region, State, Latitude, Longitude, Confirmed Cases \n"

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

ak = "ALASKA"

anch = liegen.geocode("Anchorage, Alaska")
gulf = liegen.geocode("Kenai Peninsula Borough, Alaska")
inter = liegen.geocode("Fairbanks North Star Borough, Alaska")
matsu = liegen.geocode("Matanuska-Susitna Borough, Alaska")
north = liegen.geocode("North Slope Borough, Alaska")
sE = liegen.geocode("Juneau Borough, Alaska")
sW = liegen.geocode("Bethel, Alaska")
    
hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[44].split('\n')[1]) == 'Anchorage/Southcentral Alaska' and (hold[50].split('\n')[1]) == 'Southwest':
    
    file = open(csvfile, "w")
    file.write(headers)
    
    file.write(hold[44].split('\n')[1] + ", " + ak + ", " + str(anch.latitude) + ", " + str(anch.longitude) + ", " + hold[44].split('\n')[3] + "\n")
    sleep(1)
    file.write(hold[45].split('\n')[1] + ", " + ak + ", " + str(gulf.latitude) + ", " + str(gulf.longitude) + ", " + hold[45].split('\n')[3] + "\n")
    sleep(1)
    file.write(hold[46].split('\n')[1] + ", " + ak + ", " + str(inter.latitude) + ", " + str(inter.longitude) + ", " + hold[46].split('\n')[3] + "\n")
    sleep(1)
    file.write(hold[47].split('\n')[1] + ", " + ak + ", " + str(matsu.latitude) + ", " + str(matsu.longitude) + ", " + hold[47].split('\n')[3] + "\n")
    sleep(1)
    file.write(hold[48].split('\n')[1] + ", " + ak + ", " + str(north.latitude) + ", " + str(north.longitude) + ", " + hold[48].split('\n')[3] + "\n")
    sleep(1)
    file.write(hold[49].split('\n')[1] + ", " + ak + ", " + str(sE.latitude) + ", " + str(sE.longitude) + ", " + hold[49].split('\n')[3] + "\n")
    sleep(1)
    file.write(hold[50].split('\n')[1] + ", " + ak + ", " + str(sW.latitude) + ", " + str(sW.longitude) + ", " + hold[50].split('\n')[3] + "\n")
    
    file.close()
    
    print("Alaska scraper complete.")
else:
    print("ERROR: Must fix Alaska scraper.")