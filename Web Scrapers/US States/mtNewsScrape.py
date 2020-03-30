import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

mtNews = 'https://www.livescience.com/montana-coronavirus-updates.html'

mtClient = req(mtNews)

site_parse = soup(mtClient.read(), "lxml")
mtClient.close()

tables = site_parse.find("div", {"id" : "article-body"}).find('ul')

csvfile = "COVID-19_cases_mtNews.csv"
headers = "County, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('li')

for t in tags:
    pull = t.get_text().split(": ")
    file.write(pull[0] + ", " + pull[1] + "\n")

file.close()