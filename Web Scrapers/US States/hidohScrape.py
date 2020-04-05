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
headers = "County, State, Latitude, Longitude, Total Cases, Released from Isolation, Req. Hospitalization, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('td')

hawaii = tags[26].text.replace("\xa0","")
haLocale = liegen.geocode(hawaii + ", " + hi)
haTotal = tags[31].text
haIso = tags[34].text
haHosp = tags[37].text
haDeaths = tags[40].text
file.write(hawaii + ", " + hi + ", " + str(haLocale.latitude) + ", " +
           str(haLocale.longitude) + ", " + haTotal + ", " + haIso + ", " +
           haHosp + ", " + haDeaths + "\n")

honolulu = tags[44].text
honLocale = liegen.geocode(honolulu + ", " + hi)
honTotal = tags[49].text
honIso = tags[52].text
honHosp = tags[55].text
honDeaths = tags[58].text
file.write(honolulu + ", " + hi + ", " + str(honLocale.latitude) + ", " +
           str(honLocale.longitude) + ", " + honTotal + ", " + honIso + ", " +
           honHosp + ", " + honDeaths + "\n")

kauai = tags[62].text
kauLocale = liegen.geocode(kauai + ", " + hi)
kauTotal = tags[67].text
kauIso = tags[70].text
kauHosp = tags[73].text
kauDeaths = tags[76].text
file.write(kauai + ", " + hi + ", " + str(kauLocale.latitude) + ", " +
           str(kauLocale.longitude) + ", " + kauTotal + ", " + kauIso + ", " +
           kauHosp + ", " + kauDeaths + "\n")

maui = tags[80].text
mauiLocale = liegen.geocode(maui + ", " + hi)
mauiTotal = tags[85].text
mauiIso = tags[88].text
mauiHosp = tags[91].text
mauiDeaths = tags[94].text
file.write(maui + ", " + hi + ", " + str(mauiLocale.latitude) + ", " +
           str(mauiLocale.longitude) + ", " + mauiTotal + ", " + mauiIso + ", " +
           mauiHosp + ", " + mauiDeaths + "\n")

outHI = tags[98].text
outHIno = tags[100].text
file.write(outHI + ", " + hi + ", " + "" + ", " + "" + ", " + outHIno + "\n")

pending = tags[101].text
penNo = tags[103].text
file.write(pending + ", " + hi + ", " + "" + ", " + "" + ", " + penNo + "\n")

file.close()

if hawaii == 'Hawaii County' and pending == 'County Pending':
    print("Hawai'i scraper is complete.\n")
else:
    print("ERROR: Must fix Hawai'i scraper.\n")