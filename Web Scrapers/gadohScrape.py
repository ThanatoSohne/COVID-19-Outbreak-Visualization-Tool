import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

gadoh = 'https://dph.georgia.gov/covid-19-daily-status-report'

gaClient = req(gadoh)

site_parse = soup(gaClient.read(), 'lxml')
gaClient.close()

tables = site_parse.findAll("table", {"class": "stacked-row-plus"})[2]

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_gadoh.csv"
headers = "County, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[1:69]:
        pull = tag.findAll('td')
        print("County = %s, Confirmed Cases = %s" % \
              (pull[0].text, pull[1].text))
        file.write(pull[0].text + ", " + pull[1].text + "\n")

file.close()