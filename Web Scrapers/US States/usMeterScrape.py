import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

usMeter = 'https://www.worldometers.info/coronavirus/country/us/'

bypass = {'User-Agent': 'Mozilla/5.0'}

usClient = Request(usMeter, headers=bypass)
usPage = urlopen(usClient)

site_parse = soup(usPage, 'lxml')
usPage.close()

tables = site_parse.find("table", {"id": "usa_table_countries_today"}).find('tbody')
table1 = site_parse.find("table", {"id": "usa_table_countries_today"}).findAll('tbody')[1]

csvfile = "COVID-19_cases_usMeter.csv"
headers = "State, Total Cases, Total Deaths, Active Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('tr')
tag1 = table1.findAll('tr')

for tag in tags:
    pull = tag.findAll('td')
    #print("State = %s, Total Cases = %s, Total Deaths = %s, Active Cases = %s" % \
     #     (pull[0].text.strip(), pull[1].text.strip(), pull[3].text.strip(), pull[5].text.strip()))
    file.write(pull[0].text.strip() + ", " + pull[1].text.strip().replace(',', '') + ", " + pull[3].text.strip().replace(',', '') + ", " + pull[5].text.strip().replace(',', '') + "\n")

for tag in tag1[0:6]:
    pull = tag.findAll('td')
    #print("State = %s, Total Cases = %s, Total Deaths = %s, Active Cases = %s" % \
     #     (pull[0].text.strip(), pull[1].text.strip(), pull[3].text.strip(), pull[5].text.strip()))
    file.write(pull[0].text.strip() + ", " + pull[1].text.strip().replace(',', '') + ", " + pull[3].text.strip().replace(',', '') + ", " + pull[5].text.strip().replace(',', '') + "\n")
    
file.close()