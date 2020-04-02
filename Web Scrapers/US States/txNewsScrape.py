import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

txNews = 'https://apps.texastribune.org/features/2020/tx-coronavirus-tracker/embeds/daily-tables/table-latest/index.html'

bypass = {'User-Agent': 'Mozilla/5.0'}

txClient = Request(txNews, headers=bypass)
txPage = urlopen(txClient)

site_parse = soup(txPage, 'lxml')
txPage.close()

tables = site_parse.find("table", {"class": "dv-table"}).find('tbody')

csvfile = "COVID-19_cases_txNews.csv"
headers = "County, No. of Cases, Deaths \n"

file = open(csvfile, "w", encoding = 'utf-8')
file.write(headers)

tags = tables.findAll('tr')

for tag in tags[:10]:
    pull = tag.findAll('td')
    #print("County = %s, No. of Cases = %s, Deaths = %s" % (pull[0].text, pull[1].text, pull[2].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

for tag in tags[11:136]:
    pull = tag.findAll('td')
    #print("County = %s, No. of Cases = %s, Deaths = %s" % (pull[0].text, pull[1].text, pull[2].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.close()

if (tags[0].find('td').text) == 'Harris' and (tags[135].find('td').text) == 'Wood':
    print("Texas scraper is complete.\n")
else:
    print("ERROR: Must fix Texas scraper.\n")






