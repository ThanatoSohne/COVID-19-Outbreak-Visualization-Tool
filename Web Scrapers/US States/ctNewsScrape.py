from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

ctNews = 'https://www.nbcconnecticut.com/news/local/this-is-where-there-are-confirmed-cases-of-coronavirus-in-connecticut/2243429/'

bypass = {'User-Agent': 'Mozilla/5.0'}

ctClient = Request(ctNews, headers=bypass)
ctPage = urlopen(ctClient)

site_parse = soup(ctPage.read(), 'lxml')
ctPage.close()

tables = site_parse.find("div", {"class": "article-content rich-text"})

listed = tables.findAll('ul')[0]

tags = listed.findAll('li')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ct = "CONNECTICUT"

csvfile = "COVID-19_cases_ctNews.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, , , , , Pending \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for li in tags:
    take = li.get_text()
    hold.append(take)
    
for h in hold[:8]:
    locale = liegen.geocode(h.split('County')[0] + 'County' + ", " + ct)
    file.write(h.split('County')[0] + ", " + ct + ", " + str(locale.latitude) + 
               ", " + str(locale.longitude) + ", " + h.split('County')[1].strip().replace(',','') +
               "\n")
    sleep(1)

file.write(ct + ", " + ct + ", " + str(liegen.geocode(ct).latitude) + ", " 
            + str(liegen.geocode(ct).longitude) + ", " + "" + ", " + "" 
            + ", " + "" + ", " + "" + ", " + "" + ", " + hold[8].split('validation')[1].strip() + "\n")

file.close()

if hold[0].split('County')[0].strip() == 'Fairfield' and hold[8].split('validation')[0].strip() == 'Pending address':
    print("Connecticut scraper is complete.")
else:
    print("ERROR: Must fix Connecticut scraper.")

#fair = hold[0].split(' County ')
##print(fair)
#fairC = fair[0]
#fairN = fair[1]
#file.write(fairC + ", " + fairN.replace(',', '') + "\n")
#
#
#hart = hold[1].split(' County ')
##print(hart)
#hartC = hart[0]
#hartN = hart[1]
#file.write(hartC + ", " + hartN.replace(',', '') + "\n")
#
#litch = hold[2].split(' County ')
##print(litch)
#litC = litch[0]
#litN = litch[1]
#file.write(litC + ", " + litN.replace(',', '') + "\n")
#
#midd = hold[3].split(' County ')
##print(midd)
#midC = midd[0]
#midN = midd[1]
#file.write(midC + ", " + midN.replace(',', '') + "\n")
#
#newHa = hold[4].split(' County ')
##print(newHa)
#nhC = newHa[0]
#nhN = newHa[1]
#file.write(nhC + ", " + nhN.replace(',', '') + "\n")
#
#newLo = hold[5].split(' County ')
##print(newLo)
#nlC = newLo[0]
#nlN = newLo[1]
#file.write(nlC + ", " + nlN.replace(',', '') + "\n")
#
#toll = hold[6].split(' County ')
##print(toll)
#tollC = toll[0]
#tollN = toll[1]
#file.write(tollC + ", " + tollN.replace(',', '') + "\n")
#
#wind = hold[7].split(' County ')
##print(wind)
#windC = wind[0]
#windN = wind[1]
#file.write(windC + ", " + windN.replace(',', '') + "\n")


    
