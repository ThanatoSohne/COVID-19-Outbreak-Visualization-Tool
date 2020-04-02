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
        anR1 = ''.join(anR[1:3])
        anT = anch[6]
        f.write(anR1 + ", " + anT + "\n")
        
        gulf = tags[5].text.split('\n')
        gulfR = gulf[1].split('\xa0')
        gulfR1 = gulfR[1]
        gulfT = gulf[6]
        f.write(gulfR1 + ", " + gulfT +"\n")
        
        intr = tags[11].text.split('\n')
        intrR = intr[1].split('\xa0')
        intrR1 = intrR[1]
        intrT = intr[6]
        f.write(intrR1 + ", " + intrT + "\n")
        
        matsu = tags[14].text.split('\n')
        matsuR = matsu[1].split('\xa0')
        matsuR1 = matsuR[1]
        matsuT = matsu[6]
        f.write(matsuR1 + ", " + matsuT + "\n")
        
        nort = tags[17].text.split('\n')
        nortR = nort[1].split('\xa0')
        nortR1 = nortR[1]
        nortT = nort[6]
        f.write(nortR1 + ", " + nortT + "\n")
        
        se = tags[18].text.split('\n')
        seR = se[1].split('\xa0')
        seR1 = seR[1]
        seT = se[6]
        f.write(seR1 + ", " + seT + "\n")
        
        sw = tags[21].text.split('\n')
        swR = sw[1].split('\xa0')
        swR1 = swR[1]
        swT = sw[6]
        f.write(swR1 + ", " + swT + "\n")

    f.close()
    
    if (anR1 == 'Municipality of Anchorage' and swR1 == 'Southwest'):
        print("Alaska scraper complete.")
    else:
        print("ERROR: Must fix Alaska scraper.")

def alScrape():
    
    aldoh = 'https://services7.arcgis.com/4RQmZZ0yaZkGR1zy/arcgis/rest/services/COV19_Public_Dashboard_ReadOnly/FeatureServer/0/query?where=1%3D1&outFields=CNTYNAME%2CCNTYFIPS%2CCONFIRMED%2CDIED&returnGeometry=false&f=pjson'
    
    alClient = req(aldoh).read().decode('utf-8')
    
    rJS = json.loads(alClient)
    
    attr = rJS.get('features')
    
    test = []
    
    csvfile = "COVID-19_cases_aldoh.csv"
    headers = "County, Positive Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for a in attr:
        file.write(a.get('attributes').get('CNTYNAME') + ", " + str(a.get('attributes').get('CONFIRMED')) + ", " + str(a.get('attributes').get('DIED')) + "\n")
        
        if(attr[0].get('attributes').get('CNTYNAME')) == 'Autauga':
            test = True
        else:
            test = False
    file.close()
    
    if test == True:
        print("Alabama scraper is complete.")
    else:
        print("ERROR: Must fix Alabama scraper.")
    
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
    
    for h in hold[42:97]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + ", " + take[7] +"\n")
    
    file.close()    
    
    if (hold[42].split('\n')[1]) == 'Arkansas' and (hold[96].split('\n')[1]) == 'Woodruff':
        print("Arkansas scraper is complete.")
    else:
        print("ERROR: Must fix Arkansas scraper.")
    
def azScrape():
    
    azWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Arizona'

    azClient = req(azWiki)
    
    site_parse = soup(azClient.read(), "lxml")
    azClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_azWiki.csv"
    headers = "County, Confirmed Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    for h in hold[39:54]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")
    
    file.close()
    
    if (hold[39].split('\n')[1]) == 'Maricopa' and (hold[53].split('\n')[1]) == 'Greenlee':
        print("Arizona scraper is complete.")
    else:
        print("ERROR: Must fix Arizona scraper.")
    
    
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
    
    for h in hold[:50]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + ", " + take[7] + "\n")
                
    
    file.close()
    
    if (hold[0].split('\n')[1]) == 'Los Angeles' and (hold[49].split('\n')[1]) == 'Tuolumne':
        print("California scraper is complete.")
    else:
        print("ERROR: Must fix California scraper.")
    
