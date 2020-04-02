import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

hidoh = 'https://health.hawaii.gov/coronavirusdisease2019/what-you-should-know/current-situation-in-hawaii/'

hiClient = req(hidoh)

site_parse = soup(hiClient.read(), "lxml")
hiClient.close()

tables = site_parse.find("div", {"id": "inner-wrap"}).find('tbody')

#tables = site_parse.find("div", {"id":"inner-wrap"}).find("dl", {"class": "data_list"})
#
#mort = site_parse.find("div", {"id": "inner-wrap"}).find("div", {"class": "column col2"}).findAll('dd')[1]
#
#pull = tables.get_text().split('\n')

csvfile = "COVID-19_cases_hidoh.csv"
headers = "County, HI Residents, Non-HI Residents, Total Cases \n"

file = open(csvfile, "w")
file.write(headers)

tags = tables.findAll('tr')

for t in tags[2:9]:
    pull = t.findAll('td')
    #print(pull[0].text, pull[1].text.split(' (')[0], pull[2].text.split(' (')[0], pull[3].text.split(' (')[0])
    file.write(pull[0].text+", "+pull[1].text.split(' (')[0]+", "+pull[2].text.split(' (')[0]+", "+pull[3].text.split(' (')[0]+"\n")

file.close()

if (tags[2].find('td').text) == 'Hawaii' and (tags[8].find('td').text) == 'Total (new)':
    print("Hawai'i scraper is complete.\n")
else:
    print("ERROR: Must fix Hawai'i scraper.\n")