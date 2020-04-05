from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

utNews = 'https://www.livescience.com/utah-coronavirus-updates.html'

utClient = req(utNews)

site_parse = soup(utClient.read(), 'lxml')
utClient.close()

tables = site_parse.find("article", {"class": "news-article", "data-id": "Kk2kmK3UhF5L6dgXZf8wHe"}).find("div", {"itemprop": "articleBody"}).findAll('ul')[1]

liegen = Nominatim(user_agent = 'combiner-atomundwolke@gmail.com')
ut = "UTAH"
co = ' County'

csvfile = "COVID-19_cases_utNews.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('li')

for t in range(0,13):
    locale = liegen.geocode(tags[t].text.split('- ')[0].strip() + ", " + ut)
    file.write(tags[t].text.split('- ')[0].strip() + ", " + ut + ", " + str(locale.latitude) 
               + ", " + str(locale.longitude) + ", " 
               + tags[t].text.split('- ')[1].strip().split('(')[0].strip() + "\n")

    sleep(1)
file.close()

if (tags[0].get_text().split('- ')[0].strip()) == 'Bear River' and (tags[12].get_text().split('- ')[0].strip()) == 'Weber-Morgan county':
    print("Utah scraper is complete.")
else:
    print("ERROR: Must fix Utah scraper.")






