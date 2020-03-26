import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

meDDS = 'https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml'

meClient = req(meDDS)

site_parse = soup(meClient.read(), "lxml")
meClient.close()

tables = site_parse.find("div", {"id": "Accordion1"}).findAll("td")[3:54]

#print(tables)

csvfile = "COVID-19_cases_meDDS.csv"
headers = "County, Confirmed Cases, Recovered \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
    take = t.get_text()
    hold.append(take)

andr = hold[0:3]
anC = andr.pop(0)
anCC = andr.pop(0)
anR = andr.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (anC, anCC, anR))
file.write(anC + ", " + anCC + ", " + anR + "\n")

aroo = hold[3:6]
arC = aroo.pop(0)
arCC = aroo.pop(0)
arR = aroo.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (arC, arCC, arR))
file.write(arC + ", " + arCC + ", " + arR + "\n")


cumb = hold[6:9]
cumbC = cumb.pop(0)
cumbCC = cumb.pop(0)
cumbR = cumb.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (cumbC, cumbCC, cumbR))
file.write(cumbC + ", " + cumbCC + ", " + cumbR + "\n")


frank = hold[9:12]
frC = frank.pop(0)
frCC = frank.pop(0)
frR = frank.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (frC, frCC, frR))
file.write(frC + ", " + frCC + ", " + frR + "\n")


hanc = hold[12:15]
haC = hanc.pop(0)
haCC = hanc.pop(0)
haR = hanc.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (haC, haCC, haR))
file.write(haC + ", " + haCC + ", " + haR + "\n")


kenne = hold[15:18]
keC = kenne.pop(0)
keCC = kenne.pop(0)
keR = kenne.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (keC, keCC, keR))
file.write(keC + ", " + keCC + ", " + keR + "\n")


knox = hold[18:21]
knC = knox.pop(0)
knCC = knox.pop(0)
knR = knox.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (knC, knCC, knR))
file.write(knC + ", " + knCC + ", " + knR + "\n")


linc = hold[21:24]
linC = linc.pop(0)
linCC = linc.pop(0)
linR = linc.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (linC, linCC, linR))
file.write(linC + ", " + linCC + ", " + linR + "\n")


ox = hold[24:27]
oxC = ox.pop(0)
oxCC = ox.pop(0)
oxR = ox.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (oxC, oxCC, oxR))
file.write(oxC + ", " + oxCC + ", " + oxR + "\n")


peno = hold[27:30]
penC = peno.pop(0)
penCC = peno.pop(0)
penR = peno.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (penC, penCC, penR))
file.write(penC + ", " + penCC + ", " + penR + "\n")


pisca = hold[30:33]
piC = pisca.pop(0)
piCC = pisca.pop(0)
piR = pisca.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (piC, piCC, piR))
file.write(piC + ", " + piCC + ", " + piR + "\n")


saga = hold[33:36]
sC = saga.pop(0)
sCC = saga.pop(0)
sR = saga.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (sC, sCC, sR))
file.write(sC + ", " + sCC + ", " + sR + "\n")


somer = hold[36:39]
soC = somer.pop(0)
soCC = somer.pop(0)
soR = somer.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (soC, soCC, soR))
file.write(soC + ", " + soCC + ", " + soR + "\n")


waldo = hold[39:42]
wdC = waldo.pop(0)
wdCC = waldo.pop(0)
wdR = waldo.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (wdC, wdCC, wdR))
file.write(wdC + ", " + wdCC + ", " + wdR + "\n")


wash = hold[42:45]
wsC = wash.pop(0)
wsCC = wash.pop(0)
wsR = wash.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (wsC, wsCC, wsR))
file.write(wsC + ", " + wsCC + ", " + wsR + "\n")


york = hold[45:48]
yC = york.pop(0)
yCC = york.pop(0)
yR = york.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (yC, yCC, yR))
file.write(yC + ", " + yCC + ", " + yR + "\n")


unk = hold[48:51]
uC = unk.pop(0)
uCC = unk.pop(0)
uR = unk.pop()
print("County = %s, Confirmed Cases = %s, Recovered = %s" % \
      (uC, uCC, uR))
file.write(uC + ", " + uCC + ", " + uR + "\n")

file.close()


    