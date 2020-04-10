from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

vtWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Vermont'

vtClient = req(vtWiki)

site_parse = soup(vtClient.read(), "lxml")
vtClient.close()

tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
vt = "VERMONT"
co = ' County'

csvfile = "COVID-19_cases_vtWiki.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

for h in hold[50:65]:
    take = h.split('\n')
    locale = liegen.geocode(take[1] + co + ", " + vt)
    file.write(take[1] + ", " + vt + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + take[3] + "\n")
    sleep(1)

file.write(hold[63].split('\n')[1] + ", " + vt + ", " + "" + ", "
               + "" + ", " + hold[63].split('\n')[3] + "\n")

file.close()

if (hold[50].split('\n')[1]) == 'Addison' and (hold[64].split('\n')[1]) == 'N/A[a]':
    print("Vermont scraper is complete.")
else:
    print("ERROR: Must fix Vermont scraper.")







