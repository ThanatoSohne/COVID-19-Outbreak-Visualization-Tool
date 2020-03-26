import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

orDOH = 'https://govstatus.egov.com/OR-OHA-COVID-19'

orClient = req(orDOH)

site_parse = soup(orClient.read(), "lxml")
orClient.close()

tables = site_parse.find("div", {"id": "collapseOne"}).find("tbody")

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_ordoh.csv"
headers = "County, Cases, Deaths, Negative Test Results \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags:
    pull = tag.findAll('td')
    print("County = %s, Cases = %s, Deaths = %s, Negative Test Results = %s" % \
          (pull[0].text, pull[1].text, pull[2].text, pull[3].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + ", " + pull[3].text + "\n")

file.close()
