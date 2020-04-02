import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

azWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Arizona'

azClient = req(azWiki)

site_parse = soup(azClient.read(), "lxml")
azClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_azWiki.csv"
headers = "County, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)


hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[39:54]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")

file.close()

if (hold[39].split('\n')[1]) == 'Maricopa' and (hold[53].split('\n')[1]) == 'Greenlee':
    print("Arizona scraper is complete.\n")
else:
    print("ERROR: Must fix Arizona scraper.\n")