def coScrape():

    codoh = 'https://covid19.colorado.gov/case-data'
    
    coClient = req(codoh)
    
    site_parse = soup(coClient.read(), 'lxml')
    coClient.close()
    
    tables = site_parse.findAll("div", {"class": "field field--name-field-card-body field--type-text-long field--label-hidden field--item"})[1]
    
    test = tables.findAll('tr')
    
    adamsTest = test[1].find('td').text
    outTest = test[52].find('td').text
    
    csvfile = "COVID-19_cases_coDOH.csv"
    headers = "County, Positive Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for t in test[1:53]:
            pull = t.findAll('td')
            #print("County = %s, Positive Cases = %s, Deaths = %s" % \
             #     (pull[0].text, pull[1].text, pull[2].text))
            file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()
    
    if adamsTest == 'Adams' and outTest == 'Out of state':
        print("Colorado scraper is complete.")
    else:
        print("ERROR: Must fix Colorado scraper.")


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
    fairC = fair[0]
    fairN = fair[1]
    file.write(fairC + ", " + fairN.replace(',', '') + "\n")
    
    
    hart = hold[1].split(' County ')
    #print(hart)
    hartC = hart[0]
    hartN = hart[1]
    file.write(hartC + ", " + hartN.replace(',', '') + "\n")
    
    litch = hold[2].split(' County ')
    #print(litch)
    litC = litch[0]
    litN = litch[1]
    file.write(litC + ", " + litN.replace(',', '') + "\n")
    
    midd = hold[3].split(' County ')
    #print(midd)
    midC = midd[0]
    midN = midd[1]
    file.write(midC + ", " + midN.replace(',', '') + "\n")
    
    newHa = hold[4].split(' County ')
    #print(newHa)
    nhC = newHa[0]
    nhN = newHa[1]
    file.write(nhC + ", " + nhN.replace(',', '') + "\n")
    
    newLo = hold[5].split(' County ')
    #print(newLo)
    nlC = newLo[0]
    nlN = newLo[1]
    file.write(nlC + ", " + nlN.replace(',', '') + "\n")
    
    toll = hold[6].split(' County ')
    #print(toll)
    tollC = toll[0]
    tollN = toll[1]
    file.write(tollC + ", " + tollN.replace(',', '') + "\n")
    
    wind = hold[7].split(' County ')
    #print(wind)
    windC = wind[0]
    windN = wind[1]
    file.write(windC + ", " + windN.replace(',', '') + "\n")
    
    file.close()
    
    if fairC == 'Fairfield' and windC == 'Windham':
        print("Connecticut scraper is complete.")
    else:
        print("ERROR: Must fix Connecticut scraper.")
        

    
def dcScrape():
    
    dcFile = "https://coronavirus.dc.gov/sites/default/files/dc/sites/coronavirus/page_content/attachments/COVID19_DCHealthStatisticsDataV2%20%283%29.xlsx"

    download = requests.get(dcFile)
    download.raise_for_status()
    
    newLife = open('COVID-19-DC.xlsx', 'wb')
    for chunk in download.iter_content(100000):
        newLife.write(chunk)
    
    newLife.close()
    
    print("DC pull is complete.")
    
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
    
    if kent == 'Kent' and suss == 'Sussex':
        print("Delaware scraper is complete.")
    else:
        print("ERROR: Must fix Delaware scraper.")
    
