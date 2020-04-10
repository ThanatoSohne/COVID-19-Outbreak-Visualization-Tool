from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep

mtNews = 'https://www.livescience.com/montana-coronavirus-updates.html'

mtClient = req(mtNews)

site_parse = soup(mtClient.read(), "lxml")
mtClient.close()

tables = site_parse.find("div", {"id" : "article-body"}).find('ul')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
mt = "MONTANA"
co = ' County'

csvfile = "COVID-19_cases_mtNews.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('li')

for t in tags:
    pull = t.get_text().split(": ")
    locale = liegen.geocode(pull[0] + co + ", " + mt)
    file.write(pull[0] + ", " + mt + ", " + str(locale.latitude) + ", " + str(locale.longitude) + ", " + pull[1] + "\n")
    sleep(1.1)

file.close()

if (tags[0].get_text().split(": ")[0]) == 'Gallatin' and (tags[24].get_text().split(": ")[0]) == 'Glacier':
    print("Montana scraper is complete.")
else:
    print("ERROR: Must fix Montana scraper.")