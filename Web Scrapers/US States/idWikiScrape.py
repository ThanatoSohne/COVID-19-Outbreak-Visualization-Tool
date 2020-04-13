from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup 
from geopy import Nominatim
from time import sleep
import addfips

idWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Idaho'

idClient = req(idWiki)

site_parse = soup(idClient.read(), "lxml")

idClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
iD = "IDAHO"
co = ' County'

csvfile = "COVID-19_cases_idWiki.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths\n"

hold = []

for t in tables:
    pull = t.findAll('tr')
    for p in pull[2:]:
        take = p.get_text()
        hold.append(take)

if (hold[42].split('\n')[1]) == 'Ada' and (hold[73].split('\n')[1]) == 'Washington':

    file = open(csvfile, "w")
    file.write(headers)
                
    for h in hold[42:74]:
        locale = liegen.geocode((h.split('\n')[1] + co) + ", " + iD)
        catch_TimeOut((h.split('\n')[1] + co) + ", " + iD)
        take = h.split('\n')
        file.write(take[1] + ", " + iD + ", " + fips.get_county_fips(take[1],state=iD) + ", " 
                   + str(locale.latitude) + ", " + str(locale.longitude) + ", " + take[3] + ", "
                   + take[7] + "\n")
        sleep(1.1)
    
    file.close()

    print("Idaho scraper is complete.")
else:
    print("ERROR: Must fix Idaho scraper.")


