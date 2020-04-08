import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep

hidoh = 'https://health.hawaii.gov/coronavirusdisease2019/what-you-should-know/current-situation-in-hawaii/'

hiClient = req(hidoh)

site_parse = soup(hiClient.read(), "lxml")
hiClient.close()

tables = site_parse.find("div", {"id": "inner-wrap"}).find('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
hi= "HAWAII"

csvfile = "COVID-19_cases_hidoh.csv"
headers = "County, State, Latitude, Longitude, Total Cases, Deaths, Recoveries, Released from Isolation, Req. Hospitalization \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('td')

hawaii = tags[18].text.replace("\xa0","")
haLocale = liegen.geocode(hawaii + ", " + hi)
haTotal = tags[21].text
haIso = tags[23].text
haHosp = tags[25].text
haDeaths = tags[27].text
file.write(hawaii + ", " + hi + ", " + str(haLocale.latitude) + ", " +
           str(haLocale.longitude) + ", " + haTotal + ", " + haDeaths + ",  " + "" 
           + ", " + haIso + ", " + haHosp + "\n")

honolulu = tags[30].text
honLocale = liegen.geocode(honolulu + ", " + hi)
honTotal = tags[33].text
honIso = tags[35].text
honHosp = tags[37].text
honDeaths = tags[39].text
file.write(honolulu + ", " + hi + ", " + str(honLocale.latitude) + ", " +
           str(honLocale.longitude) + ", " + honTotal + ", " + honDeaths + ",  " + "" 
           + ", " + honIso + ", " + honHosp + "\n")


kauai = tags[42].text
kauLocale = liegen.geocode(kauai + ", " + hi)
kauTotal = tags[45].text
kauIso = tags[47].text
kauHosp = tags[49].text
kauDeaths = tags[51].text
file.write(kauai + ", " + hi + ", " + str(kauLocale.latitude) + ", " +
           str(kauLocale.longitude) + ", " + kauTotal + ", " + kauDeaths + ",  " + "" 
           + ", " + kauIso + ", " + kauHosp + "\n")

maui = tags[54].text
mauiLocale = liegen.geocode(maui + ", " + hi)
mauiTotal = tags[57].text
mauiIso = tags[59].text
mauiHosp = tags[61].text
mauiDeaths = tags[63].text
file.write(maui + ", " + hi + ", " + str(mauiLocale.latitude) + ", " +
           str(mauiLocale.longitude) + ", " + mauiTotal + ", " + mauiDeaths + ",  " + "" 
           + ", " + mauiIso + ", " + mauiHosp + "\n")

outHI = tags[66].text
outHIno = tags[67].text
file.write(outHI + ", " + hi + ", " + "" + ", " + "" + ", " + outHIno + "\n")

pending = tags[68].text
penNo = tags[69].text
file.write(pending + ", " + hi + ", " + "" + ", " + "" + ", " + penNo + "\n")

file.close()

if hawaii == 'Hawaii County' and pending == 'County Pending':
    print("Hawai'i scraper is complete.\n")
else:
    print("ERROR: Must fix Hawai'i scraper.\n")