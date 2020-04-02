import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

vaWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Virginia'

vaClient = req(vaWiki)

site_parse = soup(vaClient.read(), "lxml")
vaClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_vaWiki.csv"
headers = "County, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[44:145]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3].split('[')[0] + ", " + take[5].split('[')[0] + "\n")

file.close()

if (hold[44].split('\n')[1]) == 'Accomack County' and (hold[144].split('\n')[1]) == 'York County':
    print("Virginia scraper is complete.")
else:
    print("ERROR: Must fix Virginia scraper.")






