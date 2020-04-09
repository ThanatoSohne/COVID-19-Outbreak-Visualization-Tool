from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

kyNews = 'https://www.courier-journal.com/story/news/2020/03/09/coronavirus-kentucky-how-many-cases-and-where-they-kentucky/5001636002/'

kyClient = req(kyNews)

site_parse = soup(kyClient.read(), "lxml")
kyClient.close()

tables = site_parse.find("div", {"class": "asset-double-wide double-wide p402_premium"})

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
ky = "KENTUCKY"

csvfile = "COVID-19_cases_kyNews.csv"
headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths\n"

file = open(csvfile, "w")
file.write(headers)

tag = tables.find_all('p')[12:110]

hold = []

for t in tag:
    take = t.get_text()
    hold.append(take)
    
for h in hold[:89]: 
    locale = liegen.geocode(h.split(':')[0] + ", " + ky)
    file.write(h.split(':')[0] + ", " + ky + ", " + str(locale.latitude) + ", "
               + str(locale.longitude) + ", " + h.split(':')[1].split('c')[0].strip()
               + ", " + h.split('case')[1].strip('; ').strip(' death').replace('\xa0', '').strip(',').strip('s').strip() + "\n")
    sleep(1)
    
file.write(hold[89].split(':')[0] + ", " + ky + ", " + "" + ", " + "" + ", "
           + hold[89].split(':')[1].split('c')[0].strip() + ", "
           + hold[89].split('case')[1].strip('; ').strip(' death').replace('\xa0', '').strip(',').strip('s').strip() + "\n")

file.close()

if (hold[0].split(':')[0]) == 'Adair County' and (hold[89].split(':')[0]) == 'No County Available':
    print("Kentucky scraper is complete.")
else:
    print("ERROR: Must fix Kentucky scraper.")

