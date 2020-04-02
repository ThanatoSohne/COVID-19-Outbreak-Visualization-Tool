import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

wyWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Wyoming'

wyClient = req(wyWiki)

site_parse = soup(wyClient.read(), "lxml")
wyClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_wyWiki.csv"
headers = "County, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[46:69]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")

file.close()

if (hold[46].split('\n')[1]) == 'Albany' and (hold[68].split('\n')[1]) == 'Weston':
    print("Wyoming scraper is complete.")
else:
    print("ERROR: Must fix Wyoming scraper.")






