from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

sdDOH = 'https://doh.sd.gov/news/Coronavirus.aspx'

sdClient = req(sdDOH)

site_parse = soup(sdClient.read(), "lxml")
sdClient.close()

tables = site_parse.find("div", {"id": "content_block"}).findAll("table")[2]
tables1 = site_parse.find("div", {"id": "content_block"}).findAll("table")[1]

tags = tables.findAll('td')
tages = tables1.findAll('td')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
sd = "SOUTH DAKOTA"
co = ' County'

csvfile = "COVID-19_cases_sddoh.csv"
headers = "County, State, Latitude, Longitude, Total Positive Cases, Recovered\n"

file = open(csvfile, "w")
file.write(headers)

hold = []
holdE = []

for t in tags:
    take = t.get_text()
    hold.append(take)

for ta in tages:
    taken = ta.get_text()
    holdE.append(taken)

locale1 = liegen.geocode(hold[0].strip() + co + ", " + sd)
file.write(hold[0].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[1].strip() + ", " + hold[2].strip() + "\n")
sleep(1)
locale2 = liegen.geocode(hold[3].strip() + co + ", " + sd)
file.write(hold[3].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[4].strip() + ", " + hold[5].strip() + "\n")
sleep(1)
locale3 = liegen.geocode(hold[6].strip() + co + ", " + sd)
file.write(hold[6].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[7].strip() + ", " + hold[8].strip() + "\n")
sleep(1)
locale4 = liegen.geocode(hold[9].strip() + co + ", " + sd)
file.write(hold[9].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[10].strip() + ", " + hold[11].strip() + "\n")
sleep(1)
locale5 = liegen.geocode(hold[12].strip() + co + ", " + sd)
file.write(hold[12].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[13].strip() + ", " + hold[14].strip() + "\n")
sleep(1)
locale6 = liegen.geocode(hold[15].strip() + co + ", " + sd)
file.write(hold[15].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[16].strip() + ", " + hold[17].strip() + "\n")
sleep(1)
locale7 = liegen.geocode(hold[18].strip() + co + ", " + sd)
file.write(hold[18].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[19].strip() + ", " + hold[20].strip() + "\n")
sleep(1)
locale8 = liegen.geocode(hold[21].strip() + co + ", " + sd)
file.write(hold[21].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[22].strip() + ", " + hold[23].strip() + "\n")
sleep(1)
locale9 = liegen.geocode(hold[24].strip() + co + ", " + sd)
file.write(hold[24].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[25].strip() + ", " + hold[26].strip() + "\n")
sleep(1)
locale10 = liegen.geocode(hold[27].strip() + co + ", " + sd)
file.write(hold[27].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[28].strip() + ", " + hold[29].strip() + "\n")
sleep(1)
locale11 = liegen.geocode(hold[30].strip() + co + ", " + sd)
file.write(hold[30].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[31].strip() + ", " + hold[32].strip() + "\n")
sleep(1)
locale12 = liegen.geocode(hold[33].strip() + co + ", " + sd)
file.write(hold[33].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[34].strip() + ", " + hold[35].strip() + "\n")
sleep(1)
locale13 = liegen.geocode(hold[36].strip() + co + ", " + sd)
file.write(hold[36].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[37].strip() + ", " + hold[38].strip() + "\n")
sleep(1)
locale14 = liegen.geocode(hold[0].strip() + co + ", " + sd)
file.write(hold[39].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[40].strip() + ", " + hold[41].strip() + "\n")
sleep(1)
locale15 = liegen.geocode(hold[42].strip() + co + ", " + sd)
file.write(hold[42].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[43].strip() + ", " + hold[44].strip() + "\n")
sleep(1)
locale16 = liegen.geocode(hold[45].strip() + co + ", " + sd)
file.write(hold[45].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[46].strip() + ", " + hold[47].strip() + "\n")
sleep(1)
locale17 = liegen.geocode(hold[48].strip() + co + ", " + sd)
file.write(hold[48].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[49].strip() + ", " + hold[50].strip() + "\n")
sleep(1)
locale18 = liegen.geocode(hold[51].strip() + co + ", " + sd)
file.write(hold[51].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[52].strip() + ", " + hold[53].strip() + "\n")
sleep(1)
locale19 = liegen.geocode(hold[54].strip() + co + ", " + sd)
file.write(hold[54].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[55].strip() + ", " + hold[56].strip() + "\n")
sleep(1)
locale20 = liegen.geocode(hold[57].strip() + co + ", " + sd)
file.write(hold[57].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[58].strip() + ", " + hold[59].strip() + "\n")
sleep(1)
locale21 = liegen.geocode(hold[60].strip() + co + ", " + sd)
file.write(hold[60].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[61].strip() + ", " + hold[62].strip() + "\n")
sleep(1)
locale22 = liegen.geocode(hold[63].strip() + co + ", " + sd)
file.write(hold[63].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[64].strip() + ", " + hold[65].strip() + "\n")
sleep(1)
locale23 = liegen.geocode(hold[66].strip() + co + ", " + sd)
file.write(hold[66].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[67].strip() + ", " + hold[68].strip() + "\n")
sleep(1)
locale24 = liegen.geocode(hold[69].strip() + co + ", " + sd)
file.write(hold[69].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[70].strip() + ", " + hold[71].strip() + "\n")
sleep(1)
locale25 = liegen.geocode(hold[72].strip() + co + ", " + sd)
file.write(hold[72].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[73].strip() + ", " + hold[74].strip() + "\n")
sleep(1)
locale26 = liegen.geocode(hold[75].strip() + co + ", " + sd)
file.write(hold[75].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[76].strip() + ", " + hold[77].strip() + "\n")
sleep(1)
locale27 = liegen.geocode(hold[78].strip() + co + ", " + sd)
file.write(hold[78].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[79].strip() + ", " + hold[80].strip() + "\n")
sleep(1)
locale28 = liegen.geocode(hold[81].strip() + co + ", " + sd)
file.write(hold[81].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[82].strip() + ", " + hold[83].strip() + "\n")
sleep(1)
locale29 = liegen.geocode(hold[84].strip() + co + ", " + sd)
file.write(hold[84].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[85].strip() + ", " + hold[86].strip() + "\n")
sleep(1)
locale30 = liegen.geocode(hold[87].strip() + co + ", " + sd)
file.write(hold[87].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[88].strip() + ", " + hold[89].strip() + "\n")
sleep(1)
locale31 = liegen.geocode(hold[90].strip() + co + ", " + sd)
file.write(hold[90].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
           + str(locale1.longitude) + ", " + hold[91].strip() + ", " + hold[92].strip() + "\n")
sleep(1)

file.write("\n")
file.write("#######, #########, ######### \n")

krankenhaus = holdE[2:4]
haus = krankenhaus[0]
hausNo = krankenhaus[1]
file.write(haus + ", " + hausNo + "\n")

deaths = holdE[4:6]
mort = deaths[0]
mortNo = deaths[1]
file.write(mort + ", " + mortNo + "\n")

recovered = holdE[6:8]
hope = recovered[0]
hopeN = recovered[1]
file.write(hope + ", " + hopeN + "\n")


file.close()

if (hold[0].strip()) == 'Aurora' and (hold[90].strip()) ==  'Yankton' and hope == 'Recovered':
    print("South Dakota scraper is complete.")
else:
    print("ERROR: Must fix South Dakota scraper.")