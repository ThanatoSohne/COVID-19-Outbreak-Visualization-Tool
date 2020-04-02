import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

nhNews = 'https://www.livescience.com/new-hampshire-coronavirus-updates.html'

nhClient = req(nhNews)

site_parse = soup(nhClient.read(), "lxml")
nhClient.close()

tables = site_parse.find("article", {"class":"news-article"}).find("div", {"itemprop": "articleBody"}).find('ul')

csvfile = "COVID-19_cases_nhNews.csv"
headers = "County, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('li')

for t in range(0,11):
    #print("%s %s" % \
    #      (tags[t].get_text().split(': ')[0], tags[t].get_text().split(': ')[1]))
    file.write(tags[t].get_text().split(': ')[0] + ", " + tags[t].get_text().split(': ')[1] + "\n")

file.close()
     
if (tags[0].get_text().split(': ')[0]) == 'Rockingham' and (tags[10].get_text().split(': ')[0]) == 'Sullivan':
    print("New Hampshire scraper is complete.\n")
else:
    print("ERROR: Must fix New Hampshire scraper.\n")



