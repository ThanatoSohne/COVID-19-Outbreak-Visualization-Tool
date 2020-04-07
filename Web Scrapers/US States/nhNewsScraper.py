from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

nhNews = 'https://www.livescience.com/new-hampshire-coronavirus-updates.html'

nhClient = req(nhNews)

site_parse = soup(nhClient.read(), "lxml")
nhClient.close()

tables = site_parse.find("article", {"class":"news-article"}).find("div", {"itemprop": "articleBody"}).find('ul')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
nh = "NEW HAMPSHIRE"
co = ' County'

csvfile = "COVID-19_cases_nhNews.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('li')

for t in range(0,10):
    locale = liegen.geocode(tags[1].get_text().split(': ')[0])
    file.write(tags[t].get_text().split(': ')[0] + ", " + nh + ", " + str(locale.latitude) 
                + ", " + str(locale.longitude) + ", " + tags[t].get_text().split(': ')[1] + "\n")
    sleep(1)

file.close()
     
if (tags[0].get_text().split(': ')[0]) == 'Hillsborough' and (tags[9].get_text().split(': ')[0]) == 'Coos':
    print("New Hampshire scraper is complete.")
else:
    print("ERROR: Must fix New Hampshire scraper.")



