import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

utNews = 'https://www.livescience.com/utah-coronavirus-updates.html'

utClient = req(utNews)

site_parse = soup(utClient.read(), 'lxml')
utClient.close()

tables = site_parse.find("article", {"class": "news-article", "data-id": "Kk2kmK3UhF5L6dgXZf8wHe"}).find("div", {"itemprop": "articleBody"}).findAll('ul')[1]

csvfile = "COVID-19_cases_utNews.csv"
headers = "County, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('li')

for t in range(0,13):
    #print("%s %s" % \
     #     (tags[t].get_text().split(': ')[0], tags[t].get_text().split(': ')[1]))
     file.write(tags[t].get_text().split('- ')[0] + ", " + tags[t].get_text().split('- ')[1] + "\n")

file.close()