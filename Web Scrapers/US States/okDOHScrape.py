import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

okDOH = 'https://coronavirus.health.ok.gov/'

okClient = req(okDOH)

site_parse = soup(okClient.read(), "lxml")
okClient.close()

tables = site_parse.find("table", {"summary": "COVID-19 Cases by County"}).find("tbody")

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_okdoh.csv"
headers = "County, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags:
    pull = tag.findAll('td')
    print("County = %s, Cases = %s, Deaths = %s" % \
          (pull[0].text, pull[1].text, pull[2].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
file.close()