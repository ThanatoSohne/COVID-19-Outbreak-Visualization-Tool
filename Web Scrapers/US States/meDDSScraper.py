from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim 
from time import sleep
import addfips

meDDS = 'https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml'

meClient = req(meDDS)

site_parse = soup(meClient.read(), "lxml")
meClient.close()

tables = site_parse.find("div", {"id": "Accordion1"}).findAll("td")[5:90]

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
me = "MAINE"
co = ' County'
fips = addfips.AddFIPS()
    
csvfile = "COVID-19_cases_meDDS.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"

hold = []

for t in tables:
    take = t.get_text()
    hold.append(take)
    
andr = hold[0:5]
anC = andr[0]
anCC = andr[1]
anR = andr[2]
anD = andr[4]
anLocale = liegen.geocode(anC + co + ", " + me)
sleep(1)
aroo = hold[5:10]
arC = aroo[0]
arCC = aroo[1]
arR = aroo[2]
arD = aroo[4]
arLocale = liegen.geocode(arC + co + ", " + me)
sleep(1)
cumb = hold[10:15]
cumbC = cumb[0]
cumbCC = cumb[1]
cumbR = cumb[2]
cumbD = cumb[4]
cLocale = liegen.geocode(cumbC + co + ", " + me)
sleep(1)
frank = hold[15:20]
frC = frank[0]
frCC = frank[1]
frR = frank[2]
frD = frank[4]
fLocale = liegen.geocode(frC + co + ", " + me)
sleep(1)
hanc = hold[20:25]
haC = hanc[0]
haCC = hanc[1]
haR = hanc[2]
haD = hanc[4]
hLocale = liegen.geocode(haC + co + ", " + me)
sleep(1)
kenne = hold[25:30]
keC = kenne[0]
keCC = kenne[1]
keR = kenne[2]
keD = kenne[4]
keLocale = liegen.geocode(keC + co + ", " + me)
sleep(1)
knox = hold[30:35]
knC = knox[0]
knCC = knox[1]
knR = knox[2]
knD = knox[4]
knLocale = liegen.geocode(knC + co + ", " + me)
sleep(1)
linc = hold[35:40]
linC = linc[0]
linCC = linc[1]
linR = linc[2]
linD = linc[4]
lLocale = liegen.geocode(linC + co + ", " + me)
sleep(1)
ox = hold[40:45]
oxC = ox[0]
oxCC = ox[1]
oxR = ox[2]
oxD = ox[4]
oxLocale = liegen.geocode(oxC + co + ", " + me)
sleep(1)
peno = hold[45:50]
penC = peno[0]
penCC = peno[1]
penR = peno[2]
penD = peno[4]
peLocale = liegen.geocode(penC + co + ", " + me)
sleep(1)
pisca = hold[50:55]
piC = pisca[0]
piCC = pisca[1]
piR = pisca[2]
piD = pisca[4]
piLocale = liegen.geocode(piC + co + ", " + me)
sleep(1)
saga = hold[55:60]
sC = saga[0]
sCC = saga[1]
sR = saga[2]
sD = saga[4]
saLocale = liegen.geocode(sC + co + ", " + me)
sleep(1)
somer = hold[60:65]
soC = somer[0]
soCC = somer[1]
soR = somer[2]
soD = somer[4]
soLocale = liegen.geocode(soC + co + ", " + me)
sleep(1)
waldo = hold[65:70]
wdC = waldo[0]
wdCC = waldo[1]
wdR = waldo[2]
wdD = waldo[4]
wdLocale = liegen.geocode(wdC + co + ", " + me)
sleep(1)
wash = hold[70:75]
wsC = wash[0]
wsCC = wash[1]
wsR = wash[2]
wsD = wash[4]
waLocale = liegen.geocode(wsC + co + ", " + me)
sleep(1)
york = hold[75:80]
yC = york[0]
yCC = york[1]
yR = york[2]
yD = york[4]
yoLocale = liegen.geocode(yC + co + ", " + me)
sleep(1)
unk = hold[80:85]
uC = unk[0]
uCC = unk[1]
uR = unk[2]
uD = unk[4]

