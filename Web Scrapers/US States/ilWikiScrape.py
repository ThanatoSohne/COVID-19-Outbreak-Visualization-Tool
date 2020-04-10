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
headers = "County, State, Latitude, Longitude, Total Cases, Deaths, Recoveries, Active Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)
            
for h in hold[66:147]:
    locale = liegen.geocode((h.split('\n')[1]+co) + ", " + il)
    take = h.split('\n')
    file.write(take[1] + ", " + il + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + take[9].replace(',','') + ", " 
               + take[5].replace(',','') + ", " + take[7].replace(',','') + ", " 
               + "" + ", " + "" + ", " + take[3].replace(',','') + "\n")
    sleep(1)

file.write(hold[147].split('\n')[1] + ", " + il + ", " + str(liegen.geocode(il).latitude) + ", "
               + str(liegen.geocode(il).longitude) + ", " + hold[147].split('\n')[9] + ", " + hold[147].split('\n')[5] + ", " 
               + hold[147].split('\n')[7] + ", " + "" + ", " + "" + ", "
               + hold[147].split('\n')[3] + "\n")

file.close()
    
if (hold[66].split('\n')[1]) == 'Adams' and (hold[146].split('\n')[1]) == 'Woodford':
    print("Illinois scraper is complete.\n")
else:
    print("ERROR: Must fix Illinois scraper.\n")
