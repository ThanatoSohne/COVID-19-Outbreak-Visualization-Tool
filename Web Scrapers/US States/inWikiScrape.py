import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

inWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Indiana'

inClient = req(inWiki)

site_parse = soup(inClient.read(), "lxml")
inClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_inWiki.csv"
headers = "County, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[40:122]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")

file.close()

if (hold[40].split('\n')[1]) == 'Adams' and (hold[121].split('\n')[1]) == 'Whitley':
    print("Indiana scraper is complete.\n")
else:
    print("ERROR: Must fix Indiana scraper.\n")




