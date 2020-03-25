import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

ctNews = 'https://www.nbcconnecticut.com/news/local/this-is-where-there-are-confirmed-cases-of-coronavirus-in-connecticut/2243429/'

bypass = {'User-Agent': 'Mozilla/5.0'}

ctClient = Request(ctNews, headers=bypass)
ctPage = urlopen(ctClient)

site_parse = soup(ctPage.read(), 'lxml')
ctPage.close()

tables = site_parse.find("div", {"class": "article-content rich-text"})

listed = tables.find('ul')

tags = listed.findAll('li')

csvfile = "COVID-19_cases_ctNews.csv"
headers = "County, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for li in tags:
    take = li.get_text()
    hold.append(take)

fair = hold[0].split(' County ')
#print(fair)
fairC = fair.pop(0)
fairN = fair.pop()
file.write(fairC + ", " + fairN + "\n")


hart = hold[1].split(' County ')
#print(hart)
hartC = hart.pop(0)
hartN = hart.pop()
file.write(hartC + ", " + hartN + "\n")

litch = hold[2].split(' County ')
#print(litch)
litC = litch.pop(0)
litN = litch.pop()
file.write(litC + ", " + litN + "\n")

midd = hold[3].split(' County ')
#print(midd)
midC = midd.pop(0)
midN = midd.pop()
file.write(midC + ", " + midN + "\n")

newHa = hold[4].split(' County ')
#print(newHa)
nhC = newHa.pop(0)
nhN = newHa.pop()
file.write(nhC + ", " + nhN + "\n")

newLo = hold[5].split(' County ')
#print(newLo)
nlC = newLo.pop(0)
nlN = newLo.pop()
file.write(nlC + ", " + nlN + "\n")

toll = hold[6].split(' County ')
#print(toll)
tollC = toll.pop(0)
tollN = toll.pop()
file.write(tollC + ", " + tollN + "\n")

wind = hold[7].split(' County ')
#print(wind)
windC = wind.pop(0)
windN = wind.pop()
file.write(windC + ", " + windN + "\n")

file.close()
    
