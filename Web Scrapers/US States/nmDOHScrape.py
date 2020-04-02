import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

nmDOH = 'https://cv.nmhealth.org/cases-by-county/'

nmClient = req(nmDOH)

site_parse = soup(nmClient.read(), "lxml")
nmClient.close()

tables = site_parse.find("div", {"class": "et_pb_section et_pb_section_2 et_pb_with_background et_section_regular"}).find("tbody")

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_nmdoh.csv"
headers = "County, Cases, Deaths \n"

file = open(csvfile, "w")
file.write(headers)

for tag in tags[1:]:
    pull = tag.findAll('td')
    #print("County = %s, Cases = %s, Deaths = %s" % \
     #     (pull[0].text, pull[1].text, pull[2].text))
    file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

file.close()
    
if (tags[1].find('td').text) == 'Bernalillo County' and (tags[33].find('td').text) == 'Valencia County':
    print("New Mexico scraper is complete.\n")
else:
    print("ERROR: Must fix New Mexico scraper.\n")

