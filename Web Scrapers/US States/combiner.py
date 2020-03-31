import bs4
import json
from urllib.request import Request
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from urllib import request
from urllib.request import urlretrieve
import requests

def akScrape():
    
    akdoh = 'http://dhss.alaska.gov/dph/Epi/id/Pages/COVID-19/monitoring.aspx'

    akClient = req(akdoh)

    site_parse = soup(akClient.read(), 'lxml')
    akClient.close()

    tables = site_parse.find("div", {"class": "grid3"})

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

    f.close()

def alScrape():
    
    aldoh = 'https://services7.arcgis.com/4RQmZZ0yaZkGR1zy/arcgis/rest/services/COV19_Public_Dashboard_ReadOnly/FeatureServer/0/query?where=1%3D1&outFields=CNTYNAME%2CCNTYFIPS%2CCONFIRMED%2CDIED&returnGeometry=false&f=pjson'
    
    alClient = req(aldoh).read().decode('utf-8')
    
    rJS = json.loads(alClient)
    
    attr = rJS.get('features')
    
    csvfile = "COVID-19_cases_aldoh.csv"
    headers = "County, Positive Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for a in attr:
        file.write(a.get('attributes').get('CNTYNAME') + ", " + str(a.get('attributes').get('CONFIRMED')) + ", " + str(a.get('attributes').get('DIED')) + "\n")
    
    file.close()
    
def arScrape():
    
    arWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Arkansas'
    
    arClient = req(arWiki)
    
    site_parse = soup(arClient.read(), "lxml")
    arClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_arWiki.csv"
    headers = "County, Confirmed Cases, Deaths, Recoveries \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[39:90]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + ", " + take[7] +"\n")
    
    file.close()    
    
def azScrape():
    
    azNews = 'https://www.abc15.com/news/state/coronavirus-in-arizona-tracking-latest-cases-covid-19-updates-in-our-state/'
    
    bypass = {'User-Agent': 'Mozilla/5.0'}
    
    azClient = Request(azNews, headers=bypass)
    azPage = urlopen(azClient)
    
    site_parse = soup(azPage.read(), 'lxml')
    azPage.close()
    
    tables = site_parse.find("div", {"class": "RichTextArticleBody-body"})
    
    death = tables.find_all('p')[4].get_text()[0:20].split(': ')[1]
    
    cases = tables.find_all('p')[6].get_text()
    
    csvfile = "COVID-19_cases_azNews.csv"
    headers = "County, Confirmed Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    pi = cases[59:68].split(': ')
    pimaC = pi[0]
    pimaN = pi[1]
    #print("County = %s, Confirmed Cases = %s" % (pimaC, pimaN))
    file.write(pimaC + ", " + pimaN + "\n")
    
    mari = cases[25:38].split(': ')
    mariC = mari[0]
    mariN = mari[1]
    #print("County = %s, Confirmed Cases = %s" % (mariC, mariN))
    file.write(mariC + ", " + mariN + "\n")
    
    pin = cases[38:47].split(': ')
    pinalC = pin[0]
    pinalN = pin[1]
    #print("County = %s, Confirmed Cases = %s" % (pinalC, pinalN))
    file.write(pinalC + ", " + pinalN + "\n")
    
    cochise = cases[99:109].split(': ')
    cochiseC = cochise[0]
    cochiseN = cochise[1]
    #print("County = %s, Confirmed Cases = %s" % (cochiseC, cochiseN))
    file.write(cochiseC + ", " + cochiseN + "\n")
    
    santaCruz = cases[118:131].split(': ')
    santaC = santaCruz[0]
    santaN = santaCruz[1]
    #print("County = %s, Confirmed Cases = %s" % (santaC, santaN))
    file.write(santaC + ", " + santaN + "\n")
    
    navajo = cases[68:78].split(': ')
    navajoC = navajo[0]
    navajoN = navajo[1]
    #print("County = %s, Confirmed Cases = %s" % (navajoC, navajoN))
    file.write(navajoC + ", " + navajoN + "\n")
    
    graham = cases[109:118].split(': ')
    grahamC = graham[0]
    grahamN = graham[1]
    #print("County = %s, Confirmed Cases = %s" % (grahamC, grahamN))
    file.write(grahamC + ", " + grahamN + "\n")
    
    coco = cases[47:59].split(': ')
    cocoC = coco[0]
    cocoN = coco[1]
    #print("County = %s, Confirmed Cases = %s" % (cocoC, cocoN))
    file.write(cocoC + ", " + cocoN + "\n")
    
    yuma = cases[131:138].split(': ')
    yumaC = yuma[0]
    yumaN = yuma[1]
    #print("County = %s, Confirmed Cases = %s" % (yumaC, yumaN))
    file.write(yumaC + ", " + yumaN + "\n")
    
    apache = cases[89:99].split(': ')
    apacheC = apache[0]
    apacheN = apache[1]
    #print("County = %s, Confirmed Cases = %s" % (apacheC, apacheN))
    file.write(apacheC + ", " + apacheN + "\n")
    
    yava = cases[78:89].split(': ')
    yavaC = yava[0]
    yavaN = yava[1]
    #print("County = %s, Confirmed Cases = %s" % (yavaC, yavaN))
    file.write(yavaC + ", " + yavaN + "\n")
    
    mohave = cases[138:147].split(': ')
    mohC = mohave[0]
    mohN = mohave[1]
    file.write(mohC + ", " + mohN + "\n")
    
    lapaz = cases[147:156].split(': ')
    lpC = lapaz[0]
    lpN = lapaz[1]
    file.write(lpC + ", " + lpN + "\n")
    
    gila = cases[156:163].split(': ')
    gilaC = gila[0]
    gilaN = gila[1]
    file.write(gilaC + ", " + gilaN + "\n")
    
    green = cases[163:174].split(': ')
    glC = green[0]
    glN = green[1]
    file.write(glC + ", " + glN + "\n")
    
    gilaR = cases[174:205].split(': ')
    gilC = gilaR[0]
    gilN = gilaR[1]
    file.write(gilaC + ", " + gilaN + "\n")
    
    navajoN = cases[205:223].split(': ')
    nnC = green[0]
    nnN = green[1]
    file.write(nnC + ", " + nnN + "\n")
    
    saltR = cases[239:].split(': ')
    saltC = saltR[0]
    saltN = saltR[1]
    file.write(saltC + ", " + saltN + "\n")
    
    file.write("Deaths in Arizona = %s" % death)
    
    file.close()
    
