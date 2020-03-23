import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

tndoh = 'https://www.tn.gov/health/cedep/ncov.html'

tnClient = req(tndoh)

site_parse = soup(tnClient.read(), 'lxml')
tnClient.close()

tables = site_parse.find("div", {"class": "row parsys_column tn-3cols"})

colTable = tables.find("div", {"class": "parsys_column column-2"})

tags = colTable.findAll('tr')

csvfile = "COVID-19_cases_tndoh.csv"
headers = "County, Positive Cases \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[1:44]:
    pull = tag.findAll('p')
    print("County = %s, Positive Cases = %s" % (pull[0].text, pull[1].text))
    
    file.write(pull[0].text + ", " + pull[1].text + "\n")

file.close()
