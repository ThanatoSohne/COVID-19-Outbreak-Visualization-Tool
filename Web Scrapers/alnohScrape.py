import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

aldoh = 'http://www.alabamapublichealth.gov/infectiousdiseases/2019-coronavirus.html'

alClient = req(aldoh)

site_parse = soup(alClient.read(), 'lxml')
alClient.close()

tables = site_parse.find("div", {"class": "row mainContent"})

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_aldoh.csv"
headers = "County, Positive Cases \n"

file = open(csvfile, "w")
file.write(headers)


for tag in tags[2:23]:
    pull = tag.findAll('p')
    print("County = %s, Positive Cases = %s" % (pull[0].text, pull[1].text))
    
    file.write(pull[0].text + ", " + pull[1].text + "\n")

file.close()