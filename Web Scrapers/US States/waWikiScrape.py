import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

waWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Washington_(state)'

waClient = req(waWiki)

site_parse = soup(waClient.read(), "lxml")
waClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_waWiki.csv"
headers = "County, Confirmed Cases, Deaths, Recoveries \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[54:94]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3].split('[')[0].replace(',','') + ", " + take[5].split('[')[0].replace(',','') + ", " + take[7].split('[')[0].replace(',','') + "\n")

file.close()

if (hold[54].split('\n')[1]) == 'Adams' and (hold[93].split('\n')[1]) == '(Unassigned)':
    print("Washington scraper is complete.")
else:
    print("ERROR: Must fix Washington scraper.")


