from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

nvNews = 'https://www.livescience.com/nevada-coronavirus-updates.html'

nvClient = req(nvNews)

site_parse = soup(nvClient.read(), "lxml")
nvClient.close()

tables = site_parse.find("div", {"itemprop": "articleBody"}).find('ul')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
nv = "NEVADA"
co = ' County'

csvfile = "COVID-19_cases_nvNews.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('li')

for t in range(0,10):
    locale = liegen.geocode(tags[t].get_text().split(': ')[0] + co + ", " + nv)
    sleep(1)
    file.write(tags[t].get_text().split(': ')[0] + ", " + nv + ", " 
                + str(locale.latitude) + ", " + str(locale.longitude) + ", "
                + tags[t].get_text().split(': ')[1].replace(',','') + "\n")

file.close()
     
if (tags[0].get_text().split(': ')[0]) == 'Clark' and (tags[9].get_text().split(': ')[0]) == 'White Pine':
    print("Nevada scraper is complete.\n")
else:
    print("ERROR: Must fix Nevada scraper.\n")

