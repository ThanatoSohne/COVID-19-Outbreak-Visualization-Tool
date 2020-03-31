import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

tndoh = 'https://www.tn.gov/health/cedep/ncov.html'

tnClient = req(tndoh)

site_parse = soup(tnClient.read(), 'lxml')
tnClient.close()

tables = site_parse.find("div", {"class": "containers tn-accordion parbase"}).find("div", {"class": "tn-simpletable parbase"})

colTable = site_parse.find("div", {"class": "row parsys_column tn-3cols"}).findAll("div", {"class": "tn-simpletable parbase"})[2]

fatal = colTable.find('tr')
fa = fatal.get_text().split('\n')
faStr = fa.pop(0)
faNo = fa.pop(0)

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_tndoh.csv"
headers = "County, Positive Cases \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[1:]:
    pull = tag.findAll('p')
    print("County = %s, Positive Cases = %s" % (pull[0].text, pull[1].text))
    
    file.write(pull[0].text + ", " + pull[1].text.replace(',','') + "\n")

file.write("\n")
file.write(faStr + ", " + faNo + "\n")

file.close()
