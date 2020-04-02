import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

paDOH = 'https://www.health.pa.gov/topics/disease/coronavirus/Pages/Cases.aspx'

paClient = req(paDOH)

site_parse = soup(paClient.read(), "lxml")
paClient.close()

tables = site_parse.find("div", {"class": "ms-rtestate-field", "style": "display:inline"}).find("div", {"style": "text-align:center;"}).find("table", {"class": "ms-rteTable-default"})

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_padoh.csv"
headers = "County, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[1:]:
    pull = tag.findAll('td')
    print("County = %s, Cases = %s, Deaths = %s" % \
          (pull[0].text, pull[1].text, pull[2].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.close()

if (tags[1].find('td').text) == 'Adams' and (tags[60].find('td').text.strip()) == 'York':
    print("Pennsylvania scraper is complete.\n")
else:
    print("ERROR: Must fix Pennsylvania scraper.\n")