def flScrape():
    
    #Retrieved from Florida's opendata site https://open-fdoh.hub.arcgis.com/datasets/florida-covid19-cases

    flFile = "https://opendata.arcgis.com/datasets/a7887f1940b34bf5a02c6f7f27a5cb2c_0.csv?outSR=%7B%22latestWkid%22%3A3087%2C%22wkid%22%3A3087%7D"
    
    download = requests.get(flFile)
    download.raise_for_status()
    
    newLife = open('COVID-19-FL.csv', 'wb')
    for chunk in download.iter_content(100000):
        newLife.write(chunk)
    
    newLife.close()
    
    print("Florida pull complete.")

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
    
    for t in tables[5:148]:
            pull = t.findAll('td')
            #print("County = %s, Cases = %s, Deaths = %s" % \
            #      (pull[0].text, pull[1].text, pull[2].text))
            file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()
    
    if (tables[5].find('td').text) == 'Fulton' and (tables[147].find('td').text) == 'Unknown':
        print("Georgia scraper is complete.")
    else:
        print("ERROR: Must fix Georgia scraper.")
    
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
    
    if (tags[2].find('td').text) == 'Hawaii' and (tags[8].find('td').text) == 'Total (new)':
        print("Hawai'i scraper is complete.")
    else:
        print("ERROR: Must fix Hawai'i scraper.")


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
    
    if holdCo[0] == 'Bonner' and holdCo[29] == 'TOTAL':
        print("Idaho scraper is complete.")
    else:
        print("ERROR: Must fix Idaho scraper.")


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
                
    for h in hold[49:105]:
        take = h.split('\n')
        #print(take[1], take[3], take[5], take[7], take[9])
        file.write(take[1] + ", " + take[3] + ", " + take[5] + ", " + take[7] + ", " + take[9] + "\n")
    
    file.close()
    
    if (hold[49].split('\n')[1]) == 'Adams' and (hold[104].split('\n')[1]) == 'Woodford':
        print("Illinois scraper is complete.")
    else:
        print("ERROR: Must fix Illinois scraper.")
    

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
    
    for h in hold[40:122]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")
    
    file.close()
    
    if (hold[40].split('\n')[1]) == 'Adams' and (hold[121].split('\n')[1]) == 'Whitley':
        print("Indiana scraper is complete.")
    else:
        print("ERROR: Must fix Indiana scraper.")
    
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
    
    for h in hold[42:99]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")
    
    file.close()
    
    if (hold[42].split('\n')[1]) == 'Adair' and (hold[98].split('\n')[1]) == 'Wright':
        print("Iowa scraper is complete.")
    else:
        print("ERROR: Must fix Iowa Scraper.")

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
    
    for h in hold[45:88]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[4] + "\n")
    
    file.close()
    
    if (hold[45].split('\n')[1]) == 'Atchison' and (hold[87].split('\n')[1]) == 'Wyandotte':
        print("Kansas scraper is complete.")
    else:
        print("ERROR: Must fix Kansas scraper.")

    
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
    
    tag = tables.find_all('p')[12:84]

    hold = []
    
    for t in tag:
        take = t.get_text()
        hold.append(take)
        
    for h in hold:
        file.write(h.split(':')[0] + ", " + h.split(':')[1].split('c')[0] + "\n")
        
    file.close()
    
    if (hold[0].split(':')[0]) == 'Adair County' and (hold[71].split(':')[0]) == 'No County Available':
        print("Kentucky scraper is complete.")
    else:
        print("ERROR: Must fix Kentucky scraper.")

    
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
    
    for h in hold[64:121]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3].replace(',','') + ", " + take[5].replace(',','') + "\n")
        #file.writerow(take[1], take[3], take[5])
    
    file.close()
    
    if (hold[64].split('\n')[1]) == 'Acadia' and (hold[120].split('\n')[1]) == 'Under Investigation':
        print("Louisiana scraper is complete.")
    else:
        print("ERROR: Must fix Louisiana scraper.")

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
    
    if (tags[0].get_text().split(': ')[0]) == 'Barnstable' and (tags[14].get_text().split(': ')[0]) == 'Unknown':
        print("Massachusetts scraper is complete.")
    else:
        print("ERROR: Must fix Massachusetts scraper.")

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
        
    for h in hold[70:94]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + ", " + take[7] + "\n")
    
    file.close()
    
    if (hold[70].split('\n')[1]) == 'Anne Arundel' and (hold[93].split('\n')[1]) == 'Unassigned':
        print("Maryland scraper is complete.")
    else:
        print("ERROR: Must fix Maryland scraper.")
    
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
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
    #      (anC, anCC, anR, anD))
    file.write(anC + ", " + anCC + ", " + anR + ", " + anD +"\n")
    
    aroo = hold[5:10]
    arC = aroo[0]
    arCC = aroo[1]
    arR = aroo[2]
    arD = aroo[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
    #     (arC, arCC, arR, arD))
    file.write(arC + ", " + arCC + ", " + arR + ", " + arD + "\n")
    
    
    cumb = hold[10:15]
    cumbC = cumb[0]
    cumbCC = cumb[1]
    cumbR = cumb[2]
    cumbD = cumb[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (cumbC, cumbCC, cumbR, cumbD))
    file.write(cumbC + ", " + cumbCC + ", " + cumbR + ", " + cumbD + "\n")
    
    
    frank = hold[15:20]
    frC = frank[0]
    frCC = frank[1]
    frR = frank[2]
    frD = frank[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (frC, frCC, frR, frD))
    file.write(frC + ", " + frCC + ", " + frR + ", " + frD + "\n")
    
    
    hanc = hold[20:25]
    haC = hanc[0]
    haCC = hanc[1]
    haR = hanc[2]
    haD = hanc[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (haC, haCC, haR, haD))
    file.write(haC + ", " + haCC + ", " + haR + ", " + haD + "\n")
    
    
    kenne = hold[25:30]
    keC = kenne[0]
    keCC = kenne[1]
    keR = kenne[2]
    keD = kenne[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (keC, keCC, keR, keD))
    file.write(keC + ", " + keCC + ", " + keR + ", " + keD + "\n")
    
    
    knox = hold[30:35]
    knC = knox[0]
    knCC = knox[1]
    knR = knox[2]
    knD = knox[4]
   # print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
    #      (knC, knCC, knR, knD))
    file.write(knC + ", " + knCC + ", " + knR + ", " + knD + "\n")
    
    
    linc = hold[35:40]
    linC = linc[0]
    linCC = linc[1]
    linR = linc[2]
    linD = linc[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (linC, linCC, linR, linD))
    file.write(linC + ", " + linCC + ", " + linR + ", " + linD + "\n")
    
    
    ox = hold[40:45]
    oxC = ox[0]
    oxCC = ox[1]
    oxR = ox[2]
    oxD = ox[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (oxC, oxCC, oxR, oxD))
    file.write(oxC + ", " + oxCC + ", " + oxR + ", " + oxD + "\n")
    
    
    peno = hold[45:50]
    penC = peno[0]
    penCC = peno[1]
    penR = peno[2]
    penD = peno[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (penC, penCC, penR, penD))
    file.write(penC + ", " + penCC + ", " + penR + ", " + penD + "\n")
    
    
    pisca = hold[50:55]
    piC = pisca[0]
    piCC = pisca[1]
    piR = pisca[2]
    piD = pisca[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (piC, piCC, piR, piD))
    file.write(piC + ", " + piCC + ", " + piR + ", " + piD + "\n")
    
    
    saga = hold[55:60]
    sC = saga[0]
    sCC = saga[1]
    sR = saga[2]
    sD = saga[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (sC, sCC, sR, sD))
    file.write(sC + ", " + sCC + ", " + sR + ", " + sD + "\n")
    
    
    somer = hold[60:65]
    soC = somer[0]
    soCC = somer[1]
    soR = somer[2]
    soD = somer[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (soC, soCC, soR, soD))
    file.write(soC + ", " + soCC + ", " + soR + ", " + soD + "\n")
    
    
    waldo = hold[65:70]
    wdC = waldo[0]
    wdCC = waldo[1]
    wdR = waldo[2]
    wdD = waldo[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (wdC, wdCC, wdR, wdD))
    file.write(wdC + ", " + wdCC + ", " + wdR + ", " + wdD + "\n")
    
    
    wash = hold[70:75]
    wsC = wash[0]
    wsCC = wash[1]
    wsR = wash[2]
    wsD = wash[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (wsC, wsCC, wsR, wsD))
    file.write(wsC + ", " + wsCC + ", " + wsR + ", " + wsD + "\n")
    
    
    york = hold[75:80]
    yC = york[0]
    yCC = york[1]
    yR = york[2]
    yD = york[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (yC, yCC, yR, yD))
    file.write(yC + ", " + yCC + ", " + yR + ", " + yD + "\n")
    
    
    unk = hold[80:85]
    uC = unk[0]
    uCC = unk[1]
    uR = unk[2]
    uD = unk[4]
    #print("County = %s, Confirmed Cases = %s, Recovered = %s, Deaths = %s" % \
     #     (uC, uCC, uR, uD))
    file.write(uC + ", " + uCC + ", " + uR + ", " + uD + "\n")
    
    file.close()
    
    if anC == 'Androscoggin' and uC == 'Unknown':
        print("Maine scraper is complete.")
    else:
        print("ERROR: Must fix Maine scraper.")

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
        #print("County = %s, Cases = %s, Deaths = %s" % \
         #     (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()
    
    if (tags[1].find('td').text.strip()) == 'Allegan' and (tags[70].find('td').text.strip()) == 'Out of State':
        print("Michigan scraper is complete.")
    else:
        print("ERROR: Must fix Michigan scraper.")

def mnScrape():
    
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
    
    file.close()
    
    if hold[0] == 'Anoka' and hold[108] == 'Yellow Medicine':
        print("Minnesota scraper is complete.")
    else:
        print("ERROR: Must fix Minnesota scraper.")

    
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

    if (tables[1].find('td').text) == 'Adair' and (tables[118].find('td').text) == 'TBD':
        print("Missouri scraper is complete.")
    else:
        print("ERROR: Must fix Missour scraper.")
    

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
    
    for t in tables[0:31]:
        pull = t.findAll('td')
        #print("County = %s, Cases = %s, Deaths = %s" % \
         #     (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")

    file.write(tables[32].findAll('td')[0].text + ", " + tables[32].findAll('td')[1].text + ", " + tables[32].findAll('td')[2].text + "\n")
    
    for t in tables[34:79]:
        pull = t.findAll('td')
        #print("County = %s, Cases = %s, Deaths = %s" % \
         #     (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()
    
    if (tables[0].find('td').text) == 'Adams' and (tables[78].find('td').text) == 'Yazoo':
        print("Mississippi scraper is complete.")
    else:
        print("ERROR: Must fix Mississippi scraper.")

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
    
    if (tags[0].get_text().split(": ")[0]) == 'Gallatin' and (tags[20].get_text().split(": ")[0]) == 'Hill':
        print("Montana scraper is complete.")
    else:
        print("ERROR: Must fix Montana scraper.")

def ncScrape():
    
    ncDOH = 'https://www.ncdhhs.gov/covid-19-case-count-nc#nc-counties-with-cases'

    ncClient = req(ncDOH)
    
    site_parse = soup(ncClient.read(), 'lxml')
    ncClient.close()
    
    tables = site_parse.find("div", {"class": "content band-content landing-wrapper"}).find('tbody')
    
    csvfile = "COVID-19_cases_ncdoh.csv"
    headers = "County, Cases, Deaths \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    tags = tables.findAll('tr')
    
    for tag in tags:
        pull = tag.findAll('td')
        #print("County = %s, Cases = %s, Deaths = %s" % (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()
    
    if (tags[0].find('td').text) == 'Alamance County' and (tags[77].find('td').text) == 'Yadkin County':
        print("North Carolina scraper is complete.")
    else:
        print("ERROR: Must fix North Carolina scraper.")

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
    
    for tag in tags:
        pull = tag.findAll('td')
        #print("County = %s, Total Tests = %s, Positive Cases = %s" % (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()
    
    if (tags[0].find('td').text) == 'Adams' and (tags[50].find('td').text) == 'Williams':
        print("North Dakota scraper is complete.")
    else:
        print("ERROR: Must fix North Dakota Scraper.")
        

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
    
    for h in hold[42:66]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")
    
    file.close()
    
    if (hold[42].split('\n')[1]) == 'Adams' and (hold[65].split('\n')[1]) == 'TBD':
        print("Nebraska scraper is complete.")
    else:
        print("ERROR: Must fix Nebraska scraper.")
        
def nhScrape():
    
    nhNews = 'https://www.livescience.com/new-hampshire-coronavirus-updates.html'

    nhClient = req(nhNews)
    
    site_parse = soup(nhClient.read(), "lxml")
    nhClient.close()
    
    tables = site_parse.find("article", {"class":"news-article"}).find("div", {"itemprop": "articleBody"}).find('ul')
    
    csvfile = "COVID-19_cases_nhNews.csv"
    headers = "County, Confirmed Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    tags = tables.findAll('li')
    
    for t in range(0,9):
        #print("%s %s" % \
        #      (tags[t].get_text().split(': ')[0], tags[t].get_text().split(': ')[1]))
        file.write(tags[t].get_text().split(': ')[0] + ", " + tags[t].get_text().split(': ')[1] + "\n")

    file.close()
         
    if (tags[0].get_text().split(': ')[0]) == 'Rockingham' and (tags[8].get_text().split(': ')[0]) == 'Sullivan':
        print("New Hampshire scraper is complete.")
    else:
        print("ERROR: Must fix New Hampshire scraper.")
    
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
    
    for h in hold[46:68]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3].replace(',','') + ", " + take[5].replace(',','') + ", " + take[7].replace(',','') + "\n")
    
    file.close()
    
    if (hold[46].split('\n')[1]) == 'Atlantic' and (hold[67].split('\n')[1]) == 'Under investigation':
        print("New Jersey scraper is complete.")
    else:
        print("ERROR: Must fix New Jersey scraper.")
    
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
        #print("County = %s, Cases = %s, Deaths = %s" % \
         #     (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()
    
    if (tags[1].find('td').text) == 'Bernalillo County' and (tags[33].find('td').text) == 'Valencia County':
        print("New Mexico scraper is complete.")
    else:
        print("ERROR: Must fix New Mexico scraper.")
    

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

    for tag in tags[1:58]:
        pull = tag.findAll('td')
        #print("County = %s, Positive Cases = %s" % \
         #     (pull[0].text, pull[1].text))
    
        file.write(pull[0].text + ", " + pull[1].text.replace(',','') + "\n")

    file.close()
    
    if (tags[1].find('td').text) == 'Albany' and (tags[57].find('td').text) == 'Wyoming':
        print("New York scraper is complete.")
    else:
        print("ERROR: Must fix New York scraper.")
    
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
    
    for h in hold[40:112]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")
    
    file.close()
    
    if (hold[40].split('\n')[1]) == 'Allen' and (hold[111].split('\n')[1]) == 'Wyandot':
        print("Ohio scraper is complete.")
    else:
        print("ERROR: Must fix Ohio scraper.")

    
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
        #print("County = %s, Cases = %s, Deaths = %s" % \
         #     (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
        
    file.close()
    
    if (tags[0].find('td').text) == 'Adair' and (tags[48].find('td').text) == 'Total':
        print("Oklahoma scraper is complete.")
    else:
        print("ERROR: Must fix Oklahoma scraper.")
    
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
        #print("County = %s, Cases = %s, Deaths = %s, Negative Test Results = %s" % \
         #     (pull[0].text, pull[1].text, pull[2].text, pull[3].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + ", " + pull[3].text + "\n")
    
    file.close()
    
    if (tags[0].find('td').text) == 'Baker' and (tags[36].find('td').text) == 'Total':
        print("Oregon Scraper is complete.")
    else:
        print("ERROR: Must fix Oregon scraper.")

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
        #print("County = %s, Cases = %s, Deaths = %s" % \
         #     (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()
    
    if (tags[1].find('td').text) == 'Adams' and (tags[60].find('td').text.strip()) == 'York':
        print("Pennsylvania scraper is complete.")
    else:
        print("ERROR: Must fix Pennsylvania scraper.")

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
    
    for h in hold[39:48]:
        take = h.split('\n')
        file.write(take[1] +  ", " + take[5] + "\n")

    file.close()
    
    if (hold[39].split('\n')[1]) == 'Arecibo' and (hold[47].split('\n')[1]) == 'Not available':
        print("Puerto Rico scraper is complete.")
    else:
        print("ERROR: Must fix Puerto Rico scraper.")

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
    
    for h in hold[43:86]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")

    file.close()
    
    if (hold[43].split('\n')[1]) == 'Abbeville' and (hold[85].split('\n')[1]) == 'York':
        print("South Carolina scraper is complete.")
    else:
        print("ERROR: Must fix South Carolina scraper.")

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
        print("South Dakota scraper is complete.")
    else:
        print("ERROR: Must fix South Dakota scraper.")
    
