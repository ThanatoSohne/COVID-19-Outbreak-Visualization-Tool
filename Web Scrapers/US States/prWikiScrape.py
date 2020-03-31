import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

prWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Puerto_Rico'

prClient = req(prWiki)

site_parse = soup(prClient.read(), "lxml")
prClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_prWiki.csv"
headers = "Region, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[13:22]:
    take = h.split('\n')
    file.write(take[1] +  ", " + take[5] + "\n")

file.close()