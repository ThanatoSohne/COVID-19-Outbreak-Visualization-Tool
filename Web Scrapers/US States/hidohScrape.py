import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

hidoh = 'https://health.hawaii.gov/docd/advisories/novel-coronavirus-2019/'

hiClient = req(hidoh)

site_parse = soup(hiClient.read(), "lxml")
hiClient.close()

tables = site_parse.find("tbody")

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_hidoh.csv"
headers = "County, Positive Cases \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[3:7]:
    pull = tag.findAll('td')
    print("County = %s, Positive Cases = %s" % \
          (pull[0].text, pull[1].text))
    file.write(pull[0].text + ", " + pull[1].text + "\n")

file.close()