import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

moDOH = 'https://health.mo.gov/living/healthcondiseases/communicable/novel-coronavirus/results.php'

moClient = req(moDOH)

site_parse = soup(moClient.read(), "lxml")
moClient.close()

tables = site_parse.find("div", {"class": "panel-group"}).findAll('tr')

csvfile = "COVID-19_cases_modoh.csv"
headers = "County, Cases \n"
sHeaders = "County, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for t in tables[1:119]:
    pull = t.findAll('td')
    #print("County = %s, Cases = %s" % \
          #(pull[0].text, pull[1].text))
    file.write(pull[0].text + ", " + pull[1].text + "\n")

tablesDe = site_parse.find("div", {"id": "collapseDeaths"}).findAll('tr')

file.write("\n")
file.write(sHeaders)

for ta in tablesDe[1:]:
    pullDe = ta.findAll('td')
    #print("County = %s, Deaths = %s" % (pullDe[0].text, pullDe[1].text))
    file.write(pullDe[0].text + ", " + pullDe[1].text + "\n")

file.close()