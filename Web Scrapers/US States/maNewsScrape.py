from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import addfips

maNews = 'https://www.livescience.com/massachusetts-coronavirus-updates.html'

maClient = req(maNews)

site_parse = soup(maClient.read(), "lxml")
maClient.close()

tables = site_parse.find("div", {"itemprop": "articleBody"}).find('ul')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ma = "MASSACHUSETTS"
co = ' County'
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_maNews.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases\n"

tags = tables.findAll('li')

if (tags[0].get_text().split(': ')[0]) == 'Barnstable' and (tags[14].get_text().split(': ')[0]) == 'Unknown':

    file = open(csvfile, "w")
    file.write(headers)
    
    for t in range(0,14):
        locale = liegen.geocode(tags[t].get_text().split(': ')[0] + co + ", " + ma)
        catch_TimeOut(tags[t].get_text().split(': ')[0] + co + ", " + ma)
        file.write(tags[t].get_text().split(': ')[0] + ", " + ma + ", " + fips.get_county_fips(tags[t].get_text().split(': ')[0],state=ma) 
                   + ", " + str(locale.latitude) + ", " + str(locale.longitude) + ", "
                   + tags[t].get_text().split(': ')[1].replace(',','') + "\n")
        sleep(1)
    
    file.write(tags[14].get_text().split(': ')[0] + ", " + ma + ", " + fips.get_state_fips(ma) + ", " + str(liegen.geocode(ma).latitude) + ", " 
               + str(liegen.geocode(ma).longitude) + ", " + tags[14].get_text().split(': ')[1].replace(',','') + "\n")
    
    file.close()
     
    print("Massachusetts scraper is complete.")
else:
    print("ERROR: Must fix Massachusetts scraper.")