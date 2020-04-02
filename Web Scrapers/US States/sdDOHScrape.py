import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

sdDOH = 'https://doh.sd.gov/news/Coronavirus.aspx'

sdClient = req(sdDOH)

site_parse = soup(sdClient.read(), "lxml")
sdClient.close()

tables = site_parse.find("div", {"id": "content_block"}).findAll("table")[2]
tables1 = site_parse.find("div", {"id": "content_block"}).findAll("table")[1]

tags = tables.findAll('td')
tages = tables1.findAll('td')

csvfile = "COVID-19_cases_sddoh.csv"
headers = "County, Cases \n"

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

file.write(hold[0].strip() + ", " + hold[1].strip() + ", " + hold[2].strip() + "\n")
file.write(hold[3].strip() + ", " + hold[4].strip() + ", " + hold[5].strip() + "\n")
file.write(hold[6].strip() + ", " + hold[7].strip() + ", " + hold[8].strip() + "\n")
file.write(hold[9].strip() + ", " + hold[10].strip() + ", " + hold[11].strip() + "\n")
file.write(hold[12].strip() + ", " + hold[13].strip() + ", " + hold[14].strip() + "\n")
file.write(hold[15].strip() + ", " + hold[16].strip() + ", " + hold[17].strip() + "\n")
file.write(hold[18].strip() + ", " + hold[19].strip() + ", " + hold[20].strip() + "\n")
file.write(hold[21].strip() + ", " + hold[22].strip() + ", " + hold[23].strip() + "\n")
file.write(hold[24].strip() + ", " + hold[25].strip() + ", " + hold[26].strip() + "\n")
file.write(hold[27].strip() + ", " + hold[28].strip() + ", " + hold[29].strip() + "\n")
file.write(hold[30].strip() + ", " + hold[31].strip() + ", " + hold[32].strip() + "\n")
file.write(hold[33].strip() + ", " + hold[34].strip() + ", " + hold[35].strip() + "\n")
file.write(hold[36].strip() + ", " + hold[37].strip() + ", " + hold[38].strip() + "\n")
file.write(hold[39].strip() + ", " + hold[40].strip() + ", " + hold[41].strip() + "\n")
file.write(hold[42].strip() + ", " + hold[43].strip() + ", " + hold[44].strip() + "\n")
file.write(hold[45].strip() + ", " + hold[46].strip() + ", " + hold[47].strip() + "\n")
file.write(hold[48].strip() + ", " + hold[49].strip() + ", " + hold[50].strip() + "\n")
file.write(hold[51].strip() + ", " + hold[52].strip() + ", " + hold[53].strip() + "\n")
file.write(hold[54].strip() + ", " + hold[55].strip() + ", " + hold[53].strip() + "\n")
file.write(hold[57].strip() + ", " + hold[58].strip() + ", " + hold[59].strip() + "\n")
file.write(hold[60].strip() + ", " + hold[61].strip() + ", " + hold[62].strip() + "\n")
file.write(hold[63].strip() + ", " + hold[64].strip() + ", " + hold[65].strip() + "\n")
file.write(hold[66].strip() + ", " + hold[67].strip() + ", " + hold[68].strip() + "\n")
file.write(hold[69].strip() + ", " + hold[70].strip() + ", " + hold[71].strip() + "\n")
file.write(hold[72].strip() + ", " + hold[73].strip() + ", " + hold[74].strip() + "\n")
file.write(hold[75].strip() + ", " + hold[76].strip() + ", " + hold[77].strip() + "\n")
file.write(hold[78].strip() + ", " + hold[79].strip() + ", " + hold[80].strip() + "\n")
file.write(hold[81].strip() + ", " + hold[82].strip() + ", " + hold[83].strip() + "\n")
file.write(hold[84].strip() + ", " + hold[85].strip() + ", " + hold[86].strip() + "\n")

file.write("\n")
file.write("Deaths, Recoveries, Hospitalized \n")

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

if (hold[0].strip()) == 'Aurora' and (hold[84].strip()) ==  'Yankton' and hope == 'Recovered':
    print("South Dakota scraper is complete.\n")
else:
    print("ERROR: Must fix South Dakota scraper.\n")