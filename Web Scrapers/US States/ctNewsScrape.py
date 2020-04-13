from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import addfips
import geocoder

ctNews = 'https://www.nbcconnecticut.com/news/local/this-is-where-there-are-confirmed-cases-of-coronavirus-in-connecticut/2243429/'

bypass = {'User-Agent': 'Mozilla/5.0'}

ctClient = Request(ctNews, headers=bypass)
ctPage = req(ctClient)

site_parse = soup(ctPage.read(), 'lxml')
ctPage.close()

tables = site_parse.find("div", {"class": "article-content rich-text"})

listed = tables.findAll('ul')[0]

tags = listed.findAll('li')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ct = "CONNECTICUT"
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_ctNews.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases\n"

hold = []

for li in tags:
    take = li.get_text()
    hold.append(take)

if hold[0].split('County')[0].strip() == 'Fairfield' and hold[8].split('validation')[0].strip() == 'Pending address':

    file = open(csvfile, "w")
    file.write(headers)
            
    for h in hold[:8]:
        locale = liegen.geocode(h.split('County')[0] + 'County' + ", " + ct)
        file.write(h.split('County')[0] + ", " + ct + ", " 
                   + fips.get_county_fips(h.split('County')[0], state = ct) 
                   + ", " + str(locale.latitude) + ", " + str(locale.longitude) 
                   + ", " + h.split('County')[1].strip().replace(',','') + "\n")
        sleep(1)
        catch_TimeOut((h.split('County')[0] + 'County' + ", " + ct))
    
    file.write('Pending address' + ", " + ct + ", " + fips.get_state_fips(ct) 
                + ", " + str(liegen.geocode(ct).latitude) + ", " 
                + str(liegen.geocode(ct).longitude) + ", " 
                + hold[8].split('validation')[1].strip() + "\n")
    
    file.close()

    print("Connecticut scraper is complete.")
else:
    print("ERROR: Must fix Connecticut scraper.")
    
