import bs4
import csv
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

ndDOH = 'https://www.health.nd.gov/diseases-conditions/coronavirus/north-dakota-coronavirus-cases'

ndClient = req(ndDOH)

site_parse = soup(ndClient.read(), "lxml")
ndClient.close()

tables = site_parse.find("div", {"class":"paragraph paragraph--type--bp-accordion-section paragraph--view-mode--default paragraph--id--3613"}).find('tbody')

csvfile = "COVID-19_cases_nddoh.csv"
headers = "County, Total Tests, Positive Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('tr')

for tag in tags[1:]:
    pull = tag.findAll('td')
    #print("County = %s, Total Tests = %s, Positive Cases = %s" % (pull[0].text, pull[1].text, pull[2].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.close()