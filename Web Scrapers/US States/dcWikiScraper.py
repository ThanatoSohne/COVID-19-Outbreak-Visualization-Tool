from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep

dcWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

dcClient = req(dcWiki)

site_parse = soup(dcClient.read(), "lxml")
dcClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_dcWiki.csv"
headers = "Region, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

dc = "WASHINGTON DC"

dcGeo = liegen.geocode(dc)

sleep(1)

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

file.write(hold[88].split('\n')[3] + ", " + dc + ", " + str(dcGeo.latitude) 
           + ", " + str(dcGeo.longitude) + ", " + hold[88].split('\n')[5].replace(',','') 
           + ", " + hold[88].split('\n')[7].replace(',','') + ", " 
           + hold[88].split('\n')[9].replace(',','') + "\n")

file.close()

if hold[88].split('\n')[3] == "Washington D.C.":
    print("DC scraper is complete.")
else:
    print("ERROR: Must fix DC scraper.")

#dcFile = "https://coronavirus.dc.gov/sites/default/files/dc/sites/coronavirus/page_content/attachments/COVID19_DCHealthStatisticsDataV2%20%283%29.xlsx"
#
#download = requests.get(dcFile)
#download.raise_for_status()
#
#newLife = open('COVID-19-DC.xlsx', 'wb')
#for chunk in download.iter_content(100000):
#    newLife.write(chunk)
#
#newLife.close()