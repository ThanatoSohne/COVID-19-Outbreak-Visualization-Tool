import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

mnDOH = 'https://www.health.state.mn.us/diseases/coronavirus/situation.html'

mnClient = req(mnDOH)

site_parse = soup(mnClient.read(), "lxml")
mnClient.close()

tables = site_parse.find("div", {"class": "clearfix"}).find("tbody").findAll('td')

csvfile = "COVID-19_cases_mndoh.csv"
headers = "County, Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for td in tables:
    take = td.get_text()
    hold.append(take)

anoka = hold[0:2]
#print(anoka.pop(0) + ", " + anoka.pop())
file.write(anoka.pop(0) + ", " + anoka.pop() + "\n")

benton = hold[2:4]
file.write(benton.pop(0) + ", " + benton.pop() + "\n")

big = hold[4:6]
file.write(big.pop(0) + ", " + big.pop() + "\n")

blue = hold[6:8]
file.write(blue.pop(0) + ", " + blue.pop() + "\n")

carv = hold[8:10]
file.write(carv.pop(0) + ", " + carv.pop() + "\n")

cass = hold[10:12]
file.write(cass.pop(0) + ", " + cass.pop() + "\n")

chis = hold[12:14]
file.write(chis.pop(0) + ", " + chis.pop() + "\n")

clay = hold[14:16]
file.write(clay.pop(0) + ", " + clay.pop() + "\n")

dak = hold[16:18]
file.write(dak.pop(0) + ", " + dak.pop() + "\n")

dod = hold[18:20]
file.write(dod.pop(0) + ", " + dod.pop() + "\n")

fill = hold[20:22]
file.write(fill.pop(0) + ", " + fill.pop() + "\n")

good = hold[22:24]
file.write(good.pop(0) + ", " + good.pop() + "\n")

henn = hold[24:26]
file.write(henn.pop(0) + ", " + henn.pop() + "\n")

jack = hold[26:28]
file.write(jack.pop(0) + ", " + jack.pop() + "\n")

lac = hold[28:30]
file.write(lac.pop(0) + ", " + lac.pop() + "\n")

le = hold[30:32]
file.write(le.pop(0) + ", " + le.pop() + "\n")

mar = hold[32:34]
file.write(mar.pop(0) + ", " + mar.pop() + "\n")

mow = hold[34:36]
file.write(mow.pop(0) + ", " + mow.pop() + "\n")

nic = hold[36:38]
file.write(nic.pop(0) + ", " + nic.pop() + "\n")

olm = hold[38:40]
file.write(olm.pop(0) + ", " + olm.pop() + "\n")

ram = hold[40:42]
file.write(ram.pop(0) + ", " + ram.pop() + "\n")

ren = hold[42:44]
file.write(ren.pop(0) + ", " + ren.pop() + "\n")

rice = hold[44:46]
file.write(rice.pop(0) + ", " + rice.pop() + "\n")

scott = hold[46:48]
file.write(scott.pop(0) + ", " + scott.pop() + "\n")

sher = hold[48:50]
file.write(sher.pop(0) + ", " + sher.pop() + "\n")

stl = hold[50:52]
file.write(stl.pop(0) + ", " + stl.pop() + "\n")

stea = hold[52:54]
file.write(stea.pop(0) + ", " + stea.pop() + "\n")

stee = hold[54:56]
file.write(stee.pop(0) + ", " + stee.pop() + "\n")

wab = hold[56:58]
file.write(wab.pop(0) + ", " + wab.pop() + "\n")

was = hold[58:60]
file.write(was.pop(0) + ", " + was.pop() + "\n")

wash = hold[60:62]
file.write(wash.pop(0) + ", " + wash.pop() + "\n")

win = hold[62:64]
file.write(win.pop(0) + ", " + win.pop() + "\n")

wri = hold[64:66]
file.write(wri.pop(0) + ", " + wri.pop() + "\n")

file.close()