import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

idDOH = 'https://coronavirus.idaho.gov/'

idClient = req(idDOH)

site_parse = soup(idClient.read(), "lxml")
idClient.close()

tables = site_parse.find("table", {"class": "tablepress tablepress-id-1 tablepress-responsive"})

csvfile = "COVID-19_cases_idDOH.csv"
headers = "County, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

holdCo = []
holdCas = []
holdDe = []

counties = tables.findAll("td", {"class": "column-2"})
for lo in counties:
    take = lo.get_text()
    holdCo.append(take)

cases = tables.findAll("td", {"class": "column-3"})
for la in cases:
    take = la.get_text()
    holdCas.append(take)

deaths = tables.findAll("td", {"class": "column-4"})
for le in deaths:
    take = le.get_text()
    holdDe.append(take)

for c, a, d in zip(holdCo, holdCas, holdDe):
    file.write(c + ", " + a + ", " + d + "\n")
    
file.close()

if holdCo[0] == 'Bonner' and holdCo[29] == 'TOTAL':
    print("Idaho scraper is complete.\n")
else:
    print("ERROR: Must fix Idaho scraper.\n")