if anC == 'Androscoggin' and uC == 'Unknown':
   
    file = open(csvfile, "w")
    file.write(headers)
    
    file.write(anC + ", " + me + ", " + fips.get_county_fips(anC,state=me) + ", " + str(anLocale.latitude) + ", " 
               + str(anLocale.longitude) + ", " + anCC + ", " + anD + ", " + anR +"\n")
    
    file.write(arC + ", " + me + ", " + fips.get_county_fips(arC,state=me) + ", " + str(arLocale.latitude) + ", " 
               + str(arLocale.longitude) + ", " + arCC + ", " + arD + ", " + arR +"\n")
    
    file.write(cumbC + ", " + me + ", " + fips.get_county_fips(cumbC,state=me) + ", " + str(cLocale.latitude) + ", " 
               + str(cLocale.longitude) + ", " + cumbCC + ", " + cumbD + ", " + cumbR +"\n")
    
    file.write(frC + ", " + me + ", " + fips.get_county_fips(frC,state=me) + ", " + str(fLocale.latitude) + ", " 
               + str(fLocale.longitude) + ", " + frCC + ", " + frD + ", " + frR +"\n")
    
    file.write(haC + ", " + me + ", " + fips.get_county_fips(haC,state=me) + ", " + str(hLocale.latitude) + ", " 
               + str(hLocale.longitude) + ", " + haCC + ", " + haD + ", " + haR +"\n")
    
    file.write(keC + ", " + me + ", " + fips.get_county_fips(keC,state=me) + ", " + str(keLocale.latitude) + ", " 
               + str(keLocale.longitude) + ", " + keCC + ", " + keD + ", " + keR +"\n")
    
    file.write(knC + ", " + me + ", " + fips.get_county_fips(knC,state=me) + ", " + str(knLocale.latitude) + ", " 
               + str(knLocale.longitude) + ", " + knCC + ", " + knD + ", " + knR +"\n")
    
    file.write(linC + ", " + me + ", " + fips.get_county_fips(linC,state=me) + ", " + str(lLocale.latitude) + ", " 
               + str(lLocale.longitude) + ", " + linCC + ", " + linD + ", " + linR +"\n")
    
    file.write(oxC + ", " + me + ", " + fips.get_county_fips(oxC,state=me) + ", " + str(oxLocale.latitude) + ", " 
               + str(oxLocale.longitude) + ", " + oxCC + ", " + oxD + ", " + oxR +"\n")
    
    file.write(penC + ", " + me + ", " + fips.get_county_fips(penC,state=me) + ", " + str(peLocale.latitude) + ", " 
               + str(peLocale.longitude) + ", " + penCC + ", " + penD + ", " + penR +"\n")
    
    file.write(piC + ", " + me + ", " + fips.get_county_fips(piC,state=me) + ", " + str(piLocale.latitude) + ", " 
               + str(piLocale.longitude) + ", " + piCC + ", " + piD + ", " + piR +"\n")
    
    file.write(sC + ", " + me + ", " + fips.get_county_fips(sC,state=me) + ", " + str(saLocale.latitude) + ", " 
               + str(saLocale.longitude) + ", " + sCC + ", " + sD + ", " + sR +"\n")
    
    file.write(soC + ", " + me + ", " + fips.get_county_fips(soC,state=me) + ", " + str(soLocale.latitude) + ", " 
               + str(soLocale.longitude) + ", " + soCC + ", " + soD + ", " + soR +"\n")
    
    file.write(wdC + ", " + me + ", " + fips.get_county_fips(wdC,state=me) + ", " + str(wdLocale.latitude) + ", " 
               + str(wdLocale.longitude) + ", " + wdCC + ", " + wdD + ", " + wdR +"\n")
    
    file.write(wsC + ", " + me + ", " + fips.get_county_fips(wsC,state=me) + ", " + str(waLocale.latitude) + ", " 
               + str(waLocale.longitude) + ", " + wsCC + ", " + wsD + ", " + wsR +"\n")

    file.write(yC + ", " + me + ", " + fips.get_county_fips(yC,state=me) + ", " + str(yoLocale.latitude) + ", " 
               + str(yoLocale.longitude) + ", " + yCC + ", " + yD + ", " + yR +"\n")
    
    file.write(uC + ", " + me + ", " + fips.get_state_fips(me) + ", " + str(liegen.geocode(me).latitude) 
               + ", " + str(liegen.geocode(me).longitude) + ", " + uCC + ", " + uD + ", " + uR +"\n")
    
    file.close()

    print("Maine scraper is complete.")
else:
    print("ERROR: Must fix Maine scraper.")
    