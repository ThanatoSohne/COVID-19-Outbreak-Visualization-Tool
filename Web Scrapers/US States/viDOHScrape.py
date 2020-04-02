import bs4
import csv
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

viDOH = 'https://doh.vi.gov/covid19usvi'

viClient = req(viDOH)

site_parse = soup(viClient.read(), "lxml")
viClient.close()

tables = site_parse.find("div", {"class": "page-content-sidebar col-sm-12 col-md-4"}).find("div", {"class": "block-content clearfix"})

csvfile = "COVID-19_cases_vidoh.csv"
headers = "Case Types, No. of Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('p')

pos = tags[0].text.split(':\xa0')[0]
posNo = tags[0].text.split(':\xa0')[1]

recov = tags[1].text.split(':\xa0')[0]
recNo = tags[1].text.split(':\xa0')[1]

neg = tags[2].text.split(':\xa0')[0]
negNo = tags[2].text.split(':\xa0')[1]

pend = tags[3].text.split(':\xa0')[0]
pendNo = tags[3].text.split(':\xa0')[1]

file.write(pos + ", " + posNo + "\n")
file.write(recov + ", " + recNo + "\n")
file.write(neg + ", " + negNo + "\n")
file.write(pend + ", " + pendNo + "\n")

file.close()

if (pos == 'Positive') and (pend == 'Pending'):
    print("US Virgin Islands scraper is complete.")
else:
    print("ERROR: Must fix US Virgin Islands scraper.")

