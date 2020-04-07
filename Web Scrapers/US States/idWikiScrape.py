from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup 
from geopy import Nominatim
from time import sleep

idWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Idaho'

idClient = req(idWiki)

site_parse = soup(idClient.read(), "lxml")

idClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
iD = "IDAHO"
co = ' County'

csvfile = "COVID-19_cases_idWiki.csv"
headers = "County, State, Latitude, Longitude, Active Cases, Deaths, Recoveries, Total Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)
            
for h in hold[33:58]:
    locale = liegen.geocode((h.split('\n')[1] + co) + ", " + iD)
    take = h.split('\n')
    #print(take[1], take[3], take[5], take[7], take[9])
    file.write(take[1] + ", " + iD + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + take[3] + ", " + take[5] + ", "
               + take[7] + ", " + take[9] + "\n")
    sleep(1)

file.close()
    
if (hold[33].split('\n')[1]) == 'Ada' and (hold[57].split('\n')[1]) == 'Valley':
    print("Idaho scraper is complete.\n")
else:
    print("ERROR: Must fix Idaho scraper.\n")