def tnScrape():
    
    tndoh = 'https://www.tn.gov/health/cedep/ncov.html'

    tnClient = req(tndoh)
    
    site_parse = soup(tnClient.read(), 'lxml')
    tnClient.close()
    
    tables = site_parse.find("div", {"class": "containers tn-accordion parbase"}).find("div", {"class": "tn-simpletable parbase"})
    
    colTable = site_parse.find("div", {"class": "row parsys_column tn-3cols"}).findAll("div", {"class": "tn-simpletable parbase"})[2]
    
    fatal = colTable.find('tr')
    fa = fatal.get_text().split('\n')
    faStr = fa[0]
    faNo = fa[1]
    
    tags = tables.findAll('tr')
    
    csvfile = "COVID-19_cases_tndoh.csv"
    headers = "County, Positive Cases \n"
    
    file = open(csvfile, "w")
    file.write(headers)
    
    for tag in tags[1:98]:
        pull = tag.findAll('p')
        #print("County = %s, Positive Cases = %s" % (pull[0].text, pull[1].text))
        
        file.write(pull[0].text + ", " + pull[1].text.replace(',','') + "\n")
    
    file.write("\n")
    file.write(faStr + ", " + faNo + "\n")
    
    file.close()
    
    if (tags[1].find('p').text) == 'Anderson' and (tags[97].find('p').text) == 'Unknown':
        print("Tennessee scraper is complete.")
    else:
        print("ERROR: Must fix Tennessee scraper.")
    
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
    
    for tag in tags[11:136]:
        pull = tag.findAll('td')
        #print("County = %s, No. of Cases = %s, Deaths = %s" % (pull[0].text, pull[1].text, pull[2].text))
        file.write(pull[0].text + ", " + pull[1].text + ", " + pull[2].text + "\n")
    
    file.close()
    
    if (tags[0].find('td').text) == 'Harris' and (tags[135].find('td').text) == 'Wood':
        print("Texas scraper is complete.")
    else:
        print("ERROR: Must fix Texas scraper.")


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
    
    if (tags[0].get_text().split('- ')[0].strip()) == 'Bear River' and (tags[12].get_text().split('- ')[0].strip()) == 'Weber-Morgan county':
        print("Utah scraper is complete.")
    else:
        print("ERROR: Must fix Utah scraper.")
    
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
    
    for h in hold[44:145]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3].split('[')[0] + ", " + take[5].split('[')[0] + "\n")
    
    file.close()
    
    if (hold[44].split('\n')[1]) == 'Accomack County' and (hold[144].split('\n')[1]) == 'York County':
        print("Virginia scraper is complete.")
    else:
        print("ERROR: Must fix Virginia scraper.")
    
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
    
    if (pos == 'Positive') and (pend == 'Pending'):
        print("US Virgin Islands scraper is complete.")
    else:
        print("ERROR: Must fix US Virgin Islands scraper.")

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
    
    for h in hold[42:57]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + "\n")
    
    file.close()
    
    if (hold[42].split('\n')[1]) == 'Addison' and (hold[55].split('\n')[1]) == 'Windsor':
        print("Vermont scraper is complete.")
    else:
        print("ERROR: Must fix Vermont scraper.")
    
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
    
    for h in hold[53:93]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3].split('[')[0].replace(',','') + ", " + take[5].split('[')[0].replace(',','') + ", " + take[7].split('[')[0].replace(',','') + "\n")
    
    file.close()
    
    if (hold[53].split('\n')[1]) == 'Adams' and (hold[92].split('\n')[1]) == '(Unassigned)':
        print("Washington scraper is complete.")
    else:
        print("ERROR: Must fix Washington scraper.")
    
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
    
    if attr[0].get('attributes').get('NAME') == 'Adams' and attr[71].get('attributes').get('NAME') == 'Wood':
        print("Wisconsin scraper is complete.")
    else:
        print("ERROR: Must fix Wisconsin scraper.")
    
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
    file.write(cNo[58] + ", " + cNo[59].strip('(),') + "\n")
    file.write(cNo[60] + ", " + cNo[61].strip('(),') + "\n")
    
    file.close()
    
    if cNo[4] == 'Barbour' and cNo[60] == 'Wood':
        print("West Virginia scraper is complete.")
    else:
        print("ERROR: Must fix West Virginia scraper.")


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
    
    for h in hold[46:69]:
        take = h.split('\n')
        file.write(take[1] + ", " + take[3] + ", " + take[5] + "\n")

    file.close()
    
    if (hold[46].split('\n')[1]) == 'Albany' and (hold[68].split('\n')[1]) == 'Weston':
        print("Wyoming scraper is complete.")
    else:
        print("ERROR: Must fix Wyoming scraper.")
    

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
    nhScrape()
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
