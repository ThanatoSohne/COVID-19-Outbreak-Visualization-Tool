import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

kaWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Kansas'

kaClient = req(kaWiki)

site_parse = soup(kaClient.read(), "lxml")
kaClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_kaWiki.csv"
headers = "County, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[45:88]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3] + ", " + take[4] + "\n")

file.close()

if (hold[45].split('\n')[1]) == 'Atchison' and (hold[87].split('\n')[1]) == 'Wyandotte':
    print("Kansas scraper is complete.\n")
else:
    print("ERROR: Must fix Kansas scraper.\n")