def caScrape():
    
    cadoh = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_California'
    
    caClient = req(cadoh)
    
    site_parse = soup(caClient.read(), 'lxml')
    caClient.close()
    
    tables = site_parse.find("div", {"class": "tp-container"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_caWiki.csv"
    headers = "County, Confirmed Cases, Deaths, Recoveries \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull[2:]:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[:47]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + ", " + take[7] + "\n")
                
    
    file.close()
    
def coScrape():

    codoh = 'https://covid19.colorado.gov/case-data'
    
    coClient = req(codoh)
    
    site_parse = soup(coClient.read(), 'lxml')
    coClient.close()
    
    tables = site_parse.findAll("div", {"class": "field field--name-field-card-body field--type-text-long field--label-hidden field--item"})[1]
    
    test = tables.findAll('tr')
    
    hold = []
    
    csvfile = "COVID-19_cases_coDOH.csv"
    headers = "County, Positive Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for t in test[1:50]:
            pull = t.findAll('td')
            #print("County = %s, Positive Cases = %s, Deaths = %s" % \
             #     (pull[0].text, pull[1].text, pull[2].text))
            file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()

def ctScrape():
    
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
    file.write(fairC + ", " + fairN.replace(',', '') + "\n")
    
    
    hart = hold[1].split(' County ')
    #print(hart)
    hartC = hart.pop(0)
    hartN = hart.pop()
    file.write(hartC + ", " + hartN.replace(',', '') + "\n")
    
    litch = hold[2].split(' County ')
    #print(litch)
    litC = litch.pop(0)
    litN = litch.pop()
    file.write(litC + ", " + litN.replace(',', '') + "\n")
    
    midd = hold[3].split(' County ')
    #print(midd)
    midC = midd.pop(0)
    midN = midd.pop()
    file.write(midC + ", " + midN.replace(',', '') + "\n")
    
    newHa = hold[4].split(' County ')
    #print(newHa)
    nhC = newHa.pop(0)
    nhN = newHa.pop()
    file.write(nhC + ", " + nhN.replace(',', '') + "\n")
    
    newLo = hold[5].split(' County ')
    #print(newLo)
    nlC = newLo.pop(0)
    nlN = newLo.pop()
    file.write(nlC + ", " + nlN.replace(',', '') + "\n")
    
    toll = hold[6].split(' County ')
    #print(toll)
    tollC = toll.pop(0)
    tollN = toll.pop()
    file.write(tollC + ", " + tollN.replace(',', '') + "\n")
    
    wind = hold[7].split(' County ')
    #print(wind)
    windC = wind.pop(0)
    windN = wind.pop()
    file.write(windC + ", " + windN.replace(',', '') + "\n")
    
    file.close()
    
def dcScrape():
    
    dcFile = "https://coronavirus.dc.gov/sites/default/files/dc/sites/coronavirus/page_content/attachments/COVID19_DCHealthStatisticsDataV2%20%283%29.xlsx"

    download = requests.get(dcFile)
    download.raise_for_status()
    
    newLife = open('DC-COVID-19.xlsx', 'wb')
    for chunk in download.iter_content(100000):
        newLife.write(chunk)
    
    newLife.close()
    
def deScrape():
    
    dedoh = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Delaware'

    deClient = req(dedoh)
    
    site_parse = soup(deClient.read(), 'lxml')
    deClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).findAll('tbody')[3]
    
    pull = tables.findAll('td')
    
    csvfile = "COVID-19_cases_deWiki.csv"
    headers = "County, Confirmed Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    kent = pull[0].get_text().split('\n')[0]
    kentC = pull[1].get_text().split('\n')[0]
    newCastle = pull[2].get_text().split('\n')[0]
    newC = pull[3].get_text().split('\n')[0]
    suss = pull[4].get_text().split('\n')[0]
    sussC = pull[5].get_text().split('\n')[0]
    
    
    file.write(kent + ", " + kentC + "\n")
    file.write(newCastle + ", " + newC + "\n")
    file.write(suss + ", " + sussC + "\n")
    
    file.close()
    
def flScrape():
    
    #Retrieved from Florida's opendata site https://open-fdoh.hub.arcgis.com/datasets/florida-covid19-cases

    flFile = "https://opendata.arcgis.com/datasets/a7887f1940b34bf5a02c6f7f27a5cb2c_0.csv?outSR=%7B%22latestWkid%22%3A3087%2C%22wkid%22%3A3087%7D"
    
    download = requests.get(flFile)
    download.raise_for_status()
    
    newLife = open('FLCOVID-19.csv', 'wb')
    for chunk in download.iter_content(100000):
        newLife.write(chunk)
    
    newLife.close()

def gaScrape():
    
    gadoh = 'https://d20s4vd27d0hk0.cloudfront.net/?initialWidth=616&childId=covid19dashdph&parentTitle=COVID-19%20Daily%20Status%20Report%20%7C%20Georgia%20Department%20of%20Public%20Health&parentUrl=https%3A%2F%2Fdph.georgia.gov%2Fcovid-19-daily-status-report'

    gaClient = req(gadoh)
    
    site_parse = soup(gaClient.read(), 'lxml')
    gaClient.close()
    
    tables = site_parse.find("div", {"id": "summary"}).findAll('tr')
    
    csvfile = "COVID-19_cases_gadoh.csv"
    headers = "County, Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for t in tables[5:119]:
            pull = t.findAll('td')
            print("County = %s, Cases = %s, Deaths = %s" % \
                  (pull[0].text, pull[1].text, pull[2].text))
            file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()
    
def hiScrape():
    
    hidoh = 'https://health.hawaii.gov/coronavirusdisease2019/what-you-should-know/current-situation-in-hawaii/'

    hiClient = req(hidoh)
    
    site_parse = soup(hiClient.read(), "lxml")
    hiClient.close()
    
    tables = site_parse.find("div", {"id": "inner-wrap"}).find('tbody')
    
    csvfile = "COVID-19_cases_hidoh.csv"
    headers = "County, HI Residents, Non-HI Residents, Total Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    tags = tables.findAll('tr')
    
    for t in tags[2:9]:
        pull = t.findAll('td')
        #print(pull[0].text, pull[1].text.split(' (')[0], pull[2].text.split(' (')[0], pull[3].text.split(' (')[0])
        file.write(pull[0].text+", "+pull[1].text.split(' (')[0]+", "+pull[2].text.split(' (')[0]+", "+pull[3].text.split(' (')[0]+"\n")
    
    
    file.close()


def idScrape():
    
    idDOH = 'https://coronavirus.idaho.gov/'

    idClient = req(idDOH)
    
    site_parse = soup(idClient.read(), "lxml")
    idClient.close()
    
    tables = site_parse.find("table", {"class": "tablepress tablepress-id-1 tablepress-responsive"})
    
    csvfile = "COVID-19_cases_idDOH.csv"
    headers = "County, Confirmed Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    holdCo = []
    holdCas = []
    holdDe = []
    
    counties = tables.findAll("td", {"class": "column-2"})
    for lo in counties:
        take = lo.get_text()
        holdCo.append(take)
    
    cases = tables.findAll("td", {"class": "column-3"})
    for la in cases:
        take = la.get_text()
        holdCas.append(take)
    
    deaths = tables.findAll("td", {"class": "column-4"})
    for le in deaths:
        take = le.get_text()
        holdDe.append(take)
    
    for c, a, d in zip(holdCo, holdCas, holdDe):
        file.write(c + ", " + a + ", " + d + "\n")
        
    file.close()

def ilScrape():
    
    ilWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Illinois'

    ilClient = req(ilWiki)

    site_parse = soup(ilClient.read(), "lxml")
    ilClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_ilWiki.csv"
    headers = "County, Active Cases, Deaths, Recoveries, Total Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull[2:]:
                take = p.get_text()
                hold.append(take)
                
    for h in hold[46:97]:
        take = h.split('\n')
        #print(take[1], take[3], take[5], take[7], take[9])
        file.write(take[1] + ", " + take[3] + ", " + take[5] + ", " + take[7] + ", " + take[9] + "\n")
    
    file.close()
    

def inScrape():
    
    inWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Indiana'

    inClient = req(inWiki)
    
    site_parse = soup(inClient.read(), "lxml")
    inClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_inWiki.csv"
    headers = "County, Confirmed Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[36:104]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")
    
    file.close()
    
