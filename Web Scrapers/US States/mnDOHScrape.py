import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

mnDOH = 'https://www.health.state.mn.us/diseases/coronavirus/situation.html'

mnClient = req(mnDOH)

site_parse = soup(mnClient.read(), "lxml")
mnClient.close()

tables = site_parse.find("div", {"class": "clearfix"}).findAll("tbody")[2]

tags = tables.findAll('td')

csvfile = "COVID-19_cases_mndoh.csv"
headers = "County, Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for td in tags:
    take = td.get_text()
    hold.append(take)

file.write(hold[0] + ", " + hold[1] + "\n")
file.write(hold[2] + ", " + hold[3] + "\n")
file.write(hold[4] + ", " + hold[5] + "\n")
file.write(hold[6] + ", " + hold[7] + "\n")
file.write(hold[8] + ", " + hold[9] + "\n")
file.write(hold[10] + ", " + hold[11] + "\n")
file.write(hold[12] + ", " + hold[13] + "\n")
file.write(hold[14] + ", " + hold[15] + "\n")
file.write(hold[16] + ", " + hold[17] + "\n")
file.write(hold[18] + ", " + hold[19] + "\n")
file.write(hold[20] + ", " + hold[21] + "\n")
file.write(hold[22] + ", " + hold[23] + "\n")
file.write(hold[24] + ", " + hold[25] + "\n")
file.write(hold[26] + ", " + hold[27] + "\n")
file.write(hold[28] + ", " + hold[29] + "\n")
file.write(hold[30] + ", " + hold[31] + "\n")
file.write(hold[32] + ", " + hold[33] + "\n")
file.write(hold[34] + ", " + hold[35] + "\n")
file.write(hold[36] + ", " + hold[37] + "\n")
file.write(hold[38] + ", " + hold[39] + "\n")
file.write(hold[40] + ", " + hold[41] + "\n")
file.write(hold[42] + ", " + hold[43] + "\n")
file.write(hold[44] + ", " + hold[45] + "\n")
file.write(hold[46] + ", " + hold[47] + "\n")
file.write(hold[48] + ", " + hold[49] + "\n")
file.write(hold[50] + ", " + hold[51] + "\n")
file.write(hold[52] + ", " + hold[53] + "\n")
file.write(hold[54] + ", " + hold[55] + "\n")
file.write(hold[56] + ", " + hold[57] + "\n")
file.write(hold[58] + ", " + hold[59] + "\n")
file.write(hold[60] + ", " + hold[61] + "\n")
file.write(hold[62] + ", " + hold[63] + "\n")
file.write(hold[64] + ", " + hold[65] + "\n")
file.write(hold[66] + ", " + hold[67] + "\n")
file.write(hold[68] + ", " + hold[69] + "\n")
file.write(hold[70] + ", " + hold[71] + "\n")
file.write(hold[72] + ", " + hold[73] + "\n")
file.write(hold[74] + ", " + hold[75] + "\n")
file.write(hold[76] + ", " + hold[77] + "\n")
file.write(hold[78] + ", " + hold[79] + "\n")
file.write(hold[80] + ", " + hold[81] + "\n")
file.write(hold[82] + ", " + hold[83] + "\n")
file.write(hold[84] + ", " + hold[85] + "\n")
file.write(hold[86] + ", " + hold[87] + "\n")
file.write(hold[88] + ", " + hold[89] + "\n")
file.write(hold[90] + ", " + hold[91] + "\n")
file.write(hold[92] + ", " + hold[93] + "\n")
file.write(hold[94] + ", " + hold[95] + "\n")
file.write(hold[96] + ", " + hold[97] + "\n")
file.write(hold[98] + ", " + hold[99] + "\n")
file.write(hold[100] + ", " + hold[101] + "\n")
file.write(hold[102] + ", " + hold[103] + "\n")
file.write(hold[104] + ", " + hold[105] + "\n")
file.write(hold[106] + ", " + hold[107] + "\n")
file.write(hold[108] + ", " + hold[109] + "\n")
file.write(hold[110] + ", " + hold[111] + "\n")

file.close()

if hold[0] == 'Anoka' and hold[110] == 'Yellow Medicine':
    print("Minnesota scraper is complete.\n")
else:
    print("ERROR: Must fix Minnesota scraper.\n")


