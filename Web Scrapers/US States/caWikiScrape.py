import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

cadoh = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_California'

caClient = req(cadoh)

site_parse = soup(caClient.read(), 'lxml')
caClient.close()

tables = site_parse.find("div", {"class": "tp-container"}).find_all('tbody')

csvfile = "COVID-19_cases_caWiki.csv"
headers = "County, Confirmed Cases, Deaths, Recoveries \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)

for h in hold[:47]:
    take = h.split('\n')
    file.write(take[1] + ", " + take[3] + ", " + take[5] + ", " + take[7] + "\n")
            

file.close()