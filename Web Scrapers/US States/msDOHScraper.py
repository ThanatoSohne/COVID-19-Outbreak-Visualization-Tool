import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

msDOH = 'https://msdh.ms.gov/msdhsite/_static/14,0,420.html'

msClient = req(msDOH)

site_parse = soup(msClient.read(), "lxml")
msClient.close()

tables = site_parse.find("table", {"id": "msdhTotalCovid-19Cases"}).find("tbody").findAll('tr')

csvfile = "COVID-19_cases_msdoh.csv"
headers = "County, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for t in tables[0:31]:
    pull = t.findAll('td')
    #print("County = %s, Cases = %s, Deaths = %s" % \
     #     (pull[0].text, pull[1].text, pull[2].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.write(tables[32].findAll('td')[0].text + ", " + tables[32].findAll('td')[1].text + ", " + tables[32].findAll('td')[2].text + "\n")

for t in tables[34:79]:
    pull = t.findAll('td')
    #print("County = %s, Cases = %s, Deaths = %s" % \
     #     (pull[0].text, pull[1].text, pull[2].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.close()

if (tables[0].find('td').text) == 'Adams' and (tables[78].find('td').text) == 'Yazoo':
    print("Mississippi scraper is complete.\n")
else:
    print("ERROR: Must fix Mississippi scraper.\n")




