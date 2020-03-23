import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

akdoh = 'http://dhss.alaska.gov/dph/Epi/id/Pages/COVID-19/monitoring.aspx'

akClient = req(akdoh)

site_parse = soup(akClient.read(), 'lxml')
akClient.close()

tables = site_parse.find("div", {"class": "grid2"})

regTable = tables.find("table")

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_akdoh.csv"
headers = "Region, Travel Related, Non Travel Related, Total\n"

with open(csvfile, 'w', encoding = 'utf-8') as f:
    f.write(headers)

    for tag in tags[1:8]:
        pull = tag.findAll('p')
        print("Region = %s, Travel Related = %s, Non-Travel Related = %s, Total = %s" % \
              (pull[0].text, pull[1].text, pull[2].text, pull[3].text))
        f.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + ", " + pull[3].text + "\n")

f.close()
    