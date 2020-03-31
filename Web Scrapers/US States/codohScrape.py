import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

codoh = 'https://covid19.colorado.gov/case-data'

coClient = req(codoh)

site_parse = soup(coClient.read(), 'lxml')
coClient.close()

tables = site_parse.findAll("div", {"class": "field field--name-field-card-body field--type-text-long field--label-hidden field--item"})[1]

test = tables.findAll('tr')

hold = []

csvfile = "COVID-19_cases_coDOH.csv"
headers = "County, Positive Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for t in test[1:50]:
        pull = t.findAll('td')
        #print("County = %s, Positive Cases = %s, Deaths = %s" % \
         #     (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.close()



