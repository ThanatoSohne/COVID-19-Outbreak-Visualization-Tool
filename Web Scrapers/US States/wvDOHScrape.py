import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

wvDOH = 'https://dhhr.wv.gov/COVID-19/Pages/default.aspx'

wvClient = req(wvDOH)

site_parse = soup(wvClient.read(), "lxml")
wvClient.close()

tables = site_parse.find("td", {"id": "MSOZoneCell_WebPartWPQ1"}).find('p')

csvfile = "COVID-19_cases_wvdoh.csv"
headers = "County, Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = tables.get_text()

cNo = hold.split(' ')

file.write(cNo[4] + ", " + cNo[5].strip('(),') + "\n")
file.write(cNo[6] + ", " + cNo[7].strip('(),') + "\n")
file.write(cNo[8] + ", " + cNo[9].strip('(),') + "\n")
file.write(cNo[10] + ", " + cNo[11].strip('(),') + "\n")
file.write(cNo[12] + ", " + cNo[13].strip('(),') + "\n")
file.write(cNo[14] + ", " + cNo[15].strip('(),') + "\n")
file.write(cNo[16] + ", " + cNo[17].strip('(),') + "\n")
file.write(cNo[18] + ", " + cNo[19].strip('(),') + "\n")
file.write(cNo[20] + ", " + cNo[21].strip('(),') + "\n")
file.write(cNo[22] + ", " + cNo[23].strip('(),') + "\n")
file.write(cNo[24] + ", " + cNo[25].strip('(),') + "\n")
file.write(cNo[26] + ", " + cNo[27].strip('(),') + "\n")
file.write(cNo[28] + ", " + cNo[29].strip('(),') + "\n")
file.write(cNo[30] + ", " + cNo[31].strip('(),') + "\n")
file.write(cNo[32] + ", " + cNo[33].strip('(),') + "\n")
file.write(cNo[34] + ", " + cNo[35].strip('(),') + "\n")
file.write(cNo[36] + ", " + cNo[37].strip('(),') + "\n")
file.write(cNo[38] + ", " + cNo[39].strip('(),') + "\n")
file.write(cNo[40] + ", " + cNo[41].strip('(),') + "\n")
file.write(cNo[42] + ", " + cNo[43].strip('(),') + "\n")
file.write(cNo[44] + ", " + cNo[45].strip('(),') + "\n")
file.write(cNo[46] + ", " + cNo[47].strip('(),') + "\n")
file.write(cNo[48] + ", " + cNo[49].strip('(),') + "\n")
file.write(cNo[50] + ", " + cNo[51].strip('(),') + "\n")
file.write(cNo[52] + ", " + cNo[53].strip('(),') + "\n")
file.write(cNo[54] + ", " + cNo[55].strip('(),') + "\n")
file.write(cNo[56] + ", " + cNo[57].strip('(),') + "\n")
file.write(cNo[58] + ", " + cNo[59].strip('(),') + "\n")
file.write(cNo[60] + ", " + cNo[61].strip('(),') + "\n")
file.write(cNo[62] + ", " + cNo[63].strip('(),') + "\n")

file.close()

if cNo[4] == 'Barbour' and cNo[62] == 'Wood':
    print("West Virginia scraper is complete.")
else:
    print("ERROR: Must fix West Virginia scraper.")



