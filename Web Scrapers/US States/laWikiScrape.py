import bs4
import csv
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

laWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Louisiana'

laClient = req(laWiki)

site_parse = soup(laClient.read(), "lxml")
laClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_laWiki.csv"
headers = "Parish, Confirmed Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[64:121]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3].replace(',','') + ", " + take[5].replace(',','') + "\n")
    #file.writerow(take[1], take[3], take[5])

file.close()

if (hold[64].split('\n')[1]) == 'Acadia' and (hold[120].split('\n')[1]) == 'Under Investigation':
    print("Louisiana scraper is complete.\n")
else:
    print("ERROR: Must fix Louisiana scraper.\n")
