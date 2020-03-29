import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup


akdoh = 'http://dhss.alaska.gov/dph/Epi/id/Pages/COVID-19/monitoring.aspx'

akClient = req(akdoh)

site_parse = soup(akClient.read(), 'lxml')
akClient.close()

tables = site_parse.find("div", {"class": "grid3"})

#regTable = tables.find("table")

tags = tables.findAll('tr')

csvfile = "COVID-19_cases_akdoh.csv"
headers = "Region, Total Cases \n"
    
with open(csvfile, 'w', encoding = 'utf-8') as f:
    f.write(headers)
    
    anch = tags[1].text.split('\n')
    anR = anch[1].split('\xa0')
    anR1 = anR[1]
    anT = anch[6]
    f.write(anR1 + ", " + anT + "\n")
    
    gulf = tags[5].text.split('\n')
    gulfR = gulf[1].split('\xa0')
    gulfR1 = gulfR[1]
    gulfT = gulf[6]
    f.write(gulfR1 + ", " + gulfT +"\n")
    
    intr = tags[10].text.split('\n')
    intrR = intr[1].split('\xa0')
    intrR1 = intrR[1]
    intrT = intr[6]
    f.write(intrR1 + ", " + intrT + "\n")
    
    matsu = tags[13].text.split('\n')
    matsuR = matsu[1].split('\xa0')
    matsuR1 = matsuR[1]
    matsuT = matsu[6]
    f.write(matsuR1 + ", " + matsuT + "\n")
    
    nort = tags[15].text.split('\n')
    nortR = nort[1].split('\xa0')
    nortR1 = nortR[1]
    nortT = nort[6]
    f.write(nortR1 + ", " + nortT + "\n")
    
    se = tags[16].text.split('\n')
    seR = se[1].split('\xa0')
    seR1 = seR[1]
    seT = se[6]
    f.write(seR1 + ", " + seT + "\n")
    
    sw = tags[19].text.split('\n')
    swR = sw[1].split('\xa0')
    swR1 = swR[1]
    swT = sw[6]
    f.write(swR1 + ", " + swT + "\n")
    
    
#    for tag in tags[1:]:
#        pull = tag.findAll('p')
#        print("Region = %s, Total = %s" % \
#              (pull[0].text, pull[5].text))
#        f.write(pull[0].text + ", " + pull[5].text + "\n")

f.close()

