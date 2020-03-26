import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

miDOH = 'https://www.michigan.gov/Coronavirus'

miClient = req(miDOH)

site_parse = soup(miClient.read(), "lxml")
miClient.close()

tables = site_parse.find("div", {"class": "fullContent"}).find("tbody")

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_midoh.csv"
headers = "County, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[0:33]:
    pull = tag.findAll('td')
    print("County = %s, Cases = %s, Deaths = %s" % \
          (pull[0].text, pull[1].text, pull[2].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.close()