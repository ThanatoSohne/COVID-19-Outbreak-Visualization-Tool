import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup


akWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Alaska'

akClient = req(akWiki)

site_parse = soup(akClient.read(), "lxml")
akClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_akdoh.csv"
headers = "Region, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)
    
hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[34:41]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3].split('[')[0].replace(',','') + "\n")

file.close()

if (hold[34].split('\n')[1]) == 'Anchorage/Southcentral Alaska' and (hold[40].split('\n')[1]) == 'Southwest':
    print("Alaska scraper complete.\n")
else:
    print("ERROR: Must fix Alaska scraper.\n")

