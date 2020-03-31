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

file.write(hold[0].strip() + ", " + hold[1].strip() + "\n")
file.write(hold[2].strip() + ", " + hold[3].strip() + "\n")
file.write(hold[4].strip() + ", " + hold[5].strip() + "\n")
file.write(hold[6].strip() + ", " + hold[7].strip() + "\n")
file.write(hold[8].strip() + ", " + hold[9].strip() + "\n")
file.write(hold[10].strip() + ", " + hold[11].strip() + "\n")
file.write(hold[12].strip() + ", " + hold[13].strip() + "\n")
file.write(hold[14].strip() + ", " + hold[15].strip() + "\n")
file.write(hold[16].strip() + ", " + hold[17].strip() + "\n")
file.write(hold[18].strip() + ", " + hold[19].strip() + "\n")
file.write(hold[20].strip() + ", " + hold[21].strip() + "\n")
file.write(hold[22].strip() + ", " + hold[23].strip() + "\n")
file.write(hold[24].strip() + ", " + hold[25].strip() + "\n")
file.write(hold[26].strip() + ", " + hold[27].strip() + "\n")
file.write(hold[28].strip() + ", " + hold[29].strip() + "\n")
file.write(hold[30].strip()+ ", " + hold[31].strip()+ "\n")
file.write(hold[32].strip() + ", " + hold[33].strip() + "\n")
file.write(hold[34].strip() + ", " + hold[35].strip() + "\n")
file.write(hold[36].strip() + ", " + hold[37].strip() + "\n")
file.write(hold[38].strip() + ", " + hold[39].strip() + "\n")
file.write(hold[40].strip() + ", " + hold[41].strip() + "\n")
file.write(hold[42].strip() + ", " + hold[43].strip() + "\n")
file.write(hold[44].strip() + ", " + hold[45].strip() + "\n")
file.write(hold[46].strip() + ", " + hold[47].strip() + "\n")
file.write(hold[48].strip() + ", " + hold[49].strip() + "\n")
file.write(hold[50].strip() + ", " + hold[51].strip() + "\n")
file.write(hold[52].strip() + ", " + hold[53].strip() + "\n")
file.write(hold[54].strip() + ", " + hold[55].strip() + "\n")
file.write(hold[56].strip() + ", " + hold[57].strip() + "\n")
file.write(hold[58].strip() + ", " + hold[59].strip() + "\n")

