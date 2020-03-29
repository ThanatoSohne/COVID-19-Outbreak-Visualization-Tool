import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

codoh = 'https://covid19.colorado.gov/case-data'

coClient = req(codoh)

site_parse = soup(coClient.read(), 'lxml')
coClient.close()

tables = site_parse.findAll("div", {"class": "paragraph__column--container-wrapper"})[2]

test = tables.findAll('tr')

hold = []

csvfile = "COVID-19_cases_coDOH.csv"
headers = "County, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

for t in test:
    pull = t.findAll('td')
    for p in pull:
        take = p.get_text()
        hold.append(take)

adams = hold[2:4]
file.write(adams[0] + ", " + adams[1] + "\n")
ala = hold[4:6]
file.write(ala[0] + ", " + ala[1] + "\n")
ara = hold[6:8]
file.write(ara[0] + ", " + ara[1] + "\n")
baca = hold[8:10]
file.write(baca[0] + ", " + baca[1] + "\n")
boulder = hold[10:12]
file.write(boulder[0] + ", " + boulder[1] + "\n")
broom = hold[12:14]
file.write(broom[0] + ", " + broom[1] + "\n")
chaf = hold[14:16]
file.write(chaf[0] + ", " + chaf[1] + "\n")
clear = hold[16:18]
file.write(clear[0] + ", " + clear[1] + "\n")
cost = hold[18:20]
file.write(cost[0] + ", " + cost[1] + "\n")
crow = hold[20:22]
file.write(crow[0] + ", " + crow[1] + "\n")
delta = hold[22:24]
file.write(delta[0] + ", " + delta[1] + "\n")
denver = hold[24:26]
file.write(denver[0] + ", " + denver[1] + "\n")
doug = hold[26:28]
file.write(doug[0] + ", " + doug[1] + "\n")
eagle = hold[28:30]
file.write(eagle[0] + ", " + eagle[1] + "\n")
elPaso = hold[30:32]
file.write(elPaso[0] + ", " + elPaso[1] + "\n")
elb = hold[32:34]
file.write(elb[0] + ", " + elb[1] + "\n")
frem = hold[34:36]
file.write(frem[0] + ", " + frem[1] + "\n")
garf = hold[36:38]
file.write(garf[0] + ", " + garf[1] + "\n")
grand = hold[38:40]
file.write(grand[0] + ", " + grand[1] + "\n")
gunn = hold[40:42]
file.write(gunn[0] + ", " + gunn[1] + "\n")
hins = hold[42:44]
file.write(hins[0] + ", " + hins[1] + "\n")
huer = hold[44:46]
file.write(huer[0] + ", " + huer[1] + "\n")
jeff = hold[46:48]
file.write(jeff[0] + ", " + jeff[1] + "\n")
kit = hold[48:50]
file.write(kit[0] + ", " + kit[1] + "\n")
laPlata = hold[50:52]
file.write(laPlata[0] + ", " + laPlata[1] + "\n")
lar = hold[52:54]
file.write(lar[0] + ", " + lar[1] + "\n")
linc = hold[54:56]
file.write(linc[0] + ", " + linc[1] + "\n")
logan = hold[56:58]
file.write(logan[0] + ", " + logan[1] + "\n")
mesa = hold[58:60]
file.write(mesa[0] + ", " + mesa[1] + "\n")
moff = hold[60:62]
file.write(moff[0] + ", " + moff[1] + "\n")
mont = hold[62:64]
file.write(mont[0] + ", " + mont[1] + "\n")
morg = hold[64:66]
file.write(morg[0] + ", " + morg[1] + "\n")
otero = hold[66:68]
file.write(otero[0] + ", " + otero[1] + "\n")
park = hold[68:70]
file.write(park[0] + ", " + park[1] + "\n")
pitk = hold[70:72]
file.write(pitk[0] + ", " + pitk[1] + "\n")
pueblo = hold[72:74]
file.write(pueblo[0] + ", " + pueblo[1] + "\n")
rio = hold[74:76]
file.write(rio[0] + ", " + rio[1] + "\n")
routt = hold[76:78]
file.write(routt[0] + ", " + routt[1] + "\n")
san = hold[78:80]
file.write(san[0] + ", " + san[1] + "\n")
summit = hold[80:82]
file.write(summit[0] + ", " + summit[1] + "\n")
teller = hold[82:84]
file.write(teller[0] + ", " + teller[1] + "\n")
wash = hold[84:86]
file.write(wash[0] + ", " + wash[1] + "\n")
weld = hold[86:88]
file.write(weld[0] + ", " + weld[1] + "\n")
yuma = hold[88:90]
file.write(yuma[0] + ", " + yuma[1] + "\n")

file.close()



