from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep

ilWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Illinois'

ilClient = req(ilWiki)

site_parse = soup(ilClient.read(), "lxml")
ilClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
il = "ILLINOIS"
co = ' County'

csvfile = "COVID-19_cases_ilWiki.csv"
headers = "County, State, Latitude, Longitude, Active Cases, Deaths, Recoveries, Total Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)
            
for h in hold[63:136]:
    locale = liegen.geocode((h.split('\n')[1]+co) + ", " + il)
    take = h.split('\n')
    #print(take[1], take[3], take[5], take[7], take[9])
    file.write(take[1] + ", " + il + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + take[3].replace(',','') + ", " 
               + take[5].replace(',','') + ", " + take[7].replace(',','') + ", " 
               + take[9].replace(',','') + "\n")
    sleep(1)

file.write(hold[136].split('\n')[1] + ", " + il + ", " + "" + ", "
               + "" + ", " + hold[120].split('\n')[3] + ", " + hold[120].split('\n')[5] + ", " 
               + hold[120].split('\n')[7] + ", " + hold[120].split('\n')[9] + "\n")

file.close()
    
if (hold[63].split('\n')[1]) == 'Adams' and (hold[135].split('\n')[1]) == 'Woodford':
    print("Illinois scraper is complete.\n")
else:
    print("ERROR: Must fix Illinois scraper.\n")
