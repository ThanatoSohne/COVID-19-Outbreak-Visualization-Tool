import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

hidoh = 'https://health.hawaii.gov/coronavirusdisease2019/'

hiClient = req(hidoh)

site_parse = soup(hiClient.read(), "lxml")
hiClient.close()

tables = site_parse.find("div", {"id":"inner-wrap"}).find("dl", {"class": "data_list"})

mort = site_parse.find("div", {"id": "inner-wrap"}).find("div", {"class": "column col2"}).findAll('dd')[1]

pull = tables.get_text().split('\n')

csvfile = "COVID-19_cases_hidoh.csv"
headers = "County, Positive Cases \n"

file = open(csvfile, "w")
file.write(headers)

total = pull[1].split(': ')[0]
toNo = pull[1].split(': ')[1]
totalNo = toNo.split(' (')[0]

hawaii = pull[2].split(': ')[0]
hTo = pull[2].split(': ')[1]
hawaiiT = hTo.split(' (')[0]
file.write(hawaii + ", " + hawaiiT + "\n")

honolulu = pull[3].split(': ')[0]
honTo = pull[3].split(': ')[1]
honoluluT = honTo.split(' (')[0]
file.write(honolulu + ", " + honoluluT + "\n")

kauai = pull[4].split(': ')[0]
kTo = pull[4].split(': ')[1]
kauaiT = kTo.split(' (')[0]
file.write(kauai + ", " + kauaiT + "\n")

maui = pull[5].split(': ')[0]
mTo = pull[5].split(': ')[1]
mauiT = mTo.split(' (')[0]
file.write(maui + ", " + mauiT + "\n")

pend = pull[6].split(': ')[0]
pTo = pull[6].split(': ')[1]
pendT = [pTo[0].split('|')]
pendNo = pendT.pop()
fin = ''.join(pendNo)
file.write(pend + ", " + fin + "\n")

file.write(total + ", " + totalNo + "\n")
file.write(mort.get_text() + "\n")

file.close()