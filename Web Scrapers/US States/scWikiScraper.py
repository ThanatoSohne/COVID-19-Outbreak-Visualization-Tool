import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

scWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_South_Carolina'

scClient = req(scWiki)

site_parse = soup(scClient.read(), "lxml")
scClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_scWiki.csv"
headers = "County, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[43:86]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")

file.close()

if (hold[43].split('\n')[1]) == 'Abbeville' and (hold[85].split('\n')[1]) == 'York':
    print("South Carolina scraper is complete.\n")
else:
    print("ERROR: Must fix South Carolina scraper.\n")




