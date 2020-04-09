from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

riDOH = 'https://www.nytimes.com/interactive/2020/us/rhode-island-coronavirus-cases.html'

riClient = req(riDOH)

site_parse = soup(riClient.read(), "lxml")
riClient.close()

tables = site_parse.find("tbody", {"class": "top-level svelte-yabvh9"})

tags = tables.findAll('td')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ri = "RHODE ISLAND"
co = ' County'

csvfile = "COVID-19_cases_riNews.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tags[5:]:
    take = t.text.split('\n')[0]
    hold.append(take)

prov = hold[1]
provL = liegen.geocode(prov + co + ", " + ri)
sleep(1)
provC = hold[2]
provD = hold[4]
file.write(prov + ", " + ri + ", " + str(provL.latitude) + ", " 
           + str(provL.longitude) + ", " + provC + ", " + provD + "\n")

kent = hold[7]
kentL = liegen.geocode(kent + co + ", " + ri)
sleep(1)
kentC = hold[8]
kentD = hold[10]
file.write(kent + ", " + ri + ", " + str(kentL.latitude) + ", " 
           + str(kentL.longitude) + ", " + kentC + ", " + kentD + "\n")

wash = hold[13]
washL = liegen.geocode(wash + co + ", " + ri)
sleep(1)
washC = hold[14]
washD = hold[16]
file.write(wash + ", " + ri + ", " + str(washL.latitude) + ", " 
           + str(washL.longitude) + ", " + washC + ", " + washD + "\n")

new = hold[19]
newL = liegen.geocode(new + co + ", " + ri)
sleep(1)
newC = hold[20]
newD = hold[22]
file.write(new + ", " + ri + ", " + str(newL.latitude) + ", " 
           + str(newL.longitude) + ", " + newC + ", " + newD + "\n")

brist = hold[25]
bristL = liegen.geocode(brist + co + ", " + ri)
sleep(1)
bristC = hold[26]
bristD = hold[28]
file.write(brist + ", " + ri + ", " + str(bristL.latitude) + ", " 
           + str(bristL.longitude) + ", " + bristC + ", " + bristD + "\n")

unkn = hold[31]
unkC = hold[32]
unkD = hold[34]
file.write(unkn + ", " + ri + ", " + "" + ", " + "" + ", " + unkC + ", " + unkD + "\n")

file.close()

if prov == "Providence" and unkn == "Unknown":
    print("Rhode Island scraper is complete.")
else:
    print("ERROR: Must fix Rhode Island scraper.")