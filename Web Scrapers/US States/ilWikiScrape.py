import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

ilWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Illinois'

ilClient = req(ilWiki)

site_parse = soup(ilClient.read(), "lxml")
ilClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

csvfile = "COVID-19_cases_ilWiki.csv"
headers = "County, Active Cases, Deaths, Recoveries, Total Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)
            
for h in hold[46:97]:
    take = h.split('\n')
    #print(take[1], take[3], take[5], take[7], take[9])
    file.write(take[1] + ", " + take[3] + ", " + take[5] + ", " + take[7] + ", " + take[9] + "\n")

file.close()
    
    
