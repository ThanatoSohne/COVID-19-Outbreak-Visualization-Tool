import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

meDDS = 'https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml'

meClient = req(meDDS)

site_parse = soup(meClient.read(), "lxml")
meClient.close()

tables = site_parse.find("div", {"id": "Accordion1"}).findAll("td")[4:72]

#print(tables)

csvfile = "COVID-19_cases_meDDS.csv"
headers = "County, Confirmed Cases, Recovered, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
    take = t.get_text()
    hold.append(take)

andr = hold[0:4]
anC = andr.pop(0)
anCC = andr.pop(0)
anR = andr.pop(0)
anD = andr.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (anC, anCC, anR, anD))
file.write(anC + ", " + anCC + ", " + anR + ", " + anD +"\n")

aroo = hold[4:8]
arC = aroo.pop(0)
arCC = aroo.pop(0)
arR = aroo.pop(0)
arD = aroo.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (arC, arCC, arR, arD))
file.write(arC + ", " + arCC + ", " + arR + ", " + arD + "\n")


cumb = hold[8:12]
cumbC = cumb.pop(0)
cumbCC = cumb.pop(0)
cumbR = cumb.pop(0)
cumbD = cumb.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (cumbC, cumbCC, cumbR, cumbD))
file.write(cumbC + ", " + cumbCC + ", " + cumbR + ", " + cumbD + "\n")


frank = hold[12:16]
frC = frank.pop(0)
frCC = frank.pop(0)
frR = frank.pop(0)
frD = frank.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (frC, frCC, frR, frD))
file.write(frC + ", " + frCC + ", " + frR + ", " + frD + "\n")


hanc = hold[16:20]
haC = hanc.pop(0)
haCC = hanc.pop(0)
haR = hanc.pop(0)
haD = hanc.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (haC, haCC, haR, haD))
file.write(haC + ", " + haCC + ", " + haR + ", " + haD + "\n")


kenne = hold[20:24]
keC = kenne.pop(0)
keCC = kenne.pop(0)
keR = kenne.pop(0)
keD = kenne.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (keC, keCC, keR, keD))
file.write(keC + ", " + keCC + ", " + keR + ", " + keD + "\n")


knox = hold[24:28]
knC = knox.pop(0)
knCC = knox.pop(0)
knR = knox.pop(0)
knD = knox.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (knC, knCC, knR, knD))
file.write(knC + ", " + knCC + ", " + knR + ", " + knD + "\n")


linc = hold[28:32]
linC = linc.pop(0)
linCC = linc.pop(0)
linR = linc.pop(0)
linD = linc.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (linC, linCC, linR, linD))
file.write(linC + ", " + linCC + ", " + linR + ", " + linD + "\n")


ox = hold[32:36]
oxC = ox.pop(0)
oxCC = ox.pop(0)
oxR = ox.pop(0)
oxD = ox.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (oxC, oxCC, oxR, oxD))
file.write(oxC + ", " + oxCC + ", " + oxR + ", " + oxD + "\n")


peno = hold[36:40]
penC = peno.pop(0)
penCC = peno.pop(0)
penR = peno.pop(0)
penD = peno.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (penC, penCC, penR, penD))
file.write(penC + ", " + penCC + ", " + penR + ", " + penD + "\n")


pisca = hold[40:44]
piC = pisca.pop(0)
piCC = pisca.pop(0)
piR = pisca.pop(0)
piD = pisca.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (piC, piCC, piR, piD))
file.write(piC + ", " + piCC + ", " + piR + ", " + piD + "\n")


saga = hold[44:48]
sC = saga.pop(0)
sCC = saga.pop(0)
sR = saga.pop(0)
sD = saga.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (sC, sCC, sR, sD))
file.write(sC + ", " + sCC + ", " + sR + ", " + sD + "\n")


somer = hold[48:52]
soC = somer.pop(0)
soCC = somer.pop(0)
soR = somer.pop(0)
soD = somer.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (soC, soCC, soR, soD))
file.write(soC + ", " + soCC + ", " + soR + ", " + soD + "\n")


waldo = hold[52:56]
wdC = waldo.pop(0)
wdCC = waldo.pop(0)
wdR = waldo.pop(0)
wdD = waldo.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (wdC, wdCC, wdR, wdD))
file.write(wdC + ", " + wdCC + ", " + wdR + ", " + wdD + "\n")


wash = hold[56:60]
wsC = wash.pop(0)
wsCC = wash.pop(0)
wsR = wash.pop(0)
wsD = wash.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (wsC, wsCC, wsR, wsD))
file.write(wsC + ", " + wsCC + ", " + wsR + ", " + wsD + "\n")


york = hold[60:64]
yC = york.pop(0)
yCC = york.pop(0)
yR = york.pop(0)
yD = york.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (yC, yCC, yR, yD))
file.write(yC + ", " + yCC + ", " + yR + ", " + yD + "\n")


unk = hold[64:68]
uC = unk.pop(0)
uCC = unk.pop(0)
uR = unk.pop(0)
uD = unk.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
      (uC, uCC, uR, uD))
file.write(uC + ", " + uCC + ", " + uR + ", " + uD + "\n")

file.close()


    