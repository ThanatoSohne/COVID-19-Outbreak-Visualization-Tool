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

hold = []

for t in tables:
    pull = t.findAll('tr')
    for p in pull[2:]:
        take = p.get_text()
        hold.append(take)

if (hold[67].split('\n')[1]) == 'Adams' and (hold[152].split('\n')[1]) == 'Woodford':

    file = open(csvfile, "w")
    file.write(headers)
                
    for h in hold[67:153]:
        #locale = liegen.geocode((h.split('\n')[1]+co) + ", " + il)
        #catch_TimeOut((h.split('\n')[1]+co) + ", " + il)
        take = h.split('\n')
        file.write(take[1] + ", " + il + ", " 
                   + str(geocoder.opencage(h.split('\n')[1] + co + ", " + il, key='').latlng).strip('[]') 
                   + ", " + take[9].replace(',','') + ", " 
                   + take[5].replace(',','') + ", " + take[7].replace(',','') + ", " 
                   + "" + ", " + "" + ", " + take[3].replace(',','') + "\n")
        #sleep(1)
    
    file.write(hold[153].split('\n')[1] + ", " + il + ", " + str(liegen.geocode(il).latitude) + ", "
                   + str(liegen.geocode(il).longitude) + ", " + hold[153].split('\n')[9] + ", " + hold[153].split('\n')[5] + ", " 
                   + hold[153].split('\n')[7] + ", " + "" + ", " + "" + ", "
                   + hold[153].split('\n')[3] + "\n")
    
    file.close()
    
    print("Illinois scraper is complete.")
else:
    print("ERROR: Must fix Illinois scraper.")
