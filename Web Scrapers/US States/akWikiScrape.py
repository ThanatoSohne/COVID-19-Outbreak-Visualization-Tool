from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from time import sleep

akWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Alaska'

akClient = req(akWiki)

site_parse = soup(akClient.read(), "lxml")
akClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_akdoh.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases\n"

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

fips = addfips.AddFIPS()
ak = "ALASKA"

anch = liegen.geocode("Anchorage, Alaska")                      #1
gulf = liegen.geocode("Kenai Peninsula Borough, Alaska")        #2
inter = liegen.geocode("Fairbanks North Star Borough, Alaska")  #3
matsu = liegen.geocode("Matanuska-Susitna Borough, Alaska")     #4
north = liegen.geocode("North Slope Borough, Alaska")           #5
sE = liegen.geocode("Juneau Borough, Alaska")                   #6
sW = liegen.geocode("Bethel, Alaska")                           #7
    
hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

if (hold[46].split('\n')[1]) == 'Anchorage' and (hold[68].split('\n')[1]) == 'Total':
    
    file = open(csvfile, "w")
    file.write(headers)
    
    #Anchorage, AK
    file.write(hold[46].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Anchorage", state = ak) + ", " + str(anch.latitude) + ", " + str(anch.longitude) + ", " + hold[44].split('\n')[3] + "\n")
    sleep(1)
    #Anchor Point, AK
    file.write(hold[47].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Kenai Peninsula", state = ak) + ", " + str(liegen.geocode("Anchor Point, AK").latitude) + ", " + str(liegen.geocode("Anchor Point, AK").longitude) + ", " + hold[47].split('\n')[3] + "\n")
    sleep(1)
    #Bethel, AK
    file.write(hold[48].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Bethel", state = ak) + ", " + str(liegen.geocode("Bethel, AK").latitude) + ", " + str(liegen.geocode("Bethel, AK").longitude) + ", " + hold[48].split('\n')[3] + "\n")
    sleep(1)
    #Chugiak, AK
    file.write(hold[49].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Anchorage", state = ak) + ", " + str(liegen.geocode("Chugiak, AK").latitude) + ", " + str(liegen.geocode("Chugiak, AK").longitude) + ", " + hold[49].split('\n')[3] + "\n")
    sleep(1)
    #Craig, AK
    file.write(hold[50].split('\n')[1] + ", " + ak + ", " + "02201" + ", " + str(liegen.geocode("Craig, AK").latitude) + ", " + str(liegen.geocode("Craig, AK").longitude) + ", " + hold[50].split('\n')[3] + "\n")
    sleep(1)
    #Delta Junction, AK
    file.write(hold[51].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Southeast Fairbanks", state = ak) + ", " + str(liegen.geocode("Delta Junction, AK").latitude) + ", " + str(liegen.geocode("Delta Junction, AK").longitude) + ", " + hold[51].split('\n')[3] + "\n")
    sleep(1)
    #Eagle River, AK
    file.write(hold[52].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Anchorage", state = ak) + ", " + str(liegen.geocode("Eagle River, AK").latitude) + ", " + str(liegen.geocode("Eagle River, AK").longitude) + ", " + hold[52].split('\n')[3] + "\n")
    sleep(1)
    #Fairbanks, AK
    file.write(hold[53].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Fairbanks North Star", state = ak) + ", " + str(liegen.geocode("Fairbanks, AK").latitude) + ", " + str(liegen.geocode("Fairbanks, AK").longitude) + ", " + hold[53].split('\n')[3] + "\n")
    sleep(1)
    #Girdwood, AK
    file.write(hold[54].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Anchorage", state = ak) + ", " + str(liegen.geocode("Girdwood, AK").latitude) + ", " + str(liegen.geocode("Girdwood, AK").longitude) + ", " + hold[54].split('\n')[3] + "\n")
    sleep(1)
    #Homer, AK
    file.write(hold[55].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Kenai Peninsula", state = ak) + ", " + str(liegen.geocode("Homer, AK").latitude) + ", " + str(liegen.geocode("Homer, AK").longitude) + ", " + hold[55].split('\n')[3] + "\n")
    sleep(1)
    #Juneau, AK
    file.write(hold[56].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Juneau", state = ak) + ", " + str(liegen.geocode("Juneau, AK").latitude) + ", " + str(liegen.geocode("Juneau, AK").longitude) + ", " + hold[56].split('\n')[3] + "\n")
    sleep(1)
    #Kenai, AK
    file.write(hold[57].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Kenai Peninsula", state = ak) + ", " + str(liegen.geocode("Kenai, AK").latitude) + ", " + str(liegen.geocode("Kenai, AK").longitude) + ", " + hold[57].split('\n')[3] + "\n")
    sleep(1)
    #Ketchikan, AK
    file.write(hold[58].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Ketchikan Gateway", state = ak) + ", " + str(liegen.geocode("Ketchikan, AK").latitude) + ", " + str(liegen.geocode("Ketchikan, AK").longitude) + ", " + hold[58].split('\n')[3] + "\n")
    sleep(1)
    #North Pole
    file.write(hold[59].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Fairbanks North Star", state = ak) + ", " + str(liegen.geocode("North Pole, AK").latitude) + ", " + str(liegen.geocode("North Pole, AK").longitude) + ", " + hold[59].split('\n')[3] + "\n")
    sleep(1)
    #Palmer, AK
    file.write(hold[60].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Matanuska-Susitna", state = ak) + ", " + str(liegen.geocode("Palmer, AK").latitude) + ", " + str(liegen.geocode("Palmer, AK").longitude) + ", " + hold[60].split('\n')[3] + "\n")
    sleep(1)
    #Petersburg, AK
    file.write(hold[61].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Petersburg", state = ak) + ", " + str(liegen.geocode("Petersburg, AK").latitude) + ", " + str(liegen.geocode("Petersburg, AK").longitude) + ", " + hold[61].split('\n')[3] + "\n")
    sleep(1)
    #Seward, AK
    file.write(hold[62].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Kenai Peninsula", state = ak) + ", " + str(liegen.geocode("Seward, AK").latitude) + ", " + str(liegen.geocode("Seward, AK").longitude) + ", " + hold[62].split('\n')[3] + "\n")
    sleep(1)
    #Soldotna, AK
    file.write(hold[63].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Kenai Peninsula", state = ak) + ", " + str(liegen.geocode("Soldotna, AK").latitude) + ", " + str(liegen.geocode("Soldotna, AK").longitude) + ", " + hold[63].split('\n')[3] + "\n")
    sleep(1)
    #Sterling, AK
    file.write(hold[64].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Kenai Peninsula", state = ak) + ", " + str(liegen.geocode("Sterling, AK").latitude) + ", " + str(liegen.geocode("Sterling, AK").longitude) + ", " + hold[64].split('\n')[3] + "\n")
    sleep(1)
    #Yukon-Koyukuk, AK
    file.write(hold[65].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Yukon-Koyukuk", state = ak) + ", " + str(liegen.geocode("Yukon-Koyukuk, AK").latitude) + ", " + str(liegen.geocode("Yukon-Koyukuk, AK").longitude) + ", " + hold[65].split('\n')[3] + "\n")
    sleep(1)
    #Wasilla, AK
    file.write(hold[66].split('\n')[1] + ", " + ak + ", " + fips.get_county_fips("Matanuska-Susitna", state = ak) + ", " + str(liegen.geocode("Wasilla, AK").latitude) + ", " + str(liegen.geocode("Wasilla, AK").longitude) + ", " + hold[66].split('\n')[3] + "\n")
    sleep(1)
    #Simply for purposes of allocating counties on map visualization
    file.write("Aleutians East" + ", " + ak + ", " + fips.get_county_fips("Aleutians East", state = ak) + "\n")
    file.write("Aleutians West" + ", " + ak + ", " + fips.get_county_fips("Aleutians West", state = ak) + "\n")
    file.write("Denali" + ", " + ak + ", " + fips.get_county_fips("Denali", state = ak) + "\n")
    file.write("Dillingham" + ", " + ak + ", " + fips.get_county_fips("Dillingham", state = ak) + "\n")
    file.write("Haines" + ", " + ak + ", " + fips.get_county_fips("Haines", state = ak) + "\n")
    file.write("Kodiak Island" + ", " + ak + ", " + fips.get_county_fips("Kodiak Island", state = ak) + "\n")
    file.write("Lake and Peninsula" + ", " + ak + ", " + fips.get_county_fips("Lake and Peninsula", state = ak) + "\n")
    file.write("Nome" + ", " + ak + ", " + fips.get_county_fips("Nome", state = ak) + "\n")
    file.write("Northwest Attic" + ", " + ak + ", " + "02188" + "\n")
    file.write("Sitka" + ", " + ak + ", " + fips.get_county_fips("Sitka", state = ak) + "\n")
    file.write("Skagway" + ", " + ak + ", " + fips.get_county_fips("Skagway", state = ak) + "\n")
    file.write("Valdez-Cordova" + ", " + ak + ", " + fips.get_county_fips("Valdez-Cordova", state = ak) + "\n")
    file.write("Kusilvak" + ", " + ak + ", " + fips.get_county_fips("Kusilvak", state = ak) + "\n")
    file.write("Wrangell" + ", " + ak + ", " + fips.get_county_fips("Wrangell", state = ak) + "\n")
    file.write("Yakutat" + ", " + ak + ", " + fips.get_county_fips("Yakutat", state = ak) + "\n")
    
    file.close()
    
    print("Alaska scraper complete.")
else:
    print("ERROR: Must fix Alaska scraper.")