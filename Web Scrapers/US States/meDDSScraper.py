import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

meDDS = 'https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml'

meClient = req(meDDS)

site_parse = soup(meClient.read(), "lxml")
meClient.close()

tables = site_parse.find("div", {"id": "Accordion1"}).findAll("td")[5:90]

#print(tables)

csvfile = "COVID-19_cases_meDDS.csv"
headers = "County, Confirmed Cases, Recovered, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
    take = t.get_text()
    hold.append(take)

andr = hold[0:5]
anC = andr[0]
anCC = andr[1]
anR = andr[2]
anD = andr[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (anC, anCC, anR, anD))
file.write(anC + ", " + anCC + ", " + anR + ", " + anD +"\n")

aroo = hold[5:10]
arC = aroo[0]
arCC = aroo[1]
arR = aroo[2]
arD = aroo[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (arC, arCC, arR, arD))
file.write(arC + ", " + arCC + ", " + arR + ", " + arD + "\n")


cumb = hold[10:15]
cumbC = cumb[0]
cumbCC = cumb[1]
cumbR = cumb[2]
cumbD = cumb[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (cumbC, cumbCC, cumbR, cumbD))
file.write(cumbC + ", " + cumbCC + ", " + cumbR + ", " + cumbD + "\n")


frank = hold[15:20]
frC = frank[0]
frCC = frank[1]
frR = frank[2]
frD = frank[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (frC, frCC, frR, frD))
file.write(frC + ", " + frCC + ", " + frR + ", " + frD + "\n")


hanc = hold[20:25]
haC = hanc[0]
haCC = hanc[1]
haR = hanc[2]
haD = hanc[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (haC, haCC, haR, haD))
file.write(haC + ", " + haCC + ", " + haR + ", " + haD + "\n")


kenne = hold[25:30]
keC = kenne[0]
keCC = kenne[1]
keR = kenne[2]
keD = kenne[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (keC, keCC, keR, keD))
file.write(keC + ", " + keCC + ", " + keR + ", " + keD + "\n")


knox = hold[30:35]
knC = knox[0]
knCC = knox[1]
knR = knox[2]
knD = knox[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (knC, knCC, knR, knD))
file.write(knC + ", " + knCC + ", " + knR + ", " + knD + "\n")


linc = hold[35:40]
linC = linc[0]
linCC = linc[1]
linR = linc[2]
linD = linc[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (linC, linCC, linR, linD))
file.write(linC + ", " + linCC + ", " + linR + ", " + linD + "\n")


ox = hold[40:45]
oxC = ox[0]
oxCC = ox[1]
oxR = ox[2]
oxD = ox[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (oxC, oxCC, oxR, oxD))
file.write(oxC + ", " + oxCC + ", " + oxR + ", " + oxD + "\n")


peno = hold[45:50]
penC = peno[0]
penCC = peno[1]
penR = peno[2]
penD = peno[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (penC, penCC, penR, penD))
file.write(penC + ", " + penCC + ", " + penR + ", " + penD + "\n")


pisca = hold[50:55]
piC = pisca[0]
piCC = pisca[1]
piR = pisca[2]
piD = pisca[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (piC, piCC, piR, piD))
file.write(piC + ", " + piCC + ", " + piR + ", " + piD + "\n")


saga = hold[55:60]
sC = saga[0]
sCC = saga[1]
sR = saga[2]
sD = saga[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (sC, sCC, sR, sD))
file.write(sC + ", " + sCC + ", " + sR + ", " + sD + "\n")


somer = hold[60:65]
soC = somer[0]
soCC = somer[1]
soR = somer[2]
soD = somer[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (soC, soCC, soR, soD))
file.write(soC + ", " + soCC + ", " + soR + ", " + soD + "\n")


waldo = hold[65:70]
wdC = waldo[0]
wdCC = waldo[1]
wdR = waldo[2]
wdD = waldo[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (wdC, wdCC, wdR, wdD))
file.write(wdC + ", " + wdCC + ", " + wdR + ", " + wdD + "\n")


wash = hold[70:75]
wsC = wash[0]
wsCC = wash[1]
wsR = wash[2]
wsD = wash[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (wsC, wsCC, wsR, wsD))
file.write(wsC + ", " + wsCC + ", " + wsR + ", " + wsD + "\n")


york = hold[75:80]
yC = york[0]
yCC = york[1]
yR = york[2]
yD = york[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (yC, yCC, yR, yD))
file.write(yC + ", " + yCC + ", " + yR + ", " + yD + "\n")


unk = hold[80:85]
uC = unk[0]
uCC = unk[1]
uR = unk[2]
uD = unk[4]
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (uC, uCC, uR, uD))
file.write(uC + ", " + uCC + ", " + uR + ", " + uD + "\n")

file.close()


    