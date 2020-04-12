from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep
import geocoder 

arWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Arkansas'

arClient = req(arWiki)

site_parse = soup(arClient.read(), "lxml")
arClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_arWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

hold = []
    
for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[52].split('\n')[1]) == 'Arkansas' and (hold[122].split('\n')[1]) == 'Missing county information':
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for h in hold[51:122]:
        #locale = liegen.geocode(h.split('\n')[1] + ", " + "ARKANSAS")
        #catch_TimeOut(h.split('\n')[1] + ", " + "ARKANSAS")
        take = h.split('\n')
        file.write(take[1] + ", " + "ARKANSAS" + ", " 
                   + str(geocoder.opencage(h.split('\n')[1] + ", " + "ARKANSAS", key='').latlng).strip('[]') 
                   +  ", " + take[3] + ", " + take[5] + ", " + take[7] +"\n")
        #sleep(1)
    
    file.write(hold[122].split('\n')[1] + ", " + "ARKANSAS" +  ", "  
               + str(geocoder.opencage("ARKANSAS", key='').latlng).strip('[]') 
               +", "+ hold[122].split('\n')[3] + ", " + hold[122].split('\n')[5] + ", " + hold[122].split('\n')[7] +"\n")
        
    file.close()

else:
    print("ERROR: Must fix Arkansas scraper.")
    