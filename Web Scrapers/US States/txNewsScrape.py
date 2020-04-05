from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

txNews = 'https://apps.texastribune.org/features/2020/tx-coronavirus-tracker/embeds/daily-tables/table-latest/index.html'

bypass = {'User-Agent': 'Mozilla/5.0'}

txClient = Request(txNews, headers=bypass)
txPage = urlopen(txClient)

site_parse = soup(txPage, 'lxml')
txPage.close()

tables = site_parse.find("table", {"class": "dv-table"}).find('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
tx = "TEXAS"
co = ' County'

csvfile = "COVID-19_cases_txNews.csv"
headers = "County, State, Latitude, Longitude, No. of Cases, Deaths \n"

file = open(csvfile, "w", encoding = 'utf-8')
file.write(headers)

tags = tables.findAll('tr')

for tag in tags[:10]:
    pull = tag.findAll('td')
    locale = liegen.geocode(pull[0].text + co + ", " + tx)
    file.write(pull[0].text + ", " + tx + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + pull[1].text.replace(',','') + ", " + pull[2].text + "\n")
    sleep(1)

for tag in tags[11:65]:
    pull = tag.findAll('td')
    locale = liegen.geocode(pull[0].text + co + ", " + tx)
    file.write(pull[0].text + ", " + tx + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + pull[1].text.replace(',','') + ", " + pull[2].text + "\n")
    sleep(1)

locale1 = liegen.geocode(tags[65].find('td').text.replace(' ', '') + co + ", " + tx)
file.write(tags[65].find('td').text.replace(' ', '') + ", " + tx + ", " + str(locale1.latitude) + ", " 
               + str(locale1.longitude) + ", " + tags[65].findAll('td')[1].text.replace(',','') 
               + ", " + tags[65].findAll('td')[2].text + "\n")

for tag in tags[66:152]:
    pull = tag.findAll('td')
    locale = liegen.geocode(pull[0].text + co + ", " + tx)
    file.write(pull[0].text + ", " + tx + ", " + str(locale.latitude) + ", " 
               + str(locale.longitude) + ", " + pull[1].text.replace(',','') + ", " + pull[2].text + "\n")
    sleep(1.2)

file.close()

if (tags[0].find('td').text) == 'Harris' and (tags[151].find('td').text) == 'Wood':
    print("Texas scraper is complete.")
else:
    print("ERROR: Must fix Texas scraper.")






