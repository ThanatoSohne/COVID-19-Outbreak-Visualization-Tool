from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep

azWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Arizona'

azClient = req(azWiki)

site_parse = soup(azClient.read(), "lxml")
azClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
az = "ARIZONA"

csvfile = "COVID-19_cases_azWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths\n"

hold = []

for t in tables:
    pull = t.findAll('tr')
    for p in pull:
        take = p.get_text()
        hold.append(take)

if (hold[49].split('\n')[1]) == 'Apache' and (hold[63].split('\n')[1]) == 'Yuma':

    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[49:64]:
        locale = liegen.geocode(h.split('\n')[1] + ", " + az)
        catch_TimeOut(h.split('\n')[1] + ", " + az)
        take = h.split('\n')
        file.write(take[1] + ", " + az + ", " + str(locale.latitude) + ", " + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
        sleep(1)
    
    #file.write(hold[61].split('\n')[1] + ", " + az + ", " + "" + ", " + ""+ ", "+ hold[61].split('\n')[3] + ", " + hold[61].split('\n')[5] + "\n" )
    
    file.close()
    print("Arizona scraper is complete.")
else:
    print("ERROR: Must fix Arizona scraper.")