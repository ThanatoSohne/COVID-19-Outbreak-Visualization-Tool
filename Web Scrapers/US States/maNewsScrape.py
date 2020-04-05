from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

maNews = 'https://www.livescience.com/massachusetts-coronavirus-updates.html'

maClient = req(maNews)

site_parse = soup(maClient.read(), "lxml")
maClient.close()

tables = site_parse.find("div", {"itemprop": "articleBody"}).find('ul')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ma = "MASSACHUSETTS"
co = ' County'

csvfile = "COVID-19_cases_maNews.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('li')

for t in range(0,14):
    locale = liegen.geocode(tags[t].get_text().split(': ')[0] + co + ", " + ma)
    sleep(1)
    file.write(tags[t].get_text().split(': ')[0] + ", " + ma + ", " 
                + str(locale.latitude) + ", " + str(locale.longitude) + ", "
                + tags[t].get_text().split(': ')[1].replace(',','') + "\n")

file.write(tags[14].get_text().split(': ')[0] + ", " + ma + ", " + "" + ", " 
           + "" + ", " + tags[14].get_text().split(': ')[1].replace(',','') + "\n")

file.close()
     
if (tags[0].get_text().split(': ')[0]) == 'Barnstable' and (tags[14].get_text().split(': ')[0]) == 'Unknown':
    print("Massachusetts scraper is complete.\n")
else:
    print("ERROR: Must fix Massachusetts scraper.\n")