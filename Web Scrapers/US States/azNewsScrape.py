import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

azNews = 'https://www.kold.com/2020/03/24/update-pima-county-confirms-first-death-covid-/'

bypass = {'User-Agent': 'Mozilla/5.0'}

azClient = Request(azNews, headers=bypass)
azPage = urlopen(azClient)

site_parse = soup(azPage.read(), 'lxml')
azPage.close()

tables = site_parse.find("ul", {"class": "secondary no-margin"})

tags = tables.findAll('li')

csvfile = "COVID-19_cases_azNews.csv"
headers = "County, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for li in tags:
    take = li.get_text()
    hold.append(take)
    
pima = hold[0].split(' - ')
pimaC = pima.pop(0)
pimaN = pima.pop()
#print("County = %s, Confirmed Cases = %s" % (pimaC, pimaN))
file.write(pimaC + ", " + pimaN + "\n")

maricopa = hold[1].split(' - ')
mariC = maricopa.pop(0)
mariN = maricopa.pop()
#print("County = %s, Confirmed Cases = %s" % (mariC, mariN))
file.write(mariC + ", " + mariN + "\n")

pinal = hold[2].split(' - ')
pinalC = pinal.pop(0)
pinalN = pinal.pop()
#print("County = %s, Confirmed Cases = %s" % (pinalC, pinalN))
file.write(pinalC + ", " + pinalN + "\n")

cochise = hold[3].split(' - ')
cochiseC = cochise.pop(0)
cochiseN = cochise.pop()
#print("County = %s, Confirmed Cases = %s" % (cochiseC, cochiseN))
file.write(cochiseC + ", " + cochiseN + "\n")

santaCruz = hold[4].split(' - ')
santaC = santaCruz.pop(0)
santaN = santaCruz.pop()
#print("County = %s, Confirmed Cases = %s" % (santaC, santaN))
file.write(santaC + ", " + santaN + "\n")

navajo = hold[5].split(' - ')
navajoC = navajo.pop(0)
navajoN = navajo.pop()
#print("County = %s, Confirmed Cases = %s" % (navajoC, navajoN))
file.write(navajoC + ", " + navajoN + "\n")

graham = hold[6].split(' - ')
grahamC = graham.pop(0)
grahamN = graham.pop()
#print("County = %s, Confirmed Cases = %s" % (grahamC, grahamN))
file.write(grahamC + ", " + grahamN + "\n")

cococino = hold[7].split(' - ')
cocoC = cococino.pop(0)
cocoN = cococino.pop()
#print("County = %s, Confirmed Cases = %s" % (cocoC, cocoN))
file.write(cocoC + ", " + cocoN + "\n")

yuma = hold[8].split(' - ')
yumaC = yuma.pop(0)
yumaN = yuma.pop()
#print("County = %s, Confirmed Cases = %s" % (yumaC, yumaN))
file.write(yumaC + ", " + yumaN + "\n")

apache = hold[9].split(' - ')
apacheC = apache.pop(0)
apacheN = apache.pop()
#print("County = %s, Confirmed Cases = %s" % (apacheC, apacheN))
file.write(apacheC + ", " + apacheN + "\n")

yavapai = hold[10].split(' - ')
yavaC = yavapai.pop(0)
yavaN = yavapai.pop()
#print("County = %s, Confirmed Cases = %s" % (yavaC, yavaN))
file.write(yavaC + ", " + yavaN + "\n")

other = hold[11].split(' - ')
otherC = other.pop(0)
otherN = other.pop()
#print("County = %s, Confirmed Cases = %s" % (otherC, otherN))
file.write(otherC + ", " + otherN + "\n")

file.close()





