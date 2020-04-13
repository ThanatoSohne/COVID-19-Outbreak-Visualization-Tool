import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep
import addfips

hidoh = 'https://health.hawaii.gov/coronavirusdisease2019/what-you-should-know/current-situation-in-hawaii/'

hiClient = req(hidoh)

site_parse = soup(hiClient.read(), "lxml")
hiClient.close()

tables = site_parse.find("div", {"id": "inner-wrap"}).find('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
hi= "HAWAII"
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_hidoh.csv"
headers = "County,State,FIPS,Latitude,Longitude,Total Cases,Deaths,Recoveries,Released from Isolation,Hospitalization\n"

tags = tables.findAll('td')

hawaii = tags[18].text.replace("\xa0","")
haLocale = liegen.geocode(hawaii + ", " + hi)
haFIPS = fips.get_county_fips(hawaii,state=hi)
haTotal = tags[21].text
haIso = tags[23].text
haHosp = tags[25].text
haDeaths = tags[27].text

honolulu = tags[30].text
honLocale = liegen.geocode(honolulu + ", " + hi)
honFIPS = fips.get_county_fips(honolulu,state=hi)
honTotal = tags[33].text
honIso = tags[35].text
honHosp = tags[37].text
honDeaths = tags[39].text

kauai = tags[42].text
kauLocale = liegen.geocode(kauai + ", " + hi)
kauFIPS = fips.get_county_fips(kauai,state=hi)
kauTotal = tags[45].text
kauIso = tags[47].text
kauHosp = tags[49].text
kauDeaths = tags[51].text

maui = tags[54].text
mauiLocale = liegen.geocode(maui + ", " + hi)
mauiFIPS = fips.get_county_fips(maui,state=hi)
mauiTotal = tags[57].text
mauiIso = tags[59].text
mauiHosp = tags[61].text
mauiDeaths = tags[63].text

outHI = tags[66].text
outHIno = tags[67].text

pending = tags[68].text
penNo = tags[69].text

if hawaii == 'Hawaii County' and pending == 'County Pending':

    file = open(csvfile, "w")
    file.write(headers)
    
    file.write(hawaii + ", " + hi + ", " + haFIPS + ", " + str(haLocale.latitude) + ", " +
               str(haLocale.longitude) + ", " + haTotal + ", " + haDeaths + ",  " + "" 
               + ", " + haIso + ", " + haHosp + "\n")
    
    file.write(honolulu + ", " + hi + ", " + honFIPS + ", " + str(honLocale.latitude) + ", " +
               str(honLocale.longitude) + ", " + honTotal + ", " + honDeaths + ",  " + "" 
               + ", " + honIso + ", " + honHosp + "\n")
    
    
    file.write(kauai + ", " + hi + ", " + kauFIPS + ", " + str(kauLocale.latitude) + ", " +
               str(kauLocale.longitude) + ", " + kauTotal + ", " + kauDeaths + ",  " + "" 
               + ", " + kauIso + ", " + kauHosp + "\n")
    
    file.write(maui + ", " + hi + ", " + mauiFIPS + ", " + str(mauiLocale.latitude) + ", " +
               str(mauiLocale.longitude) + ", " + mauiTotal + ", " + mauiDeaths + ",  " + "" 
               + ", " + mauiIso + ", " + mauiHosp + "\n")
    
    file.write(outHI + ", " + hi + ", " + haFIPS + ", " + str(liegen.geocode(hi).latitude) + ", " + str(liegen.geocode(hi).longitude) + ", " + outHIno + "\n")
    
    file.write(pending + ", " + hi + ", " + haFIPS + ", " + str(liegen.geocode(hi).latitude) + ", " + str(liegen.geocode(hi).longitude) + ", " + penNo + "\n")
    
    file.close()

    print("Hawai'i scraper is complete.")
else:
    print("ERROR: Must fix Hawai'i scraper.")