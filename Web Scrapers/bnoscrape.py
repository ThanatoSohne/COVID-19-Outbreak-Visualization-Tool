import bs4
import csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

bno = ('https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vR30F8lYP3jG7YOq8es0PBpJIE5yvRVZffOyaqC0GgMBN6yt0Q-NI8pxS7hd1F9dYXnowSC6zpZmW9D/pubhtml/sheet?headers=false&gid=0&range=A1:I193')

bypass = {'User-Agent': 'Mozilla/5.0'}

bClient = Request(bno, headers=bypass)
bnoPage = urlopen(bClient)

site_parse = soup(bnoPage, 'lxml')
bnoPage.close()

tables = site_parse.find("table", {"class": "waffle no-grid"})

#print(tables)

tags = tables.findAll('tr')

csvfile = "COVID-19_world_cases_bnoNews.csv"
#header = ("Country, Cases, New Cases, Deaths, New Deaths, Percent of Deaths, \
#          Serious & Critical, Recovered \n")

#file = open(csvfile, "w", encoding = 'utf-8')
#file.write(header)

with open(csvfile, 'w', newline='') as f:
    bnoNews = csv.writer(f)
    bnoNews.writerow([u"Country", u"Cases", u"New Cases", u"Deaths", u"New Deaths",
                      u"Percent of Deaths", u"Serious & Critical", u"Recovered"])

    for tag in tags[8:]:
        pull = tag.findAll('td')
        #print(pull)
        #print("Country = %s, Cases = %s, New Cases = %s, Deaths = %s, New Deaths = %s, Percent of Deaths = %s, Serious and Critical = %s, Recovered = %s\n" % \
        #      (pull[0].text, pull[1].text, pull[2].text, pull[3].text, pull[4].text, pull[5].text, pull[6].text, pull[7].text))
        bnoNews.writerow([pull[0].text] + [pull[1].text]  + [pull[2].text] 
                          + [pull[3].text] + [pull[4].text] + [pull[5].text] 
                          + [pull[6].text] + [pull[7].text] )

f.close()



