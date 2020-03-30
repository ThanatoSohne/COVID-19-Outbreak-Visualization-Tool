import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

ioWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Iowa'

ioClient = req(ioWiki)

site_parse = soup(ioClient.read(), "lxml")
ioClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_ioWiki.csv"
headers = "County, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[37:74]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")

file.close()