#allen = hold[0].split(': ')
#allC = allen[0]
#allN = allen[1].split(' ')
#allNo = allN[0]
#file.write(allC + ", " + allNo + "\n")
#
#ander = hold[1].split(': ')
#andC = ander[0]
#andN = ander[1].split(' ')
#andNo = andN[0]
#andD = andN[2]
#file.write(andC + ", " + andNo + ", " + andD + "\n")
#
#boone = hold[2].split(': ')
#booneC = boone[0]
#booneN = boone[1].split(' ')
#booneNo = booneN[0].split('\xa0')[0]
#file.write(booneC + ", " + booneNo + "\n")
#
#bour = hold[3].split(': ')
#bourC = bour[0]
#bourN = bour[1].split(' ')
#bourNo = bourN[0]
#bourD = bourN[2]
#file.write(bourC + ", " + bourNo + ", " + bourD + "\n")
#
#breat = hold[4].split(': ')
#breatC = breat[0]
#breatN = breat[1].split(' ')
#breatNo = breatN[0]
#file.write(breatC + ", " + breatNo + "\n")
#
#bull = hold[5].split(':\xa0')
#bullC = bull[0]
#bullN = bull[1].split(' ')
#bullNo = bullN[0]
#file.write(bullC + ", " + bullNo + "\n")
#
#camp = hold[6].split(': ')
#campC = camp[0]
#campN = camp[1].split(' ')
#campNo = campN[0].split('\xa0')[0]
#file.write(campC + ", " + campNo + "\n")
#
#call = hold[7].split(':')
#callC = call[0]
#callN = call[1].split(' ')
#callNo = callN[0].split('\xa0')[1]
#file.write(callC + ", " + callNo + "\n")
#
#christos = hold[8].split(': ')
#chrC = christos[0]
#chrN = christos[1].split(' ')
#chrNo = chrN[0].split('\xa0')[0]
#file.write(chrC + ", " + chrNo + "\n")
#
#clark = hold[9].split(':\xa0')
#clrC = clark[0]
#clrN = clark[1].split(' ')
#clrNo = clrN[0].split('\xa0')[0]
#file.write(clrC + ", " + clrNo + "\n")
#
#dav = hold[10].split(':')
#davC = dav[0]
#davN = dav[1].split(' ')
#davNo = davN[0].split('\xa0')[1]
#file.write(davC + ", " + davNo + "\n")
#
#fay = hold[11].split(':')
#fayC = fay[0]
#fayN = fay[1].split(' ')
#fayNo = fayN[0].split('\xa0')[1]
#fayD = fayN[1].split('\xa0')[0]
#file.write(fayC + ", " + fayNo + ", " + fayD + "\n")
#
##floyd = hold[12].split(': ')
##flyC = floyd[0]
##flyN = floyd[1].split(' ')
##flyNo = flyN[0]
##file.write(flyC + ", " + flyNo + "\n")
#
#frank = hold[12].split(': ')
#frkC = frank[0]
#frkN = frank[1].split(' ')
#frkNo = frkN[0].split('\xa0')[0]
#file.write(frkC + ", " + frkNo + "\n")
#
#gray = hold[13].split(': ')
#grayC = gray[0]
#grayN = gray[1].split(' ')
#grayNo = grayN[0]
#file.write(grayC + ", " + grayNo + "\n")
#
#hard = hold[14].split(':')
#hardC = hard[0]
#hardN = hard[1].split(' ')
#hardNo = hardN[0].split('\xa0')[1]
#file.write(hardC + ", " + hardNo + "\n")
#
#harr = hold[15].split(': ')
#harrC = harr[0]
#harrN = harr[1].split(' ')
#harrNo = harrN[0]
#file.write(harrC + ", " + harrNo + "\n")
#
#hend = hold[16].split(':')
#henC = hend[0]
#henN = hend[1].split(' ')
#henNo = henN[0].split('\xa0')[1]
#file.write(henC + ", " + henNo + "\n")
#
#hop = hold[17].split(': ')
#hopC = hop[0]
#hopN = hop[1].split(' ')
#hopNo = hopN[0].split('\xa0')[0]
#hopD = hopN[1]
#file.write(hopC + ", " + hopNo + ", " + hopD + "\n")
#
#jeff = hold[18].split(': ')
#jeffC = jeff[0]
#jeffN = jeff[1].split(' ')
#jeffNo = jeffN[0].split('\xa0')[0]
#jeffD = jeffN[1].split('\xa0')[0]
#file.write(jeffC + ", " + jeffNo + ", " + jeffD + "\n")
#
#jess = hold[19].split(': ')
#jessC = jess[0]
#jessN = jess[1].split(' ')
#jessNo = jessN[0]
#file.write(jessC + ", " + jessNo + "\n")
#
#kent = hold[20].split(':')
#kenC = kent[0]
#kenN = kent[1].split(' ')
#kenNo = kenN[0].split('\xa0')[1]
#kenD = kenN[1]
#file.write(kenC + ", " + kenNo + ", " + kenD + "\n")
#
#larue = hold[21].split(': ')
#larC = larue[0]
#larN = larue[1].split(' ')
#larNo = larN[0]
#file.write(larC + ", " + larNo + "\n")
#
#laur = hold[22].split(': ')
#lauC = laur[0]
#lauN = laur[1].split(' ')
#lauNo = lauN[0]
#file.write(lauC + ", " + lauNo + "\n")
#
#lew = hold[23].split(': ')
#lewC = lew[0]
#lewN = lew[1].split(' ')
#lewNo = lewN[0]
#file.write(lewC + ", " + lewNo + "\n")
#
#logan = hold[24].split(':')
#logC = logan[0]
#logN = logan[1].split(' ')
#logNo = logN[0].split('\xa0')[1]
#file.write(logC + ", " + logNo + "\n")
#
#lyon = hold[25].split(':\xa0')
#lyC = lyon[0]
#lyN = lyon[1].split(' ')
#lyNo = lyN[0]
#file.write(lyC + ", " + lyNo + "\n")
#
#mad = hold[26].split(':')
#madC = mad[0]
#madN = mad[1].split(' ')
#madNo = madN[0].split('\xa0')[1]
#file.write(madC + ", " + madNo + "\n")
#
#mas = hold[27].split(':')
#masC = mas[0]
#masN = mas[1].split(' ')
#masNo = masN[0].split('\xa0')[1]
#file.write(masC + ", " + masNo + "\n")
#
#mcc = hold[28].split(':')
#mccC = mcc[0]
#mccN = mcc[1].split(' ')
#mccNo = mccN[0].split('\xa0')[1]
#file.write(mccC + ", " + mccNo + "\n")
#
#mcr = hold[29].split(':\xa0')
#mcrC = mcr[0]
#mcrN = mcr[1].split('\xa0')
#mcrNo = mcrN[0]
#file.write(mcrC + ", " + mcrNo + "\n")
#
#men = hold[30].split(':\xa0')
#menC = men[0]
#menN = men[1].split(' ')
#menNo = menN[0]
#file.write(menC + ", " + menNo + "\n")
#
#mer = hold[31].split(': ')
#merC = mer[0]
#merN = mer[1].split(' ')
#merNo = merN[0]
#file.write(merC + ", " + merNo + "\n")
#
#mont = hold[32].split(': ')
#moC = mont[0]
#moN = mont[1].split(' ')
#moNo = moN[0]
#file.write(moC + ", " + moNo + "\n")
#
#muh = hold[33].split(': ')
#muC = muh[0]
#muN = muh[1].split(' ')
#muNo = muN[0]
#file.write(muC + ", " + muNo + "\n")
#
#nel = hold[34].split(': ')
#nelC = nel[0]
#nelN = nel[1].split(' ')
#nelNo = nelN[0].split('\xa0')[0]
#file.write(nelC + ", " + nelNo + "\n")
#
#old = hold[35].split(':')
#oldC = old[0]
#oldN = old[1].split(' ')
#oldNo = oldN[0].split('\xa0')[1]
#file.write(oldC + ", " + oldNo + "\n")
#
#pul = hold[36].split(':')
#pulC = pul[0]
#pulN = pul[1].split(' ')
#pulNo = pulN[0].split('\xa0')[1]
#file.write(pulC + ", " + pulNo + "\n")
#
#scott = hold[37].split(': ')
#scoC = scott[0]
#scoN = scott[1].split(' ')
#scoNo = scoN[0].split('\xa0')[0]
#file.write(scoC + ", " + scoNo + "\n")
#
#simp = hold[38].split(': ')
#simC = simp[0]
#simN = simp[1].split(' ')
#simNo = simN[0].split('\xa0')[0]
#simD = simN[1]
#file.write(simC + ", " + simNo + ", " + simD +"\n")
#
#spe = hold[39].split(': ')
#speC = spe[0]
#speN = spe[1].split(' ')
#speNo = speN[0].split('\xa0')[0]
#file.write(speC + ", " + speNo + "\n")
#
#tay = hold[40].split(': ')
#tayC = tay[0]
#tayN = tay[1].split(' ')
#tayNo = tayN[0].split('\xa0')[0]
#file.write(tayC + ", " + tayNo + "\n")
#
#unio = hold[41].split(': ')
#unC = unio[0]
#unN = unio[1].split(' ')
#unNo = unN[0]
#file.write(unC + ", " + unNo + "\n")
#
#war = hold[42].split(':')
#warC = war[0]
#warN = war[1].split(' ')
#warNo = warN[0].split('\xa0')[1]
#file.write(warC + ", " + warNo + "\n")
#
#way = hold[43].split(': ')
#wayC = way[0]
#wayN = way[1].split(' ')
#wayNo = wayN[0].split('\xa0')[0]
#file.write(wayC + ", " + wayNo + "\n")
#
#web = hold[44].split(': ')
#webC = web[0]
#webN = web[1].split(' ')
#webNo = webN[0]
#file.write(webC + ", " + webNo + "\n")
#
#wood = hold[45].split(':')
#woC = wood[0]
#woN = wood[1].split(' ')
#woNo = woN[1].split('\xa0')[0]
#file.write(woC + ", " + woNo + "\n")
#
#other = hold[46].split(':')
#oC = other[0]
#oN = other[1].split(' ')
#oNo = oN[0].split('\xa0')[1]
#file.write(oC + ", " + oNo + "\n")

