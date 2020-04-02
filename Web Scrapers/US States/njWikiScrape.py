import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

njWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_New_Jersey'

njClient = req(njWiki)

site_parse = soup(njClient.read(), "lxml")
njClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_njWiki.csv"
headers = "County, Confirmed Cases, Deaths, Recoveries \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[47:69]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3].replace(',','') + ", " + take[5].replace(',','') + ", " + take[7].replace(',','') + "\n")

file.close()

if (hold[47].split('\n')[1]) == 'Atlantic' and (hold[68].split('\n')[1]) == 'Under investigation':
    print("New Jersey scraper is complete.\n")
else:
    print("ERROR: Must fix New Jersey scraper.\n")
