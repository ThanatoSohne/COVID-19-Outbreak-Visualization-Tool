import csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import geocoder

bno = ('https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vR30F8lYP3jG7YOq8es0PBpJIE5yvRVZffOyaqC0GgMBN6yt0Q-NI8pxS7hd1F9dYXnowSC6zpZmW9D/pubhtml/sheet?headers=false&gid=0&range=A1:I193')

bypass = {'User-Agent': 'Mozilla/5.0'}

bClient = Request(bno, headers=bypass)
bnoPage = urlopen(bClient)

site_parse = soup(bnoPage, 'lxml')
bnoPage.close()

tables = site_parse.find("table", {"class": "waffle no-grid"})

tags = tables.findAll('tr')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')

csvfile = "COVID-19_world_cases_bnoNews.csv"
headers = "Country,Latitude,Longitude,Cases,New Cases,Deaths,New Deaths,Percent of Deaths,Serious & Critical,Recovered\n"

curacao = geocoder.opencage("Curaçao", key='bf1344578b6f462c9183655c80b12d1e')

file = open(csvfile, "w")
file.write(headers)

for tag in tags[8:177]:
    pull = tag.findAll('td')
    locale = geocoder.opencage(pull[0].text, key='bf1344578b6f462c9183655c80b12d1e')
    file.write(pull[0].text + ", " + str(locale.latlng).strip('[]') + ", "  
                     + pull[1].text.replace(',','')  + ", " + pull[2].text.replace(',','') + ", "
                     + pull[3].text.replace(',','') + ", " + pull[4].text.replace(',','')+ ", " + pull[5].text + ", "
                     + pull[6].text.replace(',','') + ", " + pull[7].text.replace(',','') + "\n")

file.write(tags[177].find('td').text + ", " + str(curacao.latlng).strip('[]') + ", "  
           + tags[177].findAll('td')[1].text.replace(',','')  + ", " + tags[177].findAll('td')[2].text.replace(',','') + ", "
           + tags[177].findAll('td')[3].text.replace(',','') + ", " + tags[177].findAll('td')[4].text.replace(',','')+ ", " + tags[177].findAll('td')[5].text + ", "
           + tags[177].findAll('td')[6].text.replace(',','') + ", " + tags[177].findAll('td')[7].text.replace(',','') + "\n")

for tag in tags[178:196]:
    pull = tag.findAll('td')
    locale = geocoder.opencage(pull[0].text, key='bf1344578b6f462c9183655c80b12d1e')
    file.write(pull[0].text + ", " + str(locale.latlng).strip('[]') + ", "  
                     + pull[1].text.replace(',','')  + ", " + pull[2].text.replace(',','') + ", "
                     + pull[3].text.replace(',','') + ", " + pull[4].text.replace(',','')+ ", " + pull[5].text + ", "
                     + pull[6].text.replace(',','') + ", " + pull[7].text.replace(',','') + "\n")
        

file.close()



