import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

miDOH = 'https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html'

miClient = req(miDOH)

site_parse = soup(miClient.read(), "lxml")
miClient.close()

tables = site_parse.find("div", {"class": "fullContent"}).find("tbody")

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_midoh.csv"
headers = "County, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[1:71]:
    pull = tag.findAll('td')
    #print("County = %s, Cases = %s, Deaths = %s" % \
     #     (pull[0].text, pull[1].text, pull[2].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.close()

if (tags[1].find('td').text.strip()) == 'Allegan' and (tags[70].find('td').text.strip()) == 'Out of State':
    print("Michigan scraper is complete.\n")
else:
    print("ERROR: Must fix Michigan scraper.\n")