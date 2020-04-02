import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

gadoh = 'https://d20s4vd27d0hk0.cloudfront.net/?initialWidth=616&childId=covid19dashdph&parentTitle=COVID-19%20Daily%20Status%20Report%20%7C%20Georgia%20Department%20of%20Public%20Health&parentUrl=https%3A%2F%2Fdph.georgia.gov%2Fcovid-19-daily-status-report'

gaClient = req(gadoh)

site_parse = soup(gaClient.read(), 'lxml')
gaClient.close()

tables = site_parse.find("div", {"id": "summary"}).findAll('tr')

csvfile = "COVID-19_cases_gadoh.csv"
headers = "County, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for t in tables[5:149]:
        pull = t.findAll('td')
        #print("County = %s, Cases = %s, Deaths = %s" % \
         #     (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.close()

if (tables[5].find('td').text) == 'Fulton' and (tables[148].find('td').text) == 'Unknown':
    print("Georgia scraper is complete.\n")
else:
    print("ERROR: Must fix Georgia scraper.\n")