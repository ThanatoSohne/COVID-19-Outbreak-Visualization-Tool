import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

ncDOH = 'https://www.ncdhhs.gov/covid-19-case-count-nc#nc-counties-with-cases'

ncClient = req(ncDOH)

site_parse = soup(ncClient.read(), 'lxml')
ncClient.close()

tables = site_parse.find("div", {"class": "content band-content landing-wrapper"}).find('tbody')

csvfile = "COVID-19_cases_ncdoh.csv"
headers = "County, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('tr')

for tag in tags:
    pull = tag.findAll('td')
    print("County = %s, Cases = %s, Deaths = %s" % (pull[0].text, pull[1].text, pull[2].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.close()