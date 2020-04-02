import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

maNews = 'https://www.livescience.com/massachusetts-coronavirus-updates.html'

maClient = req(maNews)

site_parse = soup(maClient.read(), "lxml")
maClient.close()

tables = site_parse.find("div", {"itemprop": "articleBody"}).find('ul')

csvfile = "COVID-19_cases_maNews.csv"
headers = "County, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('li')

for t in range(0,15):
    #print("%s %s" % \
     #     (tags[t].get_text().split(': ')[0], tags[t].get_text().split(': ')[1]))
     file.write(tags[t].get_text().split(': ')[0] + ", " + tags[t].get_text().split(': ')[1].replace(',','') + "\n")

file.close()
     
if (tags[0].get_text().split(': ')[0]) == 'Barnstable' and (tags[14].get_text().split(': ')[0]) == 'Unknown':
    print("Massachusetts scraper is complete.\n")
else:
    print("ERROR: Must fix Massachusetts scraper.\n")