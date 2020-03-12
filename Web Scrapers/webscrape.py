import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

ecdc = 'https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases'

eClient = req(ecdc)

site_parse = soup(eClient.read(), "lxml")
eClient.close()

tables = site_parse.find("div", {"class": "table-responsive field field-name-field-pt-table"})

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_ecdc.csv"
headers = "Region, Places reporting cases, Confirmed cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

#regions = []
#country = []
#confirmed_cases = []
#deaths = []

for tag in tags[1:]:
    pull = tag.findAll('td')
    print("Regions= %s, Country = %s, Confirmed Cases = %s, Deaths = %s" % \
          (pull[0].text, pull[1].text, pull[2].text, pull[3].text))
    
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + ", " + pull[3].text + "\n")

file.close()