def ioScrape():
    
    ioWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Iowa'

    ioClient = req(ioWiki)
    
    site_parse = soup(ioClient.read(), "lxml")
    ioClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_ioWiki.csv"
    headers = "County, Confirmed Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[39:76]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")
    
    file.close()
    

def kaScrape():
    
    kaWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Kansas'

    kaClient = req(kaWiki)
    
    site_parse = soup(kaClient.read(), "lxml")
    kaClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_kaWiki.csv"
    headers = "County, Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[42:82]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[4] + "\n")
    
    file.close()
    
def kyScrape():
    
    kyNews = 'https://www.courier-journal.com/story/news/2020/03/09/coronavirus-kentucky-how-many-cases-and-where-they-kentucky/5001636002/'

    kyClient = req(kyNews)
    
    site_parse = soup(kyClient.read(), "lxml")
    kyClient.close()
    
    tables = site_parse.find("div", {"class": "asset-double-wide double-wide p402_premium"})
    
    csvfile = "COVID-19_cases_kyNews.csv"
    headers = "County, Confirmed Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    tag = tables.find_all('p')[12:60]
    
    hold = []
    
    for t in tag:
        take = t.get_text()
        hold.append(take)
    
    allen = hold[0].split(': ')
    allC = allen[0]
    allN = allen[1].split(' ')
    allNo = allN[0]
    file.write(allC + ", " + allNo + "\n")
    
    ander = hold[1].split(': ')
    andC = ander[0]
    andN = ander[1].split(' ')
    andNo = andN[0]
    andD = andN[2]
    file.write(andC + ", " + andNo + ", " + andD + "\n")
    
    boone = hold[2].split(': ')
    booneC = boone[0]
    booneN = boone[1].split(' ')
    booneNo = booneN[0].split('\xa0')[0]
    file.write(booneC + ", " + booneNo + "\n")
    
    bour = hold[3].split(': ')
    bourC = bour[0]
    bourN = bour[1].split(' ')
    bourNo = bourN[0]
    bourD = bourN[2]
    file.write(bourC + ", " + bourNo + ", " + bourD + "\n")
    
    breat = hold[4].split(': ')
    breatC = breat[0]
    breatN = breat[1].split(' ')
    breatNo = breatN[0]
    file.write(breatC + ", " + breatNo + "\n")
    
    bull = hold[5].split(': ')
    bullC = bull[0]
    bullN = bull[1].split(' ')
    bullNo = bullN[0]
    file.write(bullC + ", " + bullNo + "\n")
    
    camp = hold[6].split(': ')
    campC = camp[0]
    campN = camp[1].split(' ')
    campNo = campN[0].split('\xa0')[0]
    file.write(campC + ", " + campNo + "\n")
    
    call = hold[7].split(':')
    callC = call[0]
    callN = call[1].split(' ')
    callNo = callN[0].split('\xa0')[1]
    file.write(callC + ", " + callNo + "\n")
    
    christos = hold[8].split(': ')
    chrC = christos[0]
    chrN = christos[1].split(' ')
    chrNo = chrN[0].split('\xa0')[0]
    file.write(chrC + ", " + chrNo + "\n")
    
    clark = hold[9].split(': ')
    clrC = clark[0]
    clrN = clark[1].split(' ')
    clrNo = clrN[0].split('\xa0')[0]
    file.write(clrC + ", " + clrNo + "\n")
    
    dav = hold[10].split(':')
    davC = dav[0]
    davN = dav[1].split(' ')
    davNo = davN[0].split('\xa0')[1]
    file.write(davC + ", " + davNo + "\n")
    
    fay = hold[11].split(':')
    fayC = fay[0]
    fayN = fay[1].split(' ')
    fayNo = fayN[0].split('\xa0')[1]
    fayD = fayN[1].split('\xa0')[0]
    file.write(fayC + ", " + fayNo + ", " + fayD + "\n")
    
    floyd = hold[12].split(': ')
    flyC = floyd[0]
    flyN = floyd[1].split(' ')
    flyNo = flyN[0]
    file.write(flyC + ", " + flyNo + "\n")
    
    frank = hold[13].split(': ')
    frkC = frank[0]
    frkN = frank[1].split(' ')
    frkNo = frkN[0].split('\xa0')[0]
    file.write(frkC + ", " + frkNo + "\n")
    
    gray = hold[14].split(': ')
    grayC = gray[0]
    grayN = gray[1].split(' ')
    grayNo = grayN[0]
    file.write(grayC + ", " + grayNo + "\n")
    
    hard = hold[15].split(':')
    hardC = hard[0]
    hardN = hard[1].split(' ')
    hardNo = hardN[0].split('\xa0')[1]
    file.write(hardC + ", " + hardNo + "\n")
    
    harr = hold[16].split(': ')
    harrC = harr[0]
    harrN = harr[1].split(' ')
    harrNo = harrN[0]
    file.write(harrC + ", " + harrNo + "\n")
    
    hend = hold[17].split(':')
    henC = hend[0]
    henN = hend[1].split(' ')
    henNo = henN[0].split('\xa0')[1]
    file.write(henC + ", " + henNo + "\n")
    
    hop = hold[18].split(': ')
    hopC = hop[0]
    hopN = hop[1].split(' ')
    hopNo = hopN[0].split('\xa0')[0]
    hopD = hopN[1]
    file.write(hopC + ", " + hopNo + ", " + hopD + "\n")
    
    jeff = hold[19].split(': ')
    jeffC = jeff[0]
    jeffN = jeff[1].split(' ')
    jeffNo = jeffN[0].split('\xa0')[0]
    jeffD = jeffN[1].split('\xa0')[0]
    file.write(jeffC + ", " + jeffNo + ", " + jeffD + "\n")
    
    jess = hold[20].split(': ')
    jessC = jess[0]
    jessN = jess[1].split(' ')
    jessNo = jessN[0]
    file.write(jessC + ", " + jessNo + "\n")
    
    kent = hold[21].split(':')
    kenC = kent[0]
    kenN = kent[1].split(' ')
    kenNo = kenN[0].split('\xa0')[1]
    kenD = kenN[1]
    file.write(kenC + ", " + kenNo + ", " + kenD + "\n")
    
    larue = hold[22].split(': ')
    larC = larue[0]
    larN = larue[1].split(' ')
    larNo = larN[0]
    file.write(larC + ", " + larNo + "\n")
    
    laur = hold[23].split(': ')
    lauC = laur[0]
    lauN = laur[1].split(' ')
    lauNo = lauN[0]
    file.write(lauC + ", " + lauNo + "\n")
    
    lew = hold[24].split(': ')
    lewC = lew[0]
    lewN = lew[1].split(' ')
    lewNo = lewN[0]
    file.write(lewC + ", " + lewNo + "\n")
    
    logan = hold[25].split(':')
    logC = logan[0]
    logN = logan[1].split(' ')
    logNo = logN[0].split('\xa0')[1]
    file.write(logC + ", " + logNo + "\n")
    
    lyon = hold[26].split(':\xa0')
    lyC = lyon[0]
    lyN = lyon[1].split(' ')
    lyNo = lyN[0]
    file.write(lyC + ", " + lyNo + "\n")
    
    mad = hold[27].split(':')
    madC = mad[0]
    madN = mad[1].split(' ')
    madNo = madN[0].split('\xa0')[1]
    file.write(madC + ", " + madNo + "\n")
    
    mas = hold[28].split(':')
    masC = mas[0]
    masN = mas[1].split(' ')
    masNo = masN[0].split('\xa0')[1]
    file.write(masC + ", " + masNo + "\n")
    
    mcc = hold[29].split(':')
    mccC = mcc[0]
    mccN = mcc[1].split(' ')
    mccNo = mccN[0].split('\xa0')[1]
    file.write(mccC + ", " + mccNo + "\n")
    
    mcr = hold[30].split(':\xa0')
    mcrC = mcr[0]
    mcrN = mcr[1].split('\xa0')
    mcrNo = mcrN[0]
    file.write(mcrC + ", " + mcrNo + "\n")
    
    men = hold[31].split(':\xa0')
    menC = men[0]
    menN = men[1].split(' ')
    menNo = menN[0]
    file.write(menC + ", " + menNo + "\n")
    
    mer = hold[32].split(': ')
    merC = mer[0]
    merN = mer[1].split(' ')
    merNo = merN[0]
    file.write(merC + ", " + merNo + "\n")
    
    mont = hold[33].split(': ')
    moC = mont[0]
    moN = mont[1].split(' ')
    moNo = moN[0]
    file.write(moC + ", " + moNo + "\n")
    
    muh = hold[34].split(': ')
    muC = muh[0]
    muN = muh[1].split(' ')
    muNo = muN[0]
    file.write(muC + ", " + muNo + "\n")
    
    nel = hold[35].split(': ')
    nelC = nel[0]
    nelN = nel[1].split(' ')
    nelNo = nelN[0].split('\xa0')[0]
    file.write(nelC + ", " + nelNo + "\n")
    
    old = hold[36].split(':')
    oldC = old[0]
    oldN = old[1].split(' ')
    oldNo = oldN[0].split('\xa0')[1]
    file.write(oldC + ", " + oldNo + "\n")
    
    pul = hold[37].split(':')
    pulC = pul[0]
    pulN = pul[1].split(' ')
    pulNo = pulN[0].split('\xa0')[1]
    file.write(pulC + ", " + pulNo + "\n")
    
    scott = hold[38].split(': ')
    scoC = scott[0]
    scoN = scott[1].split(' ')
    scoNo = scoN[0].split('\xa0')[0]
    file.write(scoC + ", " + scoNo + "\n")
    
    simp = hold[39].split(': ')
    simC = simp[0]
    simN = simp[1].split(' ')
    simNo = simN[0].split('\xa0')[0]
    file.write(simC + ", " + simNo + "\n")
    
    spe = hold[40].split(': ')
    speC = spe[0]
    speN = spe[1].split(' ')
    speNo = speN[0].split('\xa0')[0]
    file.write(speC + ", " + speNo + "\n")
    
    tay = hold[41].split(': ')
    tayC = tay[0]
    tayN = tay[1].split(' ')
    tayNo = tayN[0].split('\xa0')[0]
    file.write(tayC + ", " + tayNo + "\n")
    
    unio = hold[42].split(': ')
    unC = unio[0]
    unN = unio[1].split(' ')
    unNo = unN[0]
    file.write(unC + ", " + unNo + "\n")
    
    war = hold[43].split(':')
    warC = war[0]
    warN = war[1].split(' ')
    warNo = warN[0].split('\xa0')[1]
    file.write(warC + ", " + warNo + "\n")
    
    way = hold[44].split(': ')
    wayC = way[0]
    wayN = way[1].split(' ')
    wayNo = wayN[0].split('\xa0')[0]
    file.write(wayC + ", " + wayNo + "\n")
    
    web = hold[45].split(': ')
    webC = web[0]
    webN = web[1].split(' ')
    webNo = webN[0]
    file.write(webC + ", " + webNo + "\n")
    
    wood = hold[46].split(':')
    woC = wood[0]
    woN = wood[1].split(' ')
    woNo = woN[0].split('\xa0')[1]
    file.write(woC + ", " + woNo + "\n")
    
    other = hold[47].split(':')
    oC = other[0]
    oN = other[1].split(' ')
    oNo = oN[0].split('\xa0')[1]
    file.write(oC + ", " + oNo + "\n")
    
    file.close()
    
def laScrape():
    
    laWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Louisiana'

    laClient = req(laWiki)
    
    site_parse = soup(laClient.read(), "lxml")
    laClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_laWiki.csv"
    headers = "Parish, Confirmed Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[61:118]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3].replace(',','') + ", " + take[5].replace(',','') + "\n")
        #file.writerow(take[1], take[3], take[5])
    
    file.close()

def maScrape():
    
    maNews = 'https://www.livescience.com/massachusetts-coronavirus-updates.html'

    maClient = req(maNews)
    
    site_parse = soup(maClient.read(), "lxml")
    maClient.close()
    
    tables = site_parse.find("div", {"itemprop": "articleBody"}).find('ul')
    
    csvfile = "COVID-19_cases_maNews.csv"
    headers = "County, Confirmed Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    tags = tables.findAll('li')
    
    for t in range(0,15):
        #print("%s %s" % \
         #     (tags[t].get_text().split(': ')[0], tags[t].get_text().split(': ')[1]))
         file.write(tags[t].get_text().split(': ')[0] + ", " + tags[t].get_text().split(': ')[1].replace(',','') + "\n")
    
    file.close()

def mdScrape():
    
    mdWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Maryland'

    mdClient = req(mdWiki)
    
    site_parse = soup(mdClient.read(), "lxml")
    mdClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_mdWiki.csv"
    headers = "County, Confirmed Cases, Deaths, Recoveries \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
        
    for h in hold[67:90]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + ", " + take[7] + "\n")
    
    file.close()
    
def meScrape():
    
    meDDS = 'https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml'

    meClient = req(meDDS)
    
    site_parse = soup(meClient.read(), "lxml")
    meClient.close()
    
    tables = site_parse.find("div", {"id": "Accordion1"}).findAll("td")[5:90]
    
    #print(tables)
    
    csvfile = "COVID-19_cases_meDDS.csv"
    headers = "County, Confirmed Cases, Recovered, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
        take = t.get_text()
        hold.append(take)
    
    andr = hold[0:5]
    anC = andr[0]
    anCC = andr[1]
    anR = andr[2]
    anD = andr[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (anC, anCC, anR, anD))
    file.write(anC + ", " + anCC + ", " + anR + ", " + anD +"\n")
    
    aroo = hold[5:10]
    arC = aroo[0]
    arCC = aroo[1]
    arR = aroo[2]
    arD = aroo[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (arC, arCC, arR, arD))
    file.write(arC + ", " + arCC + ", " + arR + ", " + arD + "\n")
    
    
    cumb = hold[10:15]
    cumbC = cumb[0]
    cumbCC = cumb[1]
    cumbR = cumb[2]
    cumbD = cumb[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (cumbC, cumbCC, cumbR, cumbD))
    file.write(cumbC + ", " + cumbCC + ", " + cumbR + ", " + cumbD + "\n")
    
    
    frank = hold[15:20]
    frC = frank[0]
    frCC = frank[1]
    frR = frank[2]
    frD = frank[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (frC, frCC, frR, frD))
    file.write(frC + ", " + frCC + ", " + frR + ", " + frD + "\n")
    
    
    hanc = hold[20:25]
    haC = hanc[0]
    haCC = hanc[1]
    haR = hanc[2]
    haD = hanc[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (haC, haCC, haR, haD))
    file.write(haC + ", " + haCC + ", " + haR + ", " + haD + "\n")
    
    
    kenne = hold[25:30]
    keC = kenne[0]
    keCC = kenne[1]
    keR = kenne[2]
    keD = kenne[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (keC, keCC, keR, keD))
    file.write(keC + ", " + keCC + ", " + keR + ", " + keD + "\n")
    
    
    knox = hold[30:35]
    knC = knox[0]
    knCC = knox[1]
    knR = knox[2]
    knD = knox[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (knC, knCC, knR, knD))
    file.write(knC + ", " + knCC + ", " + knR + ", " + knD + "\n")
    
    
    linc = hold[35:40]
    linC = linc[0]
    linCC = linc[1]
    linR = linc[2]
    linD = linc[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (linC, linCC, linR, linD))
    file.write(linC + ", " + linCC + ", " + linR + ", " + linD + "\n")
    
    
    ox = hold[40:45]
    oxC = ox[0]
    oxCC = ox[1]
    oxR = ox[2]
    oxD = ox[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (oxC, oxCC, oxR, oxD))
    file.write(oxC + ", " + oxCC + ", " + oxR + ", " + oxD + "\n")
    
    
    peno = hold[45:50]
    penC = peno[0]
    penCC = peno[1]
    penR = peno[2]
    penD = peno[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (penC, penCC, penR, penD))
    file.write(penC + ", " + penCC + ", " + penR + ", " + penD + "\n")
    
    
    pisca = hold[50:55]
    piC = pisca[0]
    piCC = pisca[1]
    piR = pisca[2]
    piD = pisca[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (piC, piCC, piR, piD))
    file.write(piC + ", " + piCC + ", " + piR + ", " + piD + "\n")
    
    
    saga = hold[55:60]
    sC = saga[0]
    sCC = saga[1]
    sR = saga[2]
    sD = saga[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (sC, sCC, sR, sD))
    file.write(sC + ", " + sCC + ", " + sR + ", " + sD + "\n")
    
    
    somer = hold[60:65]
    soC = somer[0]
    soCC = somer[1]
    soR = somer[2]
    soD = somer[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (soC, soCC, soR, soD))
    file.write(soC + ", " + soCC + ", " + soR + ", " + soD + "\n")
    
    
    waldo = hold[65:70]
    wdC = waldo[0]
    wdCC = waldo[1]
    wdR = waldo[2]
    wdD = waldo[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (wdC, wdCC, wdR, wdD))
    file.write(wdC + ", " + wdCC + ", " + wdR + ", " + wdD + "\n")
    
    
    wash = hold[70:75]
    wsC = wash[0]
    wsCC = wash[1]
    wsR = wash[2]
    wsD = wash[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (wsC, wsCC, wsR, wsD))
    file.write(wsC + ", " + wsCC + ", " + wsR + ", " + wsD + "\n")
    
    
    york = hold[75:80]
    yC = york[0]
    yCC = york[1]
    yR = york[2]
    yD = york[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (yC, yCC, yR, yD))
    file.write(yC + ", " + yCC + ", " + yR + ", " + yD + "\n")
    
    
    unk = hold[80:85]
    uC = unk[0]
    uCC = unk[1]
    uR = unk[2]
    uD = unk[4]
    print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
          (uC, uCC, uR, uD))
    file.write(uC + ", " + uCC + ", " + uR + ", " + uD + "\n")
    
    file.close()

def miScrape():
    
    miDOH = 'https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html'

    miClient = req(miDOH)
    
    site_parse = soup(miClient.read(), "lxml")
    miClient.close()
    
    tables = site_parse.find("div", {"class": "fullContent"}).find("tbody")
    
    tags = tables.findAll('tr')
    
    csvfile = "COVID-19_cases_midoh.csv"
    headers = "County, Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for tag in tags[1:66]:
        pull = tag.findAll('td')
        print("County = %s, Cases = %s, Deaths = %s" % \
              (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()

def mnScrape():
    
    mnDOH = 'https://www.health.state.mn.us/diseases/coronavirus/situation.html'

    mnClient = req(mnDOH)
    
    site_parse = soup(mnClient.read(), "lxml")
    mnClient.close()
    
    tables = site_parse.find("div", {"class": "clearfix"}).find("tbody").findAll('td')
    
    csvfile = "COVID-19_cases_mndoh.csv"
    headers = "County, Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for td in tables:
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
    
    file.close()
    
def moScrape():
    
    moDOH = 'https://health.mo.gov/living/healthcondiseases/communicable/novel-coronavirus/results.php'

    moClient = req(moDOH)
    
    site_parse = soup(moClient.read(), "lxml")
    moClient.close()
    
    tables = site_parse.find("div", {"class": "panel-group"}).findAll('tr')
    
    csvfile = "COVID-19_cases_modoh.csv"
    headers = "County, Cases \n"
    sHeaders = "County, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for t in tables[1:119]:
        pull = t.findAll('td')
        #print("County = %s, Cases = %s" % \
              #(pull[0].text, pull[1].text))
        file.write(pull[0].text + ", " + pull[1].text + "\n")
    
    tablesDe = site_parse.find("div", {"id": "collapseDeaths"}).findAll('tr')
    
    file.write("\n")
    file.write(sHeaders)
    
    for ta in tablesDe[1:]:
        pullDe = ta.findAll('td')
        #print("County = %s, Deaths = %s" % (pullDe[0].text, pullDe[1].text))
        file.write(pullDe[0].text + ", " + pullDe[1].text + "\n")
    
    file.close()

def msScrape():
    
    msDOH = 'https://msdh.ms.gov/msdhsite/_static/14,0,420.html'

    msClient = req(msDOH)
    
    site_parse = soup(msClient.read(), "lxml")
    msClient.close()
    
    tables = site_parse.find("table", {"id": "msdhTotalCovid-19Cases"}).find("tbody").findAll('tr')
    
    csvfile = "COVID-19_cases_msdoh.csv"
    headers = "County, Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for t in tables:
        pull = t.findAll('td')
        print("County = %s, Cases = %s, Deaths = %s" % \
              (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()

def mtScrape():
    
    mtNews = 'https://www.livescience.com/montana-coronavirus-updates.html'

    mtClient = req(mtNews)
    
    site_parse = soup(mtClient.read(), "lxml")
    mtClient.close()
    
    tables = site_parse.find("div", {"id" : "article-body"}).find('ul')
    
    csvfile = "COVID-19_cases_mtNews.csv"
    headers = "County, Confirmed Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    tags = tables.findAll('li')
    
    for t in tags:
        pull = t.get_text().split(": ")
        file.write(pull[0] + ", " + pull[1] + "\n")
    
    file.close()

def ncScrape():
    
    orDOH = 'https://govstatus.egov.com/OR-OHA-COVID-19'

    orClient = req(orDOH)
    
    site_parse = soup(orClient.read(), "lxml")
    orClient.close()
    
    tables = site_parse.find("div", {"id": "collapseOne"}).find("tbody")
    
    tags = tables.findAll('tr')
    
    csvfile = "COVID-19_cases_ordoh.csv"
    headers = "County, Positive Cases, Deaths, Negative Test Results \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for tag in tags:
        pull = tag.findAll('td')
        print("County = %s, Cases = %s, Deaths = %s, Negative Test Results = %s" % \
              (pull[0].text, pull[1].text, pull[2].text, pull[3].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + ", " + pull[3].text + "\n")
    
    file.close()

def ndScrape():
    
    ndDOH = 'https://www.health.nd.gov/diseases-conditions/coronavirus/north-dakota-coronavirus-cases'

    ndClient = req(ndDOH)
    
    site_parse = soup(ndClient.read(), "lxml")
    ndClient.close()
    
    tables = site_parse.find("div", {"class":"paragraph paragraph--type--bp-accordion-section paragraph--view-mode--default paragraph--id--3613"}).find('tbody')
    
    csvfile = "COVID-19_cases_nddoh.csv"
    headers = "County, Total Tests, Positive Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    tags = tables.findAll('tr')
    
    for tag in tags[1:]:
        pull = tag.findAll('td')
        #print("County = %s, Total Tests = %s, Positive Cases = %s" % (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()

def neScrape():
    
    neWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Nebraska'

    neClient = req(neWiki)
    
    site_parse = soup(neClient.read(), "lxml")
    neClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_neWiki.csv"
    headers = "County, Confirmed Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[38:58]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")
    
    file.close()
    
def njScrape():
    
    njWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_New_Jersey'

    njClient = req(njWiki)
    
    site_parse = soup(njClient.read(), "lxml")
    njClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_njWiki.csv"
    headers = "County, Confirmed Cases, Deaths, Recoveries \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[43:65]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3].replace(',','') + ", " + take[5].replace(',','') + ", " + take[7].replace(',','') + "\n")
    
    file.close()
    
def nmScrape():
    
    nmDOH = 'https://cv.nmhealth.org/cases-by-county/'

    nmClient = req(nmDOH)
    
    site_parse = soup(nmClient.read(), "lxml")
    nmClient.close()
    
    tables = site_parse.find("div", {"class": "et_pb_section et_pb_section_2 et_pb_with_background et_section_regular"}).find("tbody")
    
    tags = tables.findAll('tr')
    
    csvfile = "COVID-19_cases_nmdoh.csv"
    headers = "County, Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for tag in tags[1:]:
        pull = tag.findAll('td')
        print("County = %s, Cases = %s, Deaths = %s" % \
              (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()
    

def nyScrape():
    nydoh = 'https://coronavirus.health.ny.gov/county-county-breakdown-positive-cases'

    bypass = {'User-Agent': 'Mozilla/5.0'}

    nClient = Request(nydoh, headers=bypass)
    nyPage = req(nClient)

    site_parse = soup(nyPage, 'lxml')
    nyPage.close()

    tables = site_parse.find("div", {"class": "wysiwyg--field-webny-wysiwyg-body"})

    tags = tables.findAll('tr')

    csvfile = "COVID-19_cases_nydoh.csv"
    headers = "County, Positive Cases \n"

    file = open(csvfile, "w", encoding = 'utf-8')
    file.write(headers)

    for tag in tags[1:57]:
        pull = tag.findAll('td')
        print("County = %s, Positive Cases = %s" % \
              (pull[0].text, pull[1].text))
    
        file.write(pull[0].text + ", " + pull[1].text.replace(',','') + "\n")

    file.close()
    
def ohScrape():
    
    ohWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Ohio'

    ohClient = req(ohWiki)
    
    site_parse = soup(ohClient.read(), "lxml")
    ohClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_ohWiki.csv"
    headers = "County, Confirmed Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[37:105]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")
    
    file.close()
    
def okScrape():
    
    okDOH = 'https://coronavirus.health.ok.gov/'

    okClient = req(okDOH)
    
    site_parse = soup(okClient.read(), "lxml")
    okClient.close()
    
    tables = site_parse.find("table", {"summary": "COVID-19 Cases by County"}).find("tbody")
    
    tags = tables.findAll('tr')
    
    csvfile = "COVID-19_cases_okdoh.csv"
    headers = "County, Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for tag in tags:
        pull = tag.findAll('td')
        print("County = %s, Cases = %s, Deaths = %s" % \
              (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
        
    file.close()
    
def orScrape():
    
    orDOH = 'https://govstatus.egov.com/OR-OHA-COVID-19'

    orClient = req(orDOH)
    
    site_parse = soup(orClient.read(), "lxml")
    orClient.close()
    
    tables = site_parse.find("div", {"id": "collapseOne"}).find("tbody")
    
    tags = tables.findAll('tr')
    
    csvfile = "COVID-19_cases_ordoh.csv"
    headers = "County, Positive Cases, Deaths, Negative Test Results \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for tag in tags:
        pull = tag.findAll('td')
        print("County = %s, Cases = %s, Deaths = %s, Negative Test Results = %s" % \
              (pull[0].text, pull[1].text, pull[2].text, pull[3].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + ", " + pull[3].text + "\n")
    
    file.close()

def paScrape():
    
    paDOH = 'https://www.health.pa.gov/topics/disease/coronavirus/Pages/Cases.aspx'

    paClient = req(paDOH)
    
    site_parse = soup(paClient.read(), "lxml")
    paClient.close()
    
    tables = site_parse.find("div", {"class": "ms-rtestate-field", "style": "display:inline"}).find("div", {"style": "text-align:center;"}).find("table", {"class": "ms-rteTable-default"})
    
    tags = tables.findAll('tr')
    
    csvfile = "COVID-19_cases_padoh.csv"
    headers = "County, Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for tag in tags[1:]:
        pull = tag.findAll('td')
        print("County = %s, Cases = %s, Deaths = %s" % \
              (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()

def prScrape():
    
    prWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Puerto_Rico'

    prClient = req(prWiki)
    
    site_parse = soup(prClient.read(), "lxml")
    prClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_prWiki.csv"
    headers = "Region, Confirmed Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[13:22]:
        take = h.split('\n')
        file.write(take[1] +  ", " + take[5] + "\n")
    
    file.close()

def scScrape():
    
    scWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_South_Carolina'

    scClient = req(scWiki)
    
    site_parse = soup(scClient.read(), "lxml")
    scClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_scWiki.csv"
    headers = "County, Confirmed Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[40:80]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")
    
    file.close()

def sdScrape():
    
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
    
def tnScrape():
    
    tndoh = 'https://www.tn.gov/health/cedep/ncov.html'

    tnClient = req(tndoh)
    
    site_parse = soup(tnClient.read(), 'lxml')
    tnClient.close()
    
    tables = site_parse.find("div", {"class": "containers tn-accordion parbase"}).find("div", {"class": "tn-simpletable parbase"})
    
    colTable = site_parse.find("div", {"class": "row parsys_column tn-3cols"}).findAll("div", {"class": "tn-simpletable parbase"})[2]
    
    fatal = colTable.find('tr')
    fa = fatal.get_text().split('\n')
    faStr = fa.pop(0)
    faNo = fa.pop(0)
    
    tags = tables.findAll('tr')
    
    csvfile = "COVID-19_cases_tndoh.csv"
    headers = "County, Positive Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for tag in tags[1:]:
        pull = tag.findAll('p')
        print("County = %s, Positive Cases = %s" % (pull[0].text, pull[1].text))
        
        file.write(pull[0].text + ", " + pull[1].text.replace(',','') + "\n")
    
    file.write("\n")
    file.write(faStr + ", " + faNo + "\n")
    
    file.close()

def txScrape():
    
    txNews = 'https://apps.texastribune.org/features/2020/tx-coronavirus-tracker/embeds/daily-tables/table-latest/index.html'

    bypass = {'User-Agent': 'Mozilla/5.0'}
    
    txClient = Request(txNews, headers=bypass)
    txPage = urlopen(txClient)
    
    site_parse = soup(txPage, 'lxml')
    txPage.close()
    
    tables = site_parse.find("table", {"class": "dv-table"}).find('tbody')
    
    csvfile = "COVID-19_cases_txNews.csv"
    headers = "County, No. of Cases, Deaths \n"
    
    file = open(csvfile, "w", encoding = 'utf-8')
    file.write(headers)
    
    tags = tables.findAll('tr')
    
    for tag in tags[:10]:
        pull = tag.findAll('td')
        #print("County = %s, No. of Cases = %s, Deaths = %s" % (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    for tag in tags[11:125]:
        pull = tag.findAll('td')
        #print("County = %s, No. of Cases = %s, Deaths = %s" % (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()

def utScrape():
    
    utNews = 'https://www.livescience.com/utah-coronavirus-updates.html'

    utClient = req(utNews)

    site_parse = soup(utClient.read(), 'lxml')
    utClient.close()
    
    tables = site_parse.find("article", {"class": "news-article", "data-id": "Kk2kmK3UhF5L6dgXZf8wHe"}).find("div", {"itemprop": "articleBody"}).findAll('ul')[1]
    
    csvfile = "COVID-19_cases_utNews.csv"
    headers = "County, Confirmed Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    tags = tables.findAll('li')
    
    for t in range(0,13):
        #print("%s %s" % \
         #     (tags[t].get_text().split(': ')[0], tags[t].get_text().split(': ')[1]))
         file.write(tags[t].get_text().split('- ')[0] + ", " + tags[t].get_text().split('- ')[1] + "\n")
    
    file.close()
    
def vaScrape():
    
    vaWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Virginia'

    vaClient = req(vaWiki)
    
    site_parse = soup(vaClient.read(), "lxml")
    vaClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_vaWiki.csv"
    headers = "County, Confirmed Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[41:128]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3].split('[')[0] + ", " + take[5].split('[')[0] + "\n")
    
    file.close()
    
def viScrape():
    
    viDOH = 'https://doh.vi.gov/covid19usvi'

    viClient = req(viDOH)
    
    site_parse = soup(viClient.read(), "lxml")
    viClient.close()
    
    tables = site_parse.find("div", {"class": "page-content-sidebar col-sm-12 col-md-4"}).find("div", {"class": "block-content clearfix"})
    
    csvfile = "COVID-19_cases_vidoh.csv"
    headers = "Case Types, No. of Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    tags = tables.findAll('p')
    
    pos = tags[0].text.split(':\xa0')[0]
    posNo = tags[0].text.split(':\xa0')[1]
    
    recov = tags[1].text.split(':\xa0')[0]
    recNo = tags[1].text.split(':\xa0')[1]
    
    neg = tags[2].text.split(':\xa0')[0]
    negNo = tags[2].text.split(':\xa0')[1]
    
    pend = tags[3].text.split(':\xa0')[0]
    pendNo = tags[3].text.split(':\xa0')[1]
    
    file.write(pos + ", " + posNo + "\n")
    file.write(recov + ", " + recNo + "\n")
    file.write(neg + ", " + negNo + "\n")
    file.write(pend + ", " + pendNo + "\n")
    
    file.close()

def vtScrape():
    
    vtWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Vermont'

    vtClient = req(vtWiki)
    
    site_parse = soup(vtClient.read(), "lxml")
    vtClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_vtWiki.csv"
    headers = "County, Confirmed Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[39:52]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + "\n")
    
    file.close()
    
def waScrape():
    
    waWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Washington_(state)'

    waClient = req(waWiki)
    
    site_parse = soup(waClient.read(), "lxml")
    waClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_waWiki.csv"
    headers = "County, Confirmed Cases, Deaths, Recoveries \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[49:84]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3].split('[')[0].replace(',','') + ", " + take[5].split('[')[0].replace(',','') + ", " + take[7].split('[')[0].replace(',','') + "\n")
    
    file.close()
    
def wiScrape():
    
    widoh = 'https://services1.arcgis.com/ISZ89Z51ft1G16OK/arcgis/rest/services/COVID19_WI/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=NAME%2CPOSITIVE%2CDEATHS%2CDATE&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=NAME+ASC&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token='

    wiClient = req(widoh).read().decode('utf-8')
    
    wiJS = json.loads(wiClient)
    
    attr = wiJS.get('features')
    
    csvfile = "COVID-19_cases_widoh.csv"
    headers = "County, Positive Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for a in attr:
        file.write(a.get('attributes').get('NAME') + ", " + str(a.get('attributes').get('POSITIVE')) + ", " + str(a.get('attributes').get('DEATHS')) + "\n")
    
    file.close()
    
def wvScrape():
    
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
    
    file.close()

def wyScrape():
    
    wyWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Wyoming'

    wyClient = req(wyWiki)
    
    site_parse = soup(wyClient.read(), "lxml")
    wyClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_wyWiki.csv"
    headers = "County, Confirmed Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[33:56]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")
    
    file.close()
        
    

def main():
    
    akScrape()
    alScrape()
    arScrape()
    azScrape()
    caScrape()
    coScrape()
    ctScrape()
    dcScrape()
    deScrape()
    flScrape()
    gaScrape()
    hiScrape()
    idScrape()
    ilScrape()
    inScrape()
    ioScrape()
    kaScrape()
    kyScrape()
    laScrape()
    maScrape()
    mdScrape()
    meScrape()
    miScrape()
    mnScrape()
    moScrape()
    msScrape()
    mtScrape()
    ncScrape()
    ndScrape()
    neScrape()
    njScrape()
    nmScrape()
    nyScrape()
    ohScrape()
    okScrape()
    orScrape()
    paScrape()
    prScrape()
    scScrape()
    sdScrape()
    tnScrape()
    txScrape()
    utScrape()
    vaScrape()
    viScrape()
    vtScrape()
    waScrape()
    wiScrape()
    wvScrape()
    wyScrape()
    
if __name__ == "__main__":
    main()
