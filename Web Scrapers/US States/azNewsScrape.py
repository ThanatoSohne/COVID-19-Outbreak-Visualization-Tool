import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

azNews = 'https://www.abc15.com/news/state/coronavirus-in-arizona-tracking-latest-cases-covid-19-updates-in-our-state/'

bypass = {'User-Agent': 'Mozilla/5.0'}

azClient = Request(azNews, headers=bypass)
azPage = urlopen(azClient)

site_parse = soup(azPage.read(), 'lxml')
azPage.close()

tables = site_parse.find("div", {"class": "RichTextArticleBody-body"})

death = tables.find_all('p')[4].get_text()[0:20].split(': ')[1]

cases = tables.find_all('p')[6].get_text()

csvfile = "COVID-19_cases_azNews.csv"
headers = "County, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

#hold = []
#
#for t in tags:
#    take = t.get_text()
#    hold.append(take)
#    
#test = hold[6]
#new = test.get_text()

pi = cases[59:68].split(': ')
pimaC = pi[0]
pimaN = pi[1]
#print("County = %s, Confirmed Cases = %s" % (pimaC, pimaN))
file.write(pimaC + ", " + pimaN + "\n")

mari = cases[25:38].split(': ')
mariC = mari[0]
mariN = mari[1]
#print("County = %s, Confirmed Cases = %s" % (mariC, mariN))
file.write(mariC + ", " + mariN + "\n")

pin = cases[38:47].split(': ')
pinalC = pin[0]
pinalN = pin[1]
#print("County = %s, Confirmed Cases = %s" % (pinalC, pinalN))
file.write(pinalC + ", " + pinalN + "\n")

cochise = cases[99:109].split(': ')
cochiseC = cochise[0]
cochiseN = cochise[1]
#print("County = %s, Confirmed Cases = %s" % (cochiseC, cochiseN))
file.write(cochiseC + ", " + cochiseN + "\n")

santaCruz = cases[118:131].split(': ')
santaC = santaCruz[0]
santaN = santaCruz[1]
#print("County = %s, Confirmed Cases = %s" % (santaC, santaN))
file.write(santaC + ", " + santaN + "\n")

navajo = cases[68:78].split(': ')
navajoC = navajo[0]
navajoN = navajo[1]
#print("County = %s, Confirmed Cases = %s" % (navajoC, navajoN))
file.write(navajoC + ", " + navajoN + "\n")

graham = cases[109:118].split(': ')
grahamC = graham[0]
grahamN = graham[1]
#print("County = %s, Confirmed Cases = %s" % (grahamC, grahamN))
file.write(grahamC + ", " + grahamN + "\n")

coco = cases[47:59].split(': ')
cocoC = coco[0]
cocoN = coco[1]
#print("County = %s, Confirmed Cases = %s" % (cocoC, cocoN))
file.write(cocoC + ", " + cocoN + "\n")

yuma = cases[131:138].split(': ')
yumaC = yuma[0]
yumaN = yuma[1]
#print("County = %s, Confirmed Cases = %s" % (yumaC, yumaN))
file.write(yumaC + ", " + yumaN + "\n")

apache = cases[89:99].split(': ')
apacheC = apache[0]
apacheN = apache[1]
#print("County = %s, Confirmed Cases = %s" % (apacheC, apacheN))
file.write(apacheC + ", " + apacheN + "\n")

yava = cases[78:89].split(': ')
yavaC = yava[0]
yavaN = yava[1]
#print("County = %s, Confirmed Cases = %s" % (yavaC, yavaN))
file.write(yavaC + ", " + yavaN + "\n")

mohave = cases[138:147].split(': ')
mohC = mohave[0]
mohN = mohave[1]
file.write(mohC + ", " + mohN + "\n")

lapaz = cases[147:156].split(': ')
lpC = lapaz[0]
lpN = lapaz[1]
file.write(lpC + ", " + lpN + "\n")

gila = cases[156:163].split(': ')
gilaC = gila[0]
gilaN = gila[1]
file.write(gilaC + ", " + gilaN + "\n")

green = cases[163:174].split(': ')
glC = green[0]
glN = green[1]
file.write(glC + ", " + glN + "\n")

gilaR = cases[174:205].split(': ')
gilC = gilaR[0]
gilN = gilaR[1]
file.write(gilaC + ", " + gilaN + "\n")

navajoN = cases[205:223].split(': ')
nnC = green[0]
nnN = green[1]
file.write(nnC + ", " + nnN + "\n")

saltR = cases[239:].split(': ')
saltC = saltR[0]
saltN = saltR[1]
file.write(saltC + ", " + saltN + "\n")

file.write("Deaths in Arizona = %s" % death)

file.close()