#aur = hold[0:2]
#aurN = aur.pop(0)
#aurC = aur.pop()
#file.write(aurN + ", " + aurC + "\n")
#
#bea = hold[2:4]
#be = bea.pop(0).split('\n')
#beN = bea.pop().split('\n')
#beaN = be.pop(1)
#beaC = beN.pop(1)
#file.write(beaN + ", " + beaC + "\n")
#
#bon = hold[4:6]
#bo = bon.pop(0).split('\n')
#boN = bon.pop().split('\n')
#bonN = bo.pop(1)
#bonC = boN.pop(1)
#file.write(bonN + ", " + bonC + "\n")
#
#brook = hold[6:8]
#broN = brook.pop(0)
#broC = brook.pop()
#file.write(broN + ", " + broC + "\n")
#
#brown = hold[8:10]
#browN = brown.pop(0)
#browC = brown.pop()
#file.write(browN + ", " + browC + "\n")
#
#charl = hold[10:12]
#charN = charl.pop(0)
#charC = charl.pop()
#file.write(charN + ", " + charC + "\n")
#
#clar = hold[12:14]
#clarN = clar.pop(0)
#clarC = clar.pop()
#file.write(clarN + ", " + clarC + "\n")
#
#clay = hold[14:16]
#clayN = clay.pop(0)
#clayC = clay.pop()
#file.write(clayN + ", " + clayC + "\n")
#
#cod = hold[16:18]
#co = cod.pop(0).split('\n')
#coN = cod.pop().split('\n')
#codN = co.pop(1)
#codC = coN.pop(1)
#file.write(codN + ", " + codC + "\n")
#
#dav = hold[18:20]
#da = dav.pop(0).split('\n')
#daN = dav.pop().split('\n')
#davN = da.pop(1)
#davC = daN.pop(1)
#file.write(davN + ", " + davC + "\n")
#
#deu = hold[20:22]
#de = deu.pop(0).split('\n')
#deN = deu.pop().split('\n')
#deuN = de.pop(1)
#deuC = deN.pop(1)
#file.write(deuN + ", " + deuC + "\n")
#
#fall = hold[22:24]
#fallN = fall.pop(0)
#fallC = fall.pop()
#file.write(fallN + ", " + fallC + "\n")
#
#fau = hold[24:26]
#fa = fau.pop(0).split('\n')
#faN = fau.pop().split('\n')
#fauN = fa.pop(1)
#faulC = faN.pop(1)
#file.write(fauN + ", " + faulC + "\n")
#
#ham = hold[26:28]
#hamN = ham.pop(0)
#hamC = ham.pop()
#file.write(hamN + ", " + hamC + "\n")
#
#hughes = hold[28:30]
#hugN = hughes.pop(0)
#hugC = hughes.pop()
#file.write(hugN + ", " + hugC + "\n")
#
#hutch = hold[30:32]
#hutN = hutch.pop(0)
#hutC = hutch.pop()
#file.write(hutN + ", " + hutC + "\n")
#
#law = hold[32:34]
#lawN = law.pop(0)
#lawC = law.pop()
#file.write(lawN + ", " + lawC + "\n")
#
#linc = hold[34:36]
#lincN = linc.pop(0)
#linC = linc.pop()
#file.write(lincN + ", " + linC + "\n")
#
#lym = hold[36:38]
#lymN = lym.pop(0)
#lymC = lym.pop()
#file.write(lymN + ", " + lymC + "\n")
#
#mcc = hold[38:40]
#mc = mcc.pop(0).split('\n')
#mcN = mcc.pop().split('\n')
#mccN = mc.pop(1)
#mccC = mcN.pop(1)
#file.write(mccN + ", " + mccC + "\n")
#
#mea = hold[40:42]
#me = mea.pop(0).split('\n')
#meN = mea.pop().split('\n')
#meaN = me.pop(1)
#meaC = meN.pop(1)
#file.write(meaN + ", " + meaC + "\n")
#
#minne = hold[42:44]
#mi = minne.pop(0).split('\n')
#miN = minne.pop().split('\n')
#minN = mi.pop(1)
#minC = miN.pop(1)
#file.write(minN + ", " + minC + "\n")
#
#penn = hold[44:46]
#penN = penn.pop(0)
#pennC = penn.pop()
#file.write(penN + ", " + pennC + "\n")
#
#rob = hold[46:48]
#robN = rob.pop(0)
#robC = rob.pop()
#file.write(robN + ", " + robC + "\n")
#
#todd = hold[48:50]
#to = todd.pop(0).split('\n')
#toN = todd.pop().split('\n')
#todN = to.pop(1)
#todC = toN.pop(1)
#file.write(todN + ", " + todC + "\n")
#
#turn = hold[50:52]
#turN = turn.pop(0)
#turC = turn.pop()
#file.write(turN + ", " + turC + "\n")
#
#uni = hold[52:54]
#uniN = uni.pop(0)
#uniC = uni.pop()
#file.write(uniN + ", " + uniC + "\n")
#
#yan = hold[54:56]
#yaN = yan.pop(0)
#yanC = yan.pop()
#file.write(yaN + ", " + yanC + "\n")

file.write("\n")
file.write("Deaths and Recoveries \n")
deaths = holdE[2:4]
mort = deaths.pop(0)
mortNo = deaths.pop()
file.write(mort + ", " + mortNo + "\n")

recovered = holdE[4:6]
hope = recovered.pop(0)
hopeN = recovered.pop()
file.write(hope + ", " + hopeN + "\n")


file.close()