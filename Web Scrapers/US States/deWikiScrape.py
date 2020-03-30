import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

dedoh = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Delaware'

deClient = req(dedoh)

site_parse = soup(deClient.read(), 'lxml')
deClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).findAll('tbody')[3]

pull = tables.findAll('td')

csvfile = "COVID-19_cases_deWiki.csv"
headers = "County, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

kent = pull[0].get_text().split('\n')[0]
kentC = pull[1].get_text().split('\n')[0]
newCastle = pull[2].get_text().split('\n')[0]
newC = pull[3].get_text().split('\n')[0]
suss = pull[4].get_text().split('\n')[0]
sussC = pull[5].get_text().split('\n')[0]


file.write(kent + ", " + kentC + "\n")
file.write(newCastle + ", " + newC + "\n")
file.write(suss + ", " + sussC + "\n")

file.close()
