import json
import os, glob
import csv
from urllib.request import Request, urlopen
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from time import sleep

#Used to catch a time out from the Nominatim servers and continue to try
#running the code until it responds
#Information for this code and the code for the Nominatim and geopy comes 
#from their documentation: https://geopy.readthedocs.io/en/stable/#
#and from StackOverflow https://stackoverflow.com/a/48039673
def catch_TimeOut(locale):
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    try:
        return liegen.geocode(locale)
    except GeocoderTimedOut:
        return catch_TimeOut(locale)


def akScrape():
    
    akWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Alaska'

    akClient = req(akWiki)
    
    site_parse = soup(akClient.read(), "lxml")
    akClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_akdoh.csv"
    headers = "Region, State, Latitude, Longitude, Confirmed Cases \n"
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    
    ak = "ALASKA"
    
    anch = liegen.geocode("Anchorage, Alaska")
    gulf = liegen.geocode("Kenai Peninsula Borough, Alaska")
    inter = liegen.geocode("Fairbanks North Star Borough, Alaska")
    matsu = liegen.geocode("Matanuska-Susitna Borough, Alaska")
    north = liegen.geocode("North Slope Borough, Alaska")
    sE = liegen.geocode("Juneau Borough, Alaska")
    sW = liegen.geocode("Bethel, Alaska")
        
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    if (hold[42].split('\n')[1]) == 'Anchorage/Southcentral Alaska' and (hold[48].split('\n')[1]) == 'Southwest':
        
        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(hold[42].split('\n')[1] + ", " + ak + ", " + str(anch.latitude) + ", " + str(anch.longitude) + ", " + hold[42].split('\n')[3] + "\n")
        sleep(1)
        file.write(hold[43].split('\n')[1] + ", " + ak + ", " + str(gulf.latitude) + ", " + str(gulf.longitude) + ", " + hold[43].split('\n')[3] + "\n")
        sleep(1)
        file.write(hold[44].split('\n')[1] + ", " + ak + ", " + str(inter.latitude) + ", " + str(inter.longitude) + ", " + hold[44].split('\n')[3] + "\n")
        sleep(1)
        file.write(hold[45].split('\n')[1] + ", " + ak + ", " + str(matsu.latitude) + ", " + str(matsu.longitude) + ", " + hold[45].split('\n')[3] + "\n")
        sleep(1)
        file.write(hold[46].split('\n')[1] + ", " + ak + ", " + str(north.latitude) + ", " + str(north.longitude) + ", " + hold[46].split('\n')[3] + "\n")
        sleep(1)
        file.write(hold[47].split('\n')[1] + ", " + ak + ", " + str(sE.latitude) + ", " + str(sE.longitude) + ", " + hold[47].split('\n')[3] + "\n")
        sleep(1)
        file.write(hold[48].split('\n')[1] + ", " + ak + ", " + str(sW.latitude) + ", " + str(sW.longitude) + ", " + hold[48].split('\n')[3] + "\n")
        
        file.close()
        
        print("Alaska scraper complete.")
    else:
        print("ERROR: Must fix Alaska scraper.")
    

def alScrape():
    
    aldoh = 'https://services7.arcgis.com/4RQmZZ0yaZkGR1zy/arcgis/rest/services/COV19_Public_Dashboard_ReadOnly/FeatureServer/0/query?where=1%3D1&outFields=CNTYNAME%2CCNTYFIPS%2CCONFIRMED%2CDIED&returnGeometry=false&f=pjson'
    
    alClient = req(aldoh).read().decode('utf-8')
    
    rJS = json.loads(alClient)
    
    attr = rJS.get('features')
    
    csvfile = "COVID-19_cases_aldoh.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    test = []
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    
    if(attr[0].get('attributes').get('CNTYNAME')) == 'Autauga':
        test = True
    else:
        test = False
    
    if test == True:
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for a in attr:
            file.write(a.get('attributes').get('CNTYNAME') + ", " + "ALABAMA" + ", " 
                       + str(liegen.geocode(a.get('attributes').get('CNTYNAME') + " ALABAMA").latitude) + ", " 
                       + str(liegen.geocode(a.get('attributes').get('CNTYNAME') + " ALABAMA").longitude) + ", "
                       + str(a.get('attributes').get('CONFIRMED')) + ", " + str(a.get('attributes').get('DIED')) + "\n")
            catch_TimeOut((a.get('attributes').get('CNTYNAME') + " ALABAMA"))
            sleep(1.1)
        
        file.close()
        print("Alabama scraper is complete.")
    else:
        print("Must fix Alabama scraper.")
    
def arScrape():
    
    arWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Arkansas'
    
    arClient = req(arWiki)
    
    site_parse = soup(arClient.read(), "lxml")
    arClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_arWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    
    hold = []
        
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if (hold[51].split('\n')[1]) == 'Arkansas' and (hold[120].split('\n')[1]) == 'Missing county information':
        
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[51:120]:
            locale = liegen.geocode(h.split('\n')[1] + ", " + "ARKANSAS")
            catch_TimeOut(h.split('\n')[1] + ", " + "ARKANSAS")
            take = h.split('\n')
            file.write(take[1] + ", " + "ARKANSAS" + ", " + str(locale.latitude) + ", " + str(locale.longitude) + ", " + take[3] + ", " + take[5] + ", " + take[7] +"\n")
            sleep(1)
        
        file.write(hold[120].split('\n')[1] + ", " + "ARKANSAS" +  ", " + "" + ", " + "" +", "+ hold[120].split('\n')[3] + ", " + hold[120].split('\n')[5] + ", " + hold[120].split('\n')[7] +"\n")
            
        file.close()
    
    else:
        print("ERROR: Must fix Arkansas scraper.")
        
def aSamScrape():
    
    asWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

    asClient = req(asWiki)
    
    site_parse = soup(asClient.read(), "lxml")
    asClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_asWiki.csv"
    headers = "Region, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    
    aSam = "AMERICAN SAMOA"
    
    asGeo = liegen.geocode(aSam)
    
    sleep(1)
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)
    
    if hold[19].split('\n')[3] == "American Samoa":
    
        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(hold[19].split('\n')[3] + ", " + aSam + ", " + str(asGeo.latitude) 
                   + ", " + str(asGeo.longitude) + ", " + hold[19].split('\n')[5].replace(',','') 
                   + ", " + hold[19].split('\n')[7].replace(',','') + ", " 
                   + hold[19].split('\n')[9].replace(',','') + "\n")
        
        file.close()
        print("American Samoa scraper is complete.")
    else:
        print("ERROR: Must fix American Samoa scraper.")
    
def azScrape():
    
    azWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Arizona'

    azClient = req(azWiki)
    
    site_parse = soup(azClient.read(), "lxml")
    azClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    az = "ARIZONA"
    
    csvfile = "COVID-19_cases_azWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)
    
    if (hold[46].split('\n')[1]) == 'Apache' and (hold[60].split('\n')[1]) == 'Yuma':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[46:61]:
            locale = liegen.geocode(h.split('\n')[1] + ", " + az)
            catch_TimeOut(h.split('\n')[1] + ", " + az)
            take = h.split('\n')
            file.write(take[1] + ", " + az + ", " + str(locale.latitude) + ", " + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
            sleep(1)
        
        #file.write(hold[61].split('\n')[1] + ", " + az + ", " + "" + ", " + ""+ ", "+ hold[61].split('\n')[3] + ", " + hold[61].split('\n')[5] + "\n" )
        
        file.close()
        print("Arizona scraper is complete.")
    else:
        print("ERROR: Must fix Arizona scraper.")
    
    
def caScrape():
    
    cadoh = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_California'
    
    caClient = req(cadoh)
    
    site_parse = soup(caClient.read(), 'lxml')
    caClient.close()
    
    tables = site_parse.find("div", {"class": "tp-container"}).find_all('tbody')
    
    ca = "CALIFORNIA"
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    
    csvfile = "COVID-19_cases_caWiki.csv"
    headers = "County/Region, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)
    
    if (hold[0].split('\n')[1]) == 'Los Angeles' and (hold[52].split('\n')[1]) == 'Tuolumne':

        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[:53]:
            locale = liegen.geocode(h.split('\n')[1].strip('[c]') + ", " + ca)
            catch_TimeOut(h.split('\n')[1].strip('[c]') + ", " + ca)
            take = h.split('\n')
            file.write(take[1] + ", " + ca + ", " + str(locale.latitude) + ", " + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
            sleep(1)
                    
        file.close()
        print("California scraper is complete.")
    else:
        print("ERROR: Must fix California scraper.")
    
def coScrape():

    codoh = 'https://covid19.colorado.gov/case-data'
    
    coClient = req(codoh)
    
    site_parse = soup(coClient.read(), 'lxml')
    coClient.close()
    
    tables = site_parse.findAll("div", {"class": "field field--name-field-card-body field--type-text-long field--label-hidden field--item"})[1]
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    co = "COLORADO"
    
    test = tables.findAll('tr')
    
    adamsTest = test[1].find('td').text
    outTest = test[58].find('td').text
    
    csvfile = "COVID-19_cases_coDOH.csv"
    headers = "County/Region, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    if adamsTest == 'Adams' and outTest == 'Out of state':

        file = open(csvfile, "w")
        file.write(headers)
        
        for t in test[1:57]:
                pull = t.findAll('td')
                locale = liegen.geocode(test[1].find('td').text + ", " + co)
                catch_TimeOut(test[1].find('td').text + ", " + co)
                file.write(pull[0].text + ", " + co + ", " + str(locale.latitude) +
                           ", " + str(locale.longitude) + ", " + pull[1].text + 
                           ", " + pull[2].text + "\n")
                sleep(1)
        
        file.write(test[57].find('td').text + ", " + co + ", " + str(liegen.geocode(co).latitude) 
                   + ", " + str(liegen.geocode(co).longitude) + ", " +
                   test[57].findAll('td')[1].text.strip()+", " +test[57].findAll('td')[2].text.strip()+ "\n")
        
        file.write(test[58].find('td').text + ", " + co + ", " + str(liegen.geocode(co).longitude) 
                   + ", " + str(liegen.geocode(co).longitude) + ", " +
                   test[58].findAll('td')[1].text.strip()+", " +test[58].findAll('td')[2].text.strip()+ "\n")
        
        file.close()
        print("Colorado scraper is complete.")
    else:
        print("ERROR: Must fix Colorado scraper.")

def ctScrape():
    
    ctNews = 'https://www.nbcconnecticut.com/news/local/this-is-where-there-are-confirmed-cases-of-coronavirus-in-connecticut/2243429/'
    
    bypass = {'User-Agent': 'Mozilla/5.0'}
    
    ctClient = Request(ctNews, headers=bypass)
    ctPage = req(ctClient)
    
    site_parse = soup(ctPage.read(), 'lxml')
    ctPage.close()
    
    tables = site_parse.find("div", {"class": "article-content rich-text"})

    listed = tables.findAll('ul')[0]
    
    tags = listed.findAll('li')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    ct = "CONNECTICUT"
    
    csvfile = "COVID-19_cases_ctNews.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, , , , , Pending \n"
    
    hold = []
    
    for li in tags:
        take = li.get_text()
        hold.append(take)

    if hold[0].split('County')[0].strip() == 'Fairfield' and hold[8].split('validation')[0].strip() == 'Pending address':

        file = open(csvfile, "w")
        file.write(headers)
                
        for h in hold[:8]:
            locale = liegen.geocode(h.split('County')[0] + 'County' + ", " + ct)
            file.write(h.split('County')[0] + ", " + ct + ", " + str(locale.latitude) + 
                       ", " + str(locale.longitude) + ", " + h.split('County')[1].strip().replace(',','') +
                       "\n")
            sleep(1)
            catch_TimeOut((h.split('County')[0] + 'County' + ", " + ct))
        
        file.write(ct + ", " + ct + ", " + str(liegen.geocode(ct).latitude) + ", " 
                    + str(liegen.geocode(ct).longitude) + ", " + "" + ", " + "" 
                    + ", " + "" + ", " + "" + ", " + "" + ", " + hold[8].split('validation')[1].strip() + "\n")
        
        file.close()
    
        print("Connecticut scraper is complete.")
    else:
        print("ERROR: Must fix Connecticut scraper.")
    
def dcScrape():
    
    dcWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

    dcClient = req(dcWiki)
    
    site_parse = soup(dcClient.read(), "lxml")
    dcClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_dcWiki.csv"
    headers = "County/Region, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    
    dc = "WASHINGTON DC"
    
    dcGeo = liegen.geocode(dc)
    
    sleep(1)
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

    if hold[26].split('\n')[3] == "Washington D.C.":
    
        file = open(csvfile, "w")
        file.write(headers)
            
        file.write(hold[26].split('\n')[3] + ", " + dc + ", " + str(dcGeo.latitude) 
                   + ", " + str(dcGeo.longitude) + ", " + hold[26].split('\n')[5].replace(',','') 
                   + ", " + hold[26].split('\n')[7].replace(',','') + ", " 
                   + hold[26].split('\n')[9].replace(',','') + "\n")
        
        file.close()
    
        print("DC scraper is complete.")
    else:
        print("ERROR: Must fix DC scraper.")
    
def deScrape():
    
    dedoh = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Delaware'

    deClient = req(dedoh)
    
    site_parse = soup(deClient.read(), 'lxml')
    deClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).findAll('tbody')[3]
    
    pull = tables.findAll('td')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    de = "DELAWARE"
    
    csvfile = "COVID-19_cases_deWiki.csv"
    headers = "County/Region, State, Latitude, Longitude, Confirmed Cases \n"
    
    kent = pull[2].text.strip() + " County"
    kentC = pull[3].text.strip()
    kLocale = liegen.geocode(kent + ", " + de)
    sleep(1)
    newCastle = pull[0].text.strip() + " County"
    newC = pull[1].text.strip()
    nLocale = liegen.geocode(newCastle + ", " + de)
    sleep(1)
    suss = pull[4].text.strip() + " County"
    sussC = pull[5].text.strip() 
    sLocale = liegen.geocode(suss + ", " + de)
    
    if kent == 'Kent County' and suss == 'Sussex County':
 
        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(kent + ", "+ de + ", " + str(kLocale.latitude) + ", " + str(kLocale.longitude) + ", " + kentC + "\n")
        file.write(newCastle + ", "+ de + ", " + str(nLocale.latitude) + ", " + str(nLocale.longitude) + ", " + newC + "\n")
        sleep(1)
        file.write(suss + ", "+ de + ", " + str(sLocale.latitude) + ", " + str(sLocale.longitude) + ", " + sussC + "\n")
        sleep(1)
        
        file.close()
    
        print("Delaware scraper is complete.")
    else:
        print("ERROR: Must fix Delaware scraper.")
    
def flScrape():
    
    flWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Florida'

    flClient = req(flWiki)
    
    site_parse = soup(flClient.read(), "lxml")
    flClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_flWiki.csv"
    headers = "County/Region, State, Latitude, Longitude, Confirmed Cases, Deaths, , , Hospitalizations \n"
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    
    fl = "FLORIDA"
    co = ' County'
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

    if (hold[56].split('\n')[1]) == 'Alachua' and (hold[122].split('\n')[1]) == 'Washington':
    
        file = open(csvfile, "w")
        file.write(headers)
            
        for h in hold[56:123]:
            locale = liegen.geocode(h.split('\n')[1] + ", " + fl)
            catch_TimeOut(h.split('\n')[1] + ", " + fl)
            take = h.split('\n')
            file.write(take[1] + ", " + fl + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[3] + ", " + take[7] + ", " 
                       + "" + ", " + "" + ", " + take[5] +"\n")
            sleep(1)
        file.write(hold[123].split('\n')[1] + ", " + fl + ", " + str(liegen.geocode(fl).latitude) + ", " 
                   + str(liegen.geocode(fl).longitude) + ", " + hold[123].split('\n')[3] 
                   + ", " + hold[123].split('\n')[7] + ", " + "" + ", " + "" 
                   + ", " + hold[123].split('\n')[5] +"\n")
        
        file.close()
    
        print("Florida scraper is complete.")
    else:
        print("ERROR: Must fix Florida scraper.")

def gaScrape():
    
    gadoh = 'https://d20s4vd27d0hk0.cloudfront.net/?initialWidth=616&childId=covid19dashdph&parentTitle=COVID-19%20Daily%20Status%20Report%20%7C%20Georgia%20Department%20of%20Public%20Health&parentUrl=https%3A%2F%2Fdph.georgia.gov%2Fcovid-19-daily-status-report'

    gaClient = req(gadoh)
    
    site_parse = soup(gaClient.read(), 'lxml')
    gaClient.close()
    
    tables = site_parse.find("div", {"id": "summary"}).findAll('tr')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    ga = "GEORGIA"
    
    csvfile = "COVID-19_cases_gadoh.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    if (tables[5].find('td').text) == 'Fulton' and (tables[160].find('td').text) == 'Unknown':

        file = open(csvfile, "w")
        file.write(headers)
        
        for t in tables[5:160]:
                pull = t.findAll('td')
                locale = liegen.geocode(pull[0].text +  " County" + ", " + ga )
                catch_TimeOut(pull[0].text +  " County" + ", " + ga)
                file.write(pull[0].text + ", "+ ga + ", " + str(locale.latitude) + ", " 
                           + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")
                sleep(1)
        
        file.write(tables[160].find('td').text + ", "+ ga + ", " + "" + ", " 
                           + "" + ", " + tables[152].findAll('td')[1].text.strip() 
                           + ", " + tables[152].findAll('td')[2].text.strip() + "\n")
        
        file.close()
    
        print("Georgia scraper is complete.")
    else:
        print("ERROR: Must fix Georgia scraper.")
        
def guScrape():
    
    guDOH = 'http://dphss.guam.gov/covid-19/'

    guClient = req(guDOH)
    
    site_parse = soup(guClient.read(), "lxml")
    guClient.close()
    
    tables = site_parse.find("div", {"class" : "et_pb_row et_pb_row_2"}).findAll('p')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    gu = "GUAM"
    
    csvfile = "COVID-19_cases_guDOH.csv"
    headers = "Region, State, Latitude, Longitude, Positive Cases, Deaths, Recoveries \n"
 
    hold = []
    
    for t in tables:
        take = t.text
        hold.append(take)
        
    locale = liegen.geocode(gu)
    sleep(1)
    pos = hold[0]
    mort = hold[2]
    hope = hold[4]

    if hold[1] == 'POSITIVE':
    
        file = open(csvfile, "w")
        file.write(headers)
            
        file.write(gu + ", " + gu + ", " + str(locale.latitude) + ", " 
                   + str(locale.longitude) + ", " + pos + ", " + mort + ", " + hope + "\n")
        
        file.close()
    
        print("Guam scraper is complete.")
    else:
        print("ERROR: Must fix Guam scraper.")
    
def hiScrape():
    
    hidoh = 'https://health.hawaii.gov/coronavirusdisease2019/what-you-should-know/current-situation-in-hawaii/'

    hiClient = req(hidoh)
    
    site_parse = soup(hiClient.read(), "lxml")
    hiClient.close()
    
    tables = site_parse.find("div", {"id": "inner-wrap"}).find('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    hi= "HAWAII"
    
    csvfile = "COVID-19_cases_hidoh.csv"
    headers = "County, State, Latitude, Longitude, Total Cases, Deaths, Recoveries, Released from Isolation, Req. Hospitalization, , Pending \n"
    
    tags = tables.findAll('td')
    
    hawaii = tags[18].text.replace("\xa0","")
    haLocale = liegen.geocode(hawaii + ", " + hi)
    haTotal = tags[21].text
    haIso = tags[23].text
    haHosp = tags[25].text
    haDeaths = tags[27].text

    honolulu = tags[30].text
    honLocale = liegen.geocode(honolulu + ", " + hi)
    honTotal = tags[33].text
    honIso = tags[35].text
    honHosp = tags[37].text
    honDeaths = tags[39].text

    kauai = tags[42].text
    kauLocale = liegen.geocode(kauai + ", " + hi)
    kauTotal = tags[45].text
    kauIso = tags[47].text
    kauHosp = tags[49].text
    kauDeaths = tags[51].text

    maui = tags[54].text
    mauiLocale = liegen.geocode(maui + ", " + hi)
    mauiTotal = tags[57].text
    mauiIso = tags[59].text
    mauiHosp = tags[61].text
    mauiDeaths = tags[63].text

    outHI = tags[66].text
    outHIno = tags[67].text

    pending = tags[68].text
    penNo = tags[69].text

    if hawaii == 'Hawaii County' and pending == 'County Pending':

        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(hawaii + ", " + hi + ", " + str(haLocale.latitude) + ", " +
                   str(haLocale.longitude) + ", " + haTotal + ", " + haDeaths + ",  " + "" 
                   + ", " + haIso + ", " + haHosp + "\n")
        
        file.write(honolulu + ", " + hi + ", " + str(honLocale.latitude) + ", " +
                   str(honLocale.longitude) + ", " + honTotal + ", " + honDeaths + ",  " + "" 
                   + ", " + honIso + ", " + honHosp + "\n")
        
        
        file.write(kauai + ", " + hi + ", " + str(kauLocale.latitude) + ", " +
                   str(kauLocale.longitude) + ", " + kauTotal + ", " + kauDeaths + ",  " + "" 
                   + ", " + kauIso + ", " + kauHosp + "\n")
        
        file.write(maui + ", " + hi + ", " + str(mauiLocale.latitude) + ", " +
                   str(mauiLocale.longitude) + ", " + mauiTotal + ", " + mauiDeaths + ",  " + "" 
                   + ", " + mauiIso + ", " + mauiHosp + "\n")
        
        file.write(outHI + ", " + hi + ", " + str(liegen.geocode(hi).latitude) + ", " + str(liegen.geocode(hi).longitude) + ", " + outHIno + "\n")
        
        file.write(pending + ", " + hi + ", " + str(liegen.geocode(hi).latitude) + ", " + str(liegen.geocode(hi).longitude) + ", " + "" + ", " + "" + ", " + "" + ", " + "" + ", " + "" + ", " + penNo + "\n")
        
        file.close()
    
        print("Hawai'i scraper is complete.")
    else:
        print("ERROR: Must fix Hawai'i scraper.")

def idScrape():
    
    idWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Idaho'

    idClient = req(idWiki)
    
    site_parse = soup(idClient.read(), "lxml")
    
    idClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    iD = "IDAHO"
    co = ' County'
    
    csvfile = "COVID-19_cases_idWiki.csv"
    headers = "County, State, Latitude, Longitude, Total Cases, Deaths, Recoveries, , , Active Cases \n"
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)
    
    if (hold[35].split('\n')[1]) == 'Ada' and (hold[66].split('\n')[1]) == 'Washington':

        file = open(csvfile, "w")
        file.write(headers)
                    
        for h in hold[35:67]:
            locale = liegen.geocode((h.split('\n')[1] + co) + ", " + iD)
            catch_TimeOut((h.split('\n')[1] + co) + ", " + iD)
            take = h.split('\n')
            file.write(take[1] + ", " + iD + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[9] + ", " + take[5] + ", "
                       + take[7] + ", " + "" + ", " + "" + ", " + take[3] + "\n")
            sleep(1.1)
        
        file.close()
    
        print("Idaho scraper is complete.")
    else:
        print("ERROR: Must fix Idaho scraper.")


def ilScrape():
    
    ilWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Illinois'

    ilClient = req(ilWiki)
    
    site_parse = soup(ilClient.read(), "lxml")
    ilClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    il = "ILLINOIS"
    co = ' County'
    
    csvfile = "COVID-19_cases_ilWiki.csv"
    headers = "County, State, Latitude, Longitude, Total Cases, Deaths, Recoveries, Active Cases \n"
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)
    
    if (hold[66].split('\n')[1]) == 'Adams' and (hold[146].split('\n')[1]) == 'Woodford':
    
        file = open(csvfile, "w")
        file.write(headers)
                    
        for h in hold[66:147]:
            locale = liegen.geocode((h.split('\n')[1]+co) + ", " + il)
            catch_TimeOut((h.split('\n')[1]+co) + ", " + il)
            take = h.split('\n')
            file.write(take[1] + ", " + il + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + take[9].replace(',','') + ", " 
                       + take[5].replace(',','') + ", " + take[7].replace(',','') + ", " 
                       + "" + ", " + "" + ", " + take[3].replace(',','') + "\n")
            sleep(1)
        
        file.write(hold[147].split('\n')[1] + ", " + il + ", " + str(liegen.geocode(il).latitude) + ", "
                       + str(liegen.geocode(il).longitude) + ", " + hold[147].split('\n')[9] + ", " + hold[147].split('\n')[5] + ", " 
                       + hold[147].split('\n')[7] + ", " + "" + ", " + "" + ", "
                       + hold[147].split('\n')[3] + "\n")
        
        file.close()
        
        print("Illinois scraper is complete.\n")
    else:
        print("ERROR: Must fix Illinois scraper.\n")

def inScrape():
    
    inWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Indiana'

    inClient = req(inWiki)
    
    site_parse = soup(inClient.read(), "lxml")
    inClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    inD = "INDIANA"
    co = ' County'
    
    csvfile = "COVID-19_cases_inWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

    if (hold[49].split('\n')[1]) == 'Adams' and (hold[140].split('\n')[1]) == 'Whitley':
    
        file = open(csvfile, "w")
        file.write(headers)
            
        for h in hold[49:123]:
            locale = liegen.geocode((h.split('\n')[1] + co) + ", " + inD)
            catch_TimeOut((h.split('\n')[1] + co) + ", " + inD)
            take = h.split('\n')
            file.write(take[1] + ", " + inD + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[2] + ", " + take[3] + "\n")
            sleep(1)
        
        file.write(hold[123].split('\n')[1] + ", " + inD + ", " + str(liegen.geocode(inD).latitude) + ", " 
                       + str(liegen.geocode(inD).longitude) + ", " + hold[123].split('\n')[2] + ", " + hold[123].split('\n')[3] + "\n")
        
        for h in hold[124:141]:
            locale = liegen.geocode((h.split('\n')[1] + co) + ", " + inD)
            catch_TimeOut((h.split('\n')[1] + co) + ", " + inD)
            take = h.split('\n')
            file.write(take[1] + ", " + inD + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[2] + ", " + take[3] + "\n")
            sleep(1)
        
        file.close()
    
        print("Indiana scraper is complete.")
    else:
        print("ERROR: Must fix Indiana scraper.")

    
def ioScrape():
    
    ioWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Iowa'

    ioClient = req(ioWiki)
    
    site_parse = soup(ioClient.read(), "lxml")
    ioClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    io = "IOWA"
    co = ' County'
    
    csvfile = "COVID-19_cases_ioWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
        
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
                
    if (hold[53].split('\n')[1]) == 'Adair' and (hold[130].split('\n')[1]) == 'Wright':

        file = open(csvfile, "w")
        file.write(headers)
    
        for h in hold[53:131]:
            locale = liegen.geocode(h.split('\n')[1] + co + ", " + io)
            catch_TimeOut(h.split('\n')[1] + co + ", " + io)
            take = h.split('\n')
            file.write(take[1] + ", " + io + ", " + str(locale.latitude) + ", "  
                       + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
            sleep(1)
            
        file.close()
    
        print("Iowa scraper is complete.")
    else:
        print("ERROR: Must fix Iowa Scraper.")

def kaScrape():
    
    kaWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Kansas'

    kaClient = req(kaWiki)
    
    site_parse = soup(kaClient.read(), "lxml")
    kaClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    ka = "KANSAS"
    co = ' County'
    
    csvfile = "COVID-19_cases_kaWiki.csv"
    headers = "County, State, Latitude, Longitude, Cases, Deaths \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    if (hold[53].split('\n')[1]) == 'Atchison' and (hold[109].split('\n')[1]) == 'Wyandotte':
       
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[53:110]:
            locale = liegen.geocode(h.split('\n')[1] + co + ", " + ka)
            catch_TimeOut(h.split('\n')[1] + co + ", " + ka)
            take = h.split('\n')
            file.write(take[1] + ", " + ka + ", " + str(locale.latitude) + ", " +  
                       str(locale.longitude) + ", " + take[3] + ", " + take[4] + "\n")
            sleep(2)
        
        file.close()
    
        print("Kansas scraper is complete.")
    else:
        print("ERROR: Must fix Kansas scraper.")
    
def kyScrape():
    
    kyNews = 'https://www.courier-journal.com/story/news/2020/03/09/coronavirus-kentucky-how-many-cases-and-where-they-kentucky/5001636002/'

    kyClient = req(kyNews)
    
    site_parse = soup(kyClient.read(), "lxml")
    kyClient.close()
    
    tables = site_parse.find("div", {"class": "asset-double-wide double-wide p402_premium"})
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    ky = "KENTUCKY"
    
    csvfile = "COVID-19_cases_kyNews.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths\n"
    
    tag = tables.find_all('p')[12:110]
    
    hold = []
    
    for t in tag:
        take = t.get_text()
        hold.append(take)
        
    if (hold[0].split(':')[0]) == 'Adair County' and (hold[95].split(':')[0]) == 'No County Available':

        file = open(csvfile, "w")
        file.write(headers)
            
        for h in hold[:95]: 
            locale = liegen.geocode(h.split(':')[0] + ", " + ky)
            catch_TimeOut(h.split(':')[0] + ", " + ky)
            file.write(h.split(':')[0] + ", " + ky + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + h.split(':')[1].split('c')[0].strip()
                       + ", " + h.split('case')[1].strip('; ').strip(' death').replace('\xa0', '').strip(',').strip('s').strip() + "\n")
            sleep(1)
        
        file.write(hold[95].split(':')[0] + ", " + ky + ", " + str(liegen.geocode(ky).latitude) + ", " 
                   + str(liegen.geocode(ky).longitude) + ", "
                   + hold[95].split(':')[1].split('c')[0].strip() + ", "
                   + hold[95].split('case')[1].strip('; ').strip(' death').replace('\xa0', '').strip(',').strip('s').strip() + "\n")
            
        file.close()
    
        print("Kentucky scraper is complete.")
    else:
        print("ERROR: Must fix Kentucky scraper.")
    
def laScrape():
    
    laWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Louisiana'

    laClient = req(laWiki)
    
    site_parse = soup(laClient.read(), "lxml")
    laClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    la = "LOUISIANA"
    
    csvfile = "COVID-19_cases_laWiki.csv"
    headers = "Parish, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
        
    if (hold[87].split('\n')[1]) == 'Acadia' and (hold[151].split('\n')[1]) == 'Under Investigation':
            
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[87:151]:
            locale = liegen.geocode(h.split('\n')[1] + ", " + la)
            catch_TimeOut(h.split('\n')[1] + ", " + la)
            sleep(1.1)
            take = h.split('\n')
            file.write(take[1] + ", " + la + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[3].replace(',','') + ", " 
                       + take[5].replace(',','') + "\n")
        
        file.write(hold[151].split('\n')[1] + ", " + la + ", " + str(liegen.geocode(la).latitude) + ", " 
                       + str(liegen.geocode(la).longitude) + ", " + hold[151].split('\n')[3].replace(',','') + ", " 
                       + hold[151].split('\n')[5].replace(',','') + "\n")
        
        file.close()
    
        print("Louisiana scraper is complete.")
    else:
        print("ERROR: Must fix Louisiana scraper.")

def maScrape():
    
    maNews = 'https://www.livescience.com/massachusetts-coronavirus-updates.html'

    maClient = req(maNews)
    
    site_parse = soup(maClient.read(), "lxml")
    maClient.close()
    
    tables = site_parse.find("div", {"itemprop": "articleBody"}).find('ul')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    ma = "MASSACHUSETTS"
    co = ' County'
    
    csvfile = "COVID-19_cases_maNews.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases \n"
    
    tags = tables.findAll('li')
    
    if (tags[0].get_text().split(': ')[0]) == 'Barnstable' and (tags[14].get_text().split(': ')[0]) == 'Unknown':

        file = open(csvfile, "w")
        file.write(headers)
        
        for t in range(0,14):
            locale = liegen.geocode(tags[t].get_text().split(': ')[0] + co + ", " + ma)
            catch_TimeOut(tags[t].get_text().split(': ')[0] + co + ", " + ma)
            file.write(tags[t].get_text().split(': ')[0] + ", " + ma + ", " 
                        + str(locale.latitude) + ", " + str(locale.longitude) + ", "
                        + tags[t].get_text().split(': ')[1].replace(',','') + "\n")
            sleep(1)
        
        file.write(tags[14].get_text().split(': ')[0] + ", " + ma + ", " + str(liegen.geocode(ma).latitude) + ", " 
                   + str(liegen.geocode(ma).longitude) + ", " + tags[14].get_text().split(': ')[1].replace(',','') + "\n")
        
        file.close()
         
        print("Massachusetts scraper is complete.")
    else:
        print("ERROR: Must fix Massachusetts scraper.")

def mdScrape():
    
    mdWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Maryland'

    mdClient = req(mdWiki)
    
    site_parse = soup(mdClient.read(), "lxml")
    mdClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    md = "MARYLAND"
    co = ' County'
    
    csvfile = "COVID-19_cases_mdWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if (hold[78].split('\n')[1]) == 'Allegany' and (hold[102].split('\n')[1]) == 'Unassigned':
                
        file = open(csvfile, "w")
        file.write(headers)
            
        for h in hold[78:102]:
            locale = liegen.geocode(h.split('\n')[1] + co + ", " + md)
            catch_TimeOut(h.split('\n')[1] + co + ", " + md)
            take = h.split('\n')
            file.write(take[1] + ", " + md + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[3] + ", " + take[5] + ", " 
                       + take[7] + "\n")
            sleep(1)
            
        file.write(hold[102].split('\n')[1] + ", " + md + ", " + str(liegen.geocode(md).latitude) + ", " 
                   + str(liegen.geocode(md).longitude) + ", " 
                   + hold[102].split('\n')[3] + ", " + hold[102].split('\n')[5] + ", " 
                   + hold[102].split('\n')[7] + "\n")
        
        file.close()
    
        print("Maryland scraper is complete.")
    else:
        print("ERROR: Must fix Maryland scraper.")
    
def meScrape():
    
    meDDS = 'https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml'

    meClient = req(meDDS)
    
    site_parse = soup(meClient.read(), "lxml")
    meClient.close()
    
    tables = site_parse.find("div", {"id": "Accordion1"}).findAll("td")[5:90]
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    me = "MAINE"
    co = ' County'
        
    csvfile = "COVID-19_cases_meDDS.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"
    
    hold = []
    
    for t in tables:
        take = t.get_text()
        hold.append(take)
        
    andr = hold[0:5]
    anC = andr[0]
    anCC = andr[1]
    anR = andr[2]
    anD = andr[4]
    anLocale = liegen.geocode(anC + co + ", " + me)
    sleep(1)
    aroo = hold[5:10]
    arC = aroo[0]
    arCC = aroo[1]
    arR = aroo[2]
    arD = aroo[4]
    arLocale = liegen.geocode(arC + co + ", " + me)
    sleep(1)
    cumb = hold[10:15]
    cumbC = cumb[0]
    cumbCC = cumb[1]
    cumbR = cumb[2]
    cumbD = cumb[4]
    cLocale = liegen.geocode(cumbC + co + ", " + me)
    sleep(1)
    frank = hold[15:20]
    frC = frank[0]
    frCC = frank[1]
    frR = frank[2]
    frD = frank[4]
    fLocale = liegen.geocode(frC + co + ", " + me)
    sleep(1)
    hanc = hold[20:25]
    haC = hanc[0]
    haCC = hanc[1]
    haR = hanc[2]
    haD = hanc[4]
    hLocale = liegen.geocode(haC + co + ", " + me)
    sleep(1)
    kenne = hold[25:30]
    keC = kenne[0]
    keCC = kenne[1]
    keR = kenne[2]
    keD = kenne[4]
    keLocale = liegen.geocode(keC + co + ", " + me)
    sleep(1)
    knox = hold[30:35]
    knC = knox[0]
    knCC = knox[1]
    knR = knox[2]
    knD = knox[4]
    knLocale = liegen.geocode(knC + co + ", " + me)
    sleep(1)
    linc = hold[35:40]
    linC = linc[0]
    linCC = linc[1]
    linR = linc[2]
    linD = linc[4]
    lLocale = liegen.geocode(linC + co + ", " + me)
    sleep(1)
    ox = hold[40:45]
    oxC = ox[0]
    oxCC = ox[1]
    oxR = ox[2]
    oxD = ox[4]
    oxLocale = liegen.geocode(oxC + co + ", " + me)
    sleep(1)
    peno = hold[45:50]
    penC = peno[0]
    penCC = peno[1]
    penR = peno[2]
    penD = peno[4]
    peLocale = liegen.geocode(penC + co + ", " + me)
    sleep(1)
    pisca = hold[50:55]
    piC = pisca[0]
    piCC = pisca[1]
    piR = pisca[2]
    piD = pisca[4]
    piLocale = liegen.geocode(piC + co + ", " + me)
    sleep(1)
    saga = hold[55:60]
    sC = saga[0]
    sCC = saga[1]
    sR = saga[2]
    sD = saga[4]
    saLocale = liegen.geocode(sC + co + ", " + me)
    sleep(1)
    somer = hold[60:65]
    soC = somer[0]
    soCC = somer[1]
    soR = somer[2]
    soD = somer[4]
    soLocale = liegen.geocode(soC + co + ", " + me)
    sleep(1)
    waldo = hold[65:70]
    wdC = waldo[0]
    wdCC = waldo[1]
    wdR = waldo[2]
    wdD = waldo[4]
    wdLocale = liegen.geocode(wdC + co + ", " + me)
    sleep(1)
    wash = hold[70:75]
    wsC = wash[0]
    wsCC = wash[1]
    wsR = wash[2]
    wsD = wash[4]
    waLocale = liegen.geocode(wsC + co + ", " + me)
    sleep(1)
    york = hold[75:80]
    yC = york[0]
    yCC = york[1]
    yR = york[2]
    yD = york[4]
    yoLocale = liegen.geocode(yC + co + ", " + me)
    sleep(1)
    unk = hold[80:85]
    uC = unk[0]
    uCC = unk[1]
    uR = unk[2]
    uD = unk[4]
    
    if anC == 'Androscoggin' and uC == 'Unknown':
       
        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(anC + ", " + me + ", " + str(anLocale.latitude) + ", " 
                   + str(anLocale.longitude) + ", " + anCC + ", " + anD + ", " + anR +"\n")
        
        file.write(arC + ", " + me + ", " + str(arLocale.latitude) + ", " 
                   + str(arLocale.longitude) + ", " + arCC + ", " + arD + ", " + arR +"\n")
        
        file.write(cumbC + ", " + me + ", " + str(cLocale.latitude) + ", " 
                   + str(cLocale.longitude) + ", " + cumbCC + ", " + cumbD + ", " + cumbR +"\n")
        
        file.write(frC + ", " + me + ", " + str(fLocale.latitude) + ", " 
                   + str(fLocale.longitude) + ", " + frCC + ", " + frD + ", " + frR +"\n")
        
        file.write(haC + ", " + me + ", " + str(hLocale.latitude) + ", " 
                   + str(hLocale.longitude) + ", " + haCC + ", " + haD + ", " + haR +"\n")
        
        file.write(keC + ", " + me + ", " + str(keLocale.latitude) + ", " 
                   + str(keLocale.longitude) + ", " + keCC + ", " + keD + ", " + keR +"\n")
        
        file.write(knC + ", " + me + ", " + str(knLocale.latitude) + ", " 
                   + str(knLocale.longitude) + ", " + knCC + ", " + knD + ", " + knR +"\n")
        
        file.write(linC + ", " + me + ", " + str(lLocale.latitude) + ", " 
                   + str(lLocale.longitude) + ", " + linCC + ", " + linD + ", " + linR +"\n")
        
        file.write(oxC + ", " + me + ", " + str(oxLocale.latitude) + ", " 
                   + str(oxLocale.longitude) + ", " + oxCC + ", " + oxD + ", " + oxR +"\n")
        
        file.write(penC + ", " + me + ", " + str(peLocale.latitude) + ", " 
                   + str(peLocale.longitude) + ", " + penCC + ", " + penD + ", " + penR +"\n")
        
        file.write(piC + ", " + me + ", " + str(piLocale.latitude) + ", " 
                   + str(piLocale.longitude) + ", " + piCC + ", " + piD + ", " + piR +"\n")
        
        file.write(sC + ", " + me + ", " + str(saLocale.latitude) + ", " 
                   + str(saLocale.longitude) + ", " + sCC + ", " + sD + ", " + sR +"\n")
        
        file.write(soC + ", " + me + ", " + str(soLocale.latitude) + ", " 
                   + str(soLocale.longitude) + ", " + soCC + ", " + soD + ", " + soR +"\n")
        
        file.write(wdC + ", " + me + ", " + str(wdLocale.latitude) + ", " 
                   + str(wdLocale.longitude) + ", " + wdCC + ", " + wdD + ", " + wdR +"\n")
        
        file.write(wsC + ", " + me + ", " + str(waLocale.latitude) + ", " 
                   + str(waLocale.longitude) + ", " + wsCC + ", " + wsD + ", " + wsR +"\n")
    
        file.write(yC + ", " + me + ", " + str(yoLocale.latitude) + ", " 
                   + str(yoLocale.longitude) + ", " + yCC + ", " + yD + ", " + yR +"\n")
        
        file.write(uC + ", " + me + ", " + str(liegen.geocode(me).latitude) 
                   + ", " + str(liegen.geocode(me).longitude) + ", " + uCC + ", " + uD + ", " + uR +"\n")
        
        file.close()
    
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
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    mi = "MICHIGAN"
    co = ' County'
    
    csvfile = "COVID-19_cases_midoh.csv"
    headers = "County, State, Latitude, Longitude, Cases, Deaths \n"
    
    if (tags[0].find('td').text.strip()) == 'Allegan' and (tags[75].find('td').text.strip()) == 'Out of State':

        file = open(csvfile, "w")
        file.write(headers)
        
        for tag in tags[0:73]:
            pull = tag.findAll('td')
            locale = liegen.geocode(pull[0].text + co + ", " + mi)
            catch_TimeOut(pull[0].text + co + ", " + mi)
            file.write(pull[0].text + ", " + mi + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")
            sleep(1)
        
        file.write(tags[73].find('td').text.strip() + ", " + mi + ", " + str(liegen.geocode(mi).latitude) + ", " 
                   + str(liegen.geocode(mi).longitude) + ", " + tags[73].findAll('td')[1].text.strip() + ", " 
                   + tags[73].findAll('td')[2].text.strip() + "\n")
        sleep(1)
        file.write(tags[74].find('td').text.strip() + ", " + mi + ", " + str(liegen.geocode(mi).latitude) + ", " 
                   + str(liegen.geocode(mi).longitude) + ", " + tags[74].findAll('td')[1].text.strip() + ", " 
                   + tags[74].findAll('td')[2].text.strip() + "\n")
        sleep(1)
        file.write(tags[75].find('td').text.strip() + ", " + mi + ", " + str(liegen.geocode(mi).latitude) + ", " 
                   + str(liegen.geocode(mi).longitude) + ", " + tags[75].findAll('td')[1].text.strip() + ", " 
                   + tags[75].findAll('td')[2].text.strip() + "\n")
        
        file.close()
    
        print("Michigan scraper is complete.")
    else:
        print("ERROR: Must fix Michigan scraper.")

def mnScrape():
    
    mnDOH = 'https://www.health.state.mn.us/diseases/coronavirus/situation.html'

    mnClient = req(mnDOH)
    
    site_parse = soup(mnClient.read(), "lxml")
    mnClient.close()
    
    tables = site_parse.find("div", {"class": "clearfix"}).findAll("tbody")[3]

    tags = tables.findAll('td')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    mn = "MINNESOTA"
    co = ' County'
    
    csvfile = "COVID-19_cases_mndoh.csv"
    headers = "County, State, Latitude, Longitude, Cases \n"
    
    hold = []
    
    for td in tags:
        take = td.get_text()
        hold.append(take)
        
    if hold[0] == 'Anoka' and hold[192] == 'Yellow Medicine':    
        
        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(hold[0] + ", " + mn + ", " + str(liegen.geocode(hold[0] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[0] + co + ", " + mn).longitude) + ", " 
                   + hold[1] + ", " + hold[2] + "\n")
        sleep(1)
        file.write(hold[3] + ", " + mn + ", " + str(liegen.geocode(hold[3] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[3] + co + ", " + mn).longitude) + ", " + hold[4] 
                   + ", " + hold[5] +"\n")
        sleep(1)
        file.write(hold[6] + ", " + mn + ", " + str(liegen.geocode(hold[6] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[6] + co + ", " + mn).longitude) + ", " + hold[7] 
                   + ", " + hold[8] +"\n")
        sleep(1)
        file.write(hold[9] + ", " + mn + ", " + str(liegen.geocode(hold[9] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[9] + co + ", " + mn).longitude) + ", " + hold[10] 
                   + ", " + hold[11] +"\n")
        sleep(1)
        file.write(hold[12] + ", " + mn + ", " + str(liegen.geocode(hold[12] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[12] + co + ", " + mn).longitude) + ", " + hold[13] 
                   + ", " + hold[14] +"\n")
        sleep(1)
        file.write(hold[15] + ", " + mn + ", " + str(liegen.geocode(hold[15] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[15] + co + ", " + mn).longitude) + ", " + hold[16] 
                   + ", " + hold[17] +"\n")
        sleep(1)
        file.write(hold[18] + ", " + mn + ", " + str(liegen.geocode(hold[18] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[18] + co + ", " + mn).longitude) + ", " + hold[19] 
                   + ", " + hold[20] +"\n")
        sleep(1)
        file.write(hold[21] + ", " + mn + ", " + str(liegen.geocode(hold[21] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[21] + co + ", " + mn).longitude) + ", " + hold[22] 
                   + ", " + hold[23] +"\n")
        sleep(1)
        file.write(hold[24] + ", " + mn + ", " + str(liegen.geocode(hold[24] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[24] + co + ", " + mn).longitude) + ", " + hold[25] 
                   + ", " + hold[26] +"\n")
        sleep(1)
        file.write(hold[27] + ", " + mn + ", " + str(liegen.geocode(hold[27] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[27] + co + ", " + mn).longitude) + ", " + hold[28] 
                   + ", " + hold[29] +"\n")
        sleep(1)
        file.write(hold[30] + ", " + mn + ", " + str(liegen.geocode(hold[30] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[30] + co + ", " + mn).longitude) + ", " + hold[31] 
                   + ", " + hold[32] +"\n")
        sleep(1)
        file.write(hold[33] + ", " + mn + ", " + str(liegen.geocode(hold[33] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[33] + co + ", " + mn).longitude) + ", " + hold[34] 
                   + ", " + hold[35] +"\n")
        sleep(1)
        file.write(hold[36] + ", " + mn + ", " + str(liegen.geocode(hold[36] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[36] + co + ", " + mn).longitude) + ", " + hold[37] 
                   + ", " + hold[38] +"\n")
        sleep(1)
        file.write(hold[39] + ", " + mn + ", " + str(liegen.geocode(hold[39] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[39] + co + ", " + mn).longitude) + ", " + hold[40] 
                   + ", " + hold[41] +"\n")
        sleep(1)
        file.write(hold[42] + ", " + mn + ", " + str(liegen.geocode(hold[42] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[42] + co + ", " + mn).longitude) + ", " + hold[43] 
                   + ", " + hold[44] +"\n")
        sleep(1)
        file.write(hold[45] + ", " + mn + ", " + str(liegen.geocode(hold[45] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[45] + co + ", " + mn).longitude) + ", " + hold[46] 
                   + ", " + hold[47] +"\n")
        sleep(1)
        file.write(hold[48] + ", " + mn + ", " + str(liegen.geocode(hold[48] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[48] + co + ", " + mn).longitude) + ", " + hold[49] 
                   + ", " + hold[50] +"\n")
        sleep(1)
        file.write(hold[51] + ", " + mn + ", " + str(liegen.geocode(hold[51] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[51] + co + ", " + mn).longitude) + ", " + hold[52] 
                   + ", " + hold[53] +"\n")
        sleep(1)
        file.write(hold[54] + ", " + mn + ", " + str(liegen.geocode(hold[54] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[54] + co + ", " + mn).longitude) + ", " + hold[55] 
                   + ", " + hold[56] +"\n")
        sleep(1)
        file.write(hold[57] + ", " + mn + ", " + str(liegen.geocode(hold[57] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[57] + co + ", " + mn).longitude) + ", " + hold[58] 
                   + ", " + hold[59] +"\n")
        sleep(1)
        file.write(hold[60] + ", " + mn + ", " + str(liegen.geocode(hold[60] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[60] + co + ", " + mn).longitude) + ", " + hold[61] 
                   + ", " + hold[62] +"\n")
        sleep(1)
        file.write(hold[63] + ", " + mn + ", " + str(liegen.geocode(hold[63] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[63] + co + ", " + mn).longitude) + ", " + hold[64] 
                   + ", " + hold[65] +"\n")
        sleep(1)
        file.write(hold[66] + ", " + mn + ", " + str(liegen.geocode(hold[66] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[66] + co + ", " + mn).longitude) + ", " + hold[67] 
                   + ", " + hold[68] +"\n")
        sleep(1)
        file.write(hold[69] + ", " + mn + ", " + str(liegen.geocode(hold[69] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[69] + co + ", " + mn).longitude) + ", " + hold[70] 
                   + ", " + hold[71] +"\n")
        sleep(1)
        file.write(hold[72] + ", " + mn + ", " + str(liegen.geocode(hold[72] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[72] + co + ", " + mn).longitude) + ", " + hold[73] 
                   + ", " + hold[74] +"\n")
        sleep(1)
        file.write(hold[75] + ", " + mn + ", " + str(liegen.geocode(hold[75] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[75] + co + ", " + mn).longitude) + ", " + hold[76] 
                   + ", " + hold[77] +"\n")
        sleep(1)
        file.write(hold[78] + ", " + mn + ", " + str(liegen.geocode(hold[78] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[78] + co + ", " + mn).longitude) + ", " + hold[79] 
                   + ", " + hold[80] +"\n")
        sleep(1)
        file.write(hold[81] + ", " + mn + ", " + str(liegen.geocode(hold[81] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[81] + co + ", " + mn).longitude) + ", " + hold[82] 
                   + ", " + hold[83] +"\n")
        sleep(1)
        file.write(hold[84] + ", " + mn + ", " + str(liegen.geocode(hold[84] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[84] + co + ", " + mn).longitude) + ", " + hold[85] 
                   + ", " + hold[86] +"\n")
        sleep(1)
        file.write(hold[87] + ", " + mn + ", " + str(liegen.geocode(hold[87] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[87] + co + ", " + mn).longitude) + ", " + hold[88] 
                   + ", " + hold[89] +"\n")
        sleep(1)
        file.write(hold[90] + ", " + mn + ", " + str(liegen.geocode(hold[90] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[90] + co + ", " + mn).longitude) + ", " + hold[91] 
                   + ", " + hold[92] +"\n")
        sleep(1)
        file.write(hold[93] + ", " + mn + ", " + str(liegen.geocode(hold[93] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[93] + co + ", " + mn).longitude) + ", " + hold[94] 
                   + ", " + hold[95] +"\n")
        sleep(1)
        file.write(hold[96] + ", " + mn + ", " + str(liegen.geocode(hold[96] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[96] + co + ", " + mn).longitude) + ", " + hold[97] 
                   + ", " + hold[98] +"\n")
        sleep(1)
        file.write(hold[99] + ", " + mn + ", " + str(liegen.geocode(hold[99] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[99] + co + ", " + mn).longitude) + ", " + hold[100] 
                   + ", " + hold[101] +"\n")
        sleep(1)
        file.write(hold[102] + ", " + mn + ", " + str(liegen.geocode(hold[102] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[102] + co + ", " + mn).longitude) + ", " + hold[103] 
                   + ", " + hold[104] +"\n")
        sleep(1)
        file.write(hold[105] + ", " + mn + ", " + str(liegen.geocode(hold[105] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[105] + co + ", " + mn).longitude) + ", " + hold[106] 
                   + ", " + hold[107] +"\n")
        sleep(1)
        file.write(hold[108] + ", " + mn + ", " + str(liegen.geocode(hold[108] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[108] + co + ", " + mn).longitude) + ", " + hold[109] 
                   + ", " + hold[110] +"\n")
        sleep(1)
        file.write(hold[111] + ", " + mn + ", " + str(liegen.geocode(hold[111] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[111] + co + ", " + mn).longitude) + ", " + hold[112] 
                   + ", " + hold[113] +"\n")
        sleep(1)
        file.write(hold[114] + ", " + mn + ", " + str(liegen.geocode(hold[114] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[114] + co + ", " + mn).longitude) + ", " + hold[115] 
                   + ", " + hold[116] +"\n")
        sleep(1)
        file.write(hold[117] + ", " + mn + ", " + str(liegen.geocode(hold[117] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[117] + co + ", " + mn).longitude) + ", " + hold[118] 
                   + ", " + hold[119] +"\n")
        sleep(1)
        file.write(hold[120] + ", " + mn + ", " + str(liegen.geocode(hold[120] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[120] + co + ", " + mn).longitude) + ", " + hold[121] 
                   + ", " + hold[122] +"\n")
        sleep(1)
        file.write(hold[123] + ", " + mn + ", " + str(liegen.geocode(hold[123] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[123] + co + ", " + mn).longitude) + ", " + hold[124] 
                   + ", " + hold[125] +"\n")
        sleep(1)
        file.write(hold[126] + ", " + mn + ", " + str(liegen.geocode(hold[126] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[126] + co + ", " + mn).longitude) + ", " + hold[127] 
                   + ", " + hold[128] +"\n")
        sleep(1)
        file.write(hold[129] + ", " + mn + ", " + str(liegen.geocode(hold[129] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[129] + co + ", " + mn).longitude) + ", " + hold[130] 
                   + ", " + hold[131] +"\n")
        sleep(1)
        file.write(hold[132] + ", " + mn + ", " + str(liegen.geocode(hold[132] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[132] + co + ", " + mn).longitude) + ", " + hold[133] 
                   + ", " + hold[134] +"\n")
        sleep(1)
        file.write(hold[135] + ", " + mn + ", " + str(liegen.geocode(hold[135] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[135] + co + ", " + mn).longitude) + ", " + hold[136] 
                   + ", " + hold[137] +"\n")
        sleep(1)
        file.write(hold[138] + ", " + mn + ", " + str(liegen.geocode(hold[138] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[138] + co + ", " + mn).longitude) + ", " + hold[139] 
                   + ", " + hold[140] +"\n")
        sleep(1)
        file.write(hold[141] + ", " + mn + ", " + str(liegen.geocode(hold[141] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[141] + co + ", " + mn).longitude) + ", " + hold[142] 
                   + ", " + hold[143] +"\n")
        sleep(1)
        file.write(hold[144] + ", " + mn + ", " + str(liegen.geocode(hold[144] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[144] + co + ", " + mn).longitude) + ", " + hold[145] 
                   + ", " + hold[146] +"\n")
        sleep(1)
        file.write(hold[147] + ", " + mn + ", " + str(liegen.geocode(hold[147] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[147] + co + ", " + mn).longitude) + ", " + hold[148] 
                   + ", " + hold[149] +"\n")
        sleep(1)
        file.write(hold[150] + ", " + mn + ", " + str(liegen.geocode(hold[150] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[150] + co + ", " + mn).longitude) + ", " + hold[151] 
                   + ", " + hold[152] +"\n")
        sleep(1)
        file.write(hold[153] + ", " + mn + ", " + str(liegen.geocode(hold[153] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[153] + co + ", " + mn).longitude) + ", " + hold[154] 
                   + ", " + hold[155] +"\n")
        sleep(1)
        file.write(hold[156] + ", " + mn + ", " + str(liegen.geocode(hold[156] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[156] + co + ", " + mn).longitude) + ", " + hold[157] 
                   + ", " + hold[158] +"\n")
        sleep(1)
        file.write(hold[159] + ", " + mn + ", " + str(liegen.geocode(hold[159] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[159] + co + ", " + mn).longitude) + ", " + hold[160] 
                   + ", " + hold[161] +"\n")
        sleep(1)
        file.write(hold[162] + ", " + mn + ", " + str(liegen.geocode(hold[162] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[162] + co + ", " + mn).longitude) + ", " + hold[163] 
                   + ", " + hold[164] +"\n")
        sleep(1)
        file.write(hold[165] + ", " + mn + ", " + str(liegen.geocode(hold[165] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[165] + co + ", " + mn).longitude) + ", " + hold[166] 
                   + ", " + hold[167] +"\n")
        sleep(1)
        file.write(hold[168] + ", " + mn + ", " + str(liegen.geocode(hold[168] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[168] + co + ", " + mn).longitude) + ", " + hold[169] 
                   + ", " + hold[170] +"\n")
        sleep(1)
        file.write(hold[171] + ", " + mn + ", " + str(liegen.geocode(hold[171] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[171] + co + ", " + mn).longitude) + ", " + hold[172] 
                   + ", " + hold[173] +"\n")
        sleep(1)
        file.write(hold[174] + ", " + mn + ", " + str(liegen.geocode(hold[174] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[174] + co + ", " + mn).longitude) + ", " + hold[175] 
                   + ", " + hold[176] +"\n")
        sleep(1)
        file.write(hold[177] + ", " + mn + ", " + str(liegen.geocode(hold[177] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[177] + co + ", " + mn).longitude) + ", " + hold[178] 
                   + ", " + hold[179] +"\n")
        sleep(1)
        file.write(hold[180] + ", " + mn + ", " + str(liegen.geocode(hold[180] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[180] + co + ", " + mn).longitude) + ", " + hold[181] 
                   + ", " + hold[182] +"\n")
        sleep(1)
        file.write(hold[183] + ", " + mn + ", " + str(liegen.geocode(hold[183] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[183] + co + ", " + mn).longitude) + ", " + hold[184] 
                   + ", " + hold[185] +"\n")
        sleep(1)
        file.write(hold[186] + ", " + mn + ", " + str(liegen.geocode(hold[186] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[186] + co + ", " + mn).longitude) + ", " + hold[187] 
                   + ", " + hold[188] +"\n")
        sleep(1)
        file.write(hold[189] + ", " + mn + ", " + str(liegen.geocode(hold[189] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[189] + co + ", " + mn).longitude) + ", " + hold[190] 
                   + ", " + hold[191] +"\n")
        sleep(1)
        file.write(hold[192] + ", " + mn + ", " + str(liegen.geocode(hold[192] + co + ", " + mn).latitude) 
                   + ", " + str(liegen.geocode(hold[192] + co + ", " + mn).longitude) + ", " + hold[193] 
                   + ", " + hold[194] +"\n")
        sleep(1)
        
        file.close()
    
        print("Minnesota scraper is complete.")
    else:
        print("ERROR: Must fix Minnesota scraper.")

    
def moScrape():
    
    moDOH = 'https://health.mo.gov/living/healthcondiseases/communicable/novel-coronavirus/results.php'

    moClient = req(moDOH)
    
    site_parse = soup(moClient.read(), "lxml")
    moClient.close()
    
    tables = site_parse.find("div", {"class": "panel-group"}).findAll('tr')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    mo = "MISSOURI"
    co = ' County'
    
    csvfile = "COVID-19_cases_modoh.csv"
    csvFile = "COVID-19_deaths_modoh.csv"
    headers = "County, State, Latitude, Longitude, Cases \n"
    sHeaders = "County, State, Latitude, Longitude, , Deaths \n"
    
    if (tables[1].find('td').text) == 'Adair' and (tables[118].find('td').text) == 'TBD':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for t in tables[1:40]:
            pull = t.findAll('td')
            locale = liegen.geocode(pull[0].text + co + ", " + mo)
            catch_TimeOut(pull[0].text + co + ", " + mo)
            file.write(pull[0].text + ", " + mo + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + pull[1].text + "\n")
            sleep(1.1)
        
        sleep(1)
        
        for t in tables[40:80]:
            pull = t.findAll('td')
            locale = liegen.geocode(pull[0].text + co + ", " + mo)
            catch_TimeOut(pull[0].text + co + ", " + mo)
            file.write(pull[0].text + ", " + mo + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + pull[1].text + "\n")
            sleep(1.1)
        
        for t in tables[80:118]:
            pull = t.findAll('td')
            locale = liegen.geocode(pull[0].text + co + ", " + mo)
            catch_TimeOut(pull[0].text + co + ", " + mo)
            file.write(pull[0].text + ", " + mo + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + pull[1].text + "\n")
            sleep(1)
        
        file.write(tables[118].find('td').text + ", " + mo + ", " + str(liegen.geocode(mo).latitude) + ", "
                       + str(liegen.geocode(mo).longitude) + ", " + tables[118].findAll('td')[1].text + "\n")
        
        file.close()
        
        tablesDe = site_parse.find("div", {"id": "collapseDeaths"}).findAll('tr')
        
        dFile = open(csvFile, "w")
        dFile.write(sHeaders)
        
        for ta in tablesDe[1:17]:
            pullDe = ta.findAll('td')
            localeD = liegen.geocode(pullDe[0].text + co + ", " + mo)
            catch_TimeOut(pullDe[0].text + co + ", " + mo)
            dFile.write(pullDe[0].text + ", " + mo + ", " + str(localeD.latitude) + ", "
                       + str(localeD.longitude) + ", " + "" + ", " + pullDe[1].text + "\n")
            sleep(1)
        
        dFile.write(tablesDe[17].find('td').text + ", " + mo + ", " + str(liegen.geocode(mo).latitude) + ", "
                       + str(liegen.geocode(mo).longitude) + ", " + "" + ", " + tablesDe[17].findAll('td')[1].text + "\n")
        
        dFile.close()
    
        print("Missouri scraper is complete.")
    else:
        print("ERROR: Must fix Missour scraper.")

def mpScrape():
    
    mpWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

    mpClient = req(mpWiki)
    
    site_parse = soup(mpClient.read(), "lxml")
    mpClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_mpWiki.csv"
    headers = "Region, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    
    mp = "NORTHERN MARIANA ISLANDS"
    
    mpGeo = liegen.geocode(mp)
    
    sleep(1)
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if hold[54].split('\n')[3] == "Northern Mariana Islands":

        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(hold[54].split('\n')[3] + ", " + mp + ", " + str(mpGeo.latitude) 
                   + ", " + str(mpGeo.longitude) + ", " + hold[54].split('\n')[5].replace(',','') 
                   + ", " + hold[54].split('\n')[7].replace(',','') + ", " 
                   + hold[54].split('\n')[9].replace(',','') + "\n")
        
        file.close()
    
        print("Northern Mariana Islands scraper is complete.")
    else:
        print("ERROR: Must fix Northern Mariana Islands scraper.")


def msScrape():
    
    msDOH = 'https://msdh.ms.gov/msdhsite/_static/14,0,420.html'

    msClient = req(msDOH)
    
    site_parse = soup(msClient.read(), "lxml")
    msClient.close()
    
    tables = site_parse.find("table", {"id": "msdhTotalCovid-19Cases"}).find("tbody").findAll('tr')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    ms = "MISSISSIPPI"
    co = ' County'
    
    csvfile = "COVID-19_cases_msdoh.csv"
    headers = "County, State, Latitude, Longitude, Cases, Deaths \n"
    
    if (tables[0].find('td').text) == 'Adams' and (tables[80].find('td').text) == 'Yazoo':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for t in tables[:81]:
            pull = t.findAll('td')
            locale = liegen.geocode(pull[0].text + co + ", " + ms)
            catch_TimeOut(pull[0].text + co + ", " + ms)
            file.write(pull[0].text + ", " + ms + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")
            sleep(2)
        
        file.close()
    
        print("Mississippi scraper is complete.\n")
    else:
        print("ERROR: Must fix Mississippi scraper.\n")

def mtScrape():
    
    mtNews = 'https://www.livescience.com/montana-coronavirus-updates.html'

    mtClient = req(mtNews)
    
    site_parse = soup(mtClient.read(), "lxml")
    mtClient.close()
    
    tables = site_parse.find("div", {"id" : "article-body"}).find('ul')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    mt = "MONTANA"
    co = ' County'
    
    csvfile = "COVID-19_cases_mtNews.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases \n"
    
    tags = tables.findAll('li')
 
    if (tags[0].get_text().split(": ")[0]) == 'Gallatin' and (tags[24].get_text().split(": ")[0]) == 'Glacier':

        file = open(csvfile, "w")
        file.write(headers)
        
        for t in tags:
            pull = t.get_text().split(": ")
            locale = liegen.geocode(pull[0] + co + ", " + mt)
            catch_TimeOut(pull[0] + co + ", " + mt)
            file.write(pull[0] + ", " + mt + ", " + str(locale.latitude) + ", " + str(locale.longitude) + ", " + pull[1] + "\n")
            sleep(1)
        
        file.close()
    
        print("Montana scraper is complete.")
    else:
        print("ERROR: Must fix Montana scraper.")

def ncScrape():
    
    ncDOH = 'https://www.ncdhhs.gov/covid-19-case-count-nc#nc-counties-with-cases'

    ncClient = req(ncDOH)
    
    site_parse = soup(ncClient.read(), 'lxml')
    ncClient.close()
    
    tables = site_parse.find("div", {"class": "content band-content landing-wrapper"}).find('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    nc = "NORTH CAROLINA"
    
    csvfile = "COVID-19_cases_ncdoh.csv"
    headers = "County, State, Latitude, Longitude, Cases, Deaths \n"
    
    tags = tables.findAll('tr')
    
    if (tags[0].find('td').text) == 'Alamance County' and (tags[90].find('td').text) == 'Yadkin County':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for tag in tags:
            pull = tag.findAll('td')
            locale = liegen.geocode(pull[0].text + ", " + nc)
            catch_TimeOut(pull[0].text + ", " + nc)
            file.write(pull[0].text + ", " + nc + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + pull[1].text + ", " 
                       + pull[2].text + "\n")
            sleep(1.1)
        
        file.close()
    
        print("North Carolina scraper is complete.")
    else:
        print("ERROR: Must fix North Carolina scraper.")

def ndScrape():
    
    ndWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_North_Dakota'

    ndClient = req(ndWiki)
    
    site_parse = soup(ndClient.read(), "lxml")
    ndClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')

    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    nd = "NORTH DAKOTA"
    co = ' County'
    
    csvfile = "COVID-19_cases_ndWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases \n"
    
    hold = []

    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if hold[46].split('\n')[1] == 'Barnes' and hold[73].split('\n')[1] == 'Ward':

        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[46:74]:
            locale = liegen.geocode(h.split('\n')[1] + co + ", " + nd)
            take = h.split('\n')
            file.write(take[1] + ", " + nd + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[3] + "\n")
            sleep(1.1)
        
        file.close()
    
        print("North Dakota scraper is complete.")
    else:
        print("ERROR: Must fix North Dakota Scraper.")

def neScrape():
    
    neWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Nebraska'

    neClient = req(neWiki)
    
    site_parse = soup(neClient.read(), "lxml")
    neClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    ne = "NEBRASKA"
    co = ' County'
    
    csvfile = "COVID-19_cases_neWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if (hold[49].split('\n')[1]) == 'Adams' and (hold[84].split('\n')[1]) == 'TBD':
                            
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[49:84]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + co + ", " + ne)
            catch_TimeOut(take[1] + co + ", " + ne)
            file.write(take[1] + ", " + ne + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
            sleep(1.1)
        
        file.write(hold[84].split('\n')[1] + ", " + ne + ", " + str(liegen.geocode(ne).latitude)
                   + ", " + str(liegen.geocode(ne).longitude) + ", " 
                   + hold[84].split('\n')[3] + ", " + hold[84].split('\n')[5] + "\n")
        
        file.close()
    
        print("Nebraska scraper is complete.\n")
    else:
        print("ERROR: Must fix Nebraska scraper.\n")

        
def nhScrape():
    
    nhNews = 'https://www.livescience.com/new-hampshire-coronavirus-updates.html'

    nhClient = req(nhNews)
    
    site_parse = soup(nhClient.read(), "lxml")
    nhClient.close()
    
    tables = site_parse.find("article", {"class":"news-article"}).find("div", {"itemprop": "articleBody"}).find('ul')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    nh = "NEW HAMPSHIRE"
    co = ' County'
    
    csvfile = "COVID-19_cases_nhNews.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases \n"
    
    tags = tables.findAll('li')

    if (tags[0].get_text().split(': ')[0]) == 'Hillsborough' and (tags[9].get_text().split(': ')[0]) == 'Coos':

        file = open(csvfile, "w")
        file.write(headers)
            
        for t in range(0,10):
            locale = liegen.geocode(tags[1].get_text().split(': ')[0])
            catch_TimeOut(tags[1].get_text().split(': ')[0])
            file.write(tags[t].get_text().split(': ')[0] + ", " + nh + ", " + str(locale.latitude) 
                        + ", " + str(locale.longitude) + ", " + tags[t].get_text().split(': ')[1] + "\n")
            sleep(1)
        
        file.close()
         
        print("New Hampshire scraper is complete.")
    else:
        print("ERROR: Must fix New Hampshire scraper.")
    
def njScrape():
    
    njWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_New_Jersey'

    njClient = req(njWiki)
    
    site_parse = soup(njClient.read(), "lxml")
    njClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    nj = "NEW JERSEY"
    co = ' County'
    
    csvfile = "COVID-19_cases_njWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
                
    if (hold[54].split('\n')[1]) == 'Atlantic' and (hold[75].split('\n')[1]) == 'Under investigation':
            
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[54:75]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + co + ", " + nj)
            catch_TimeOut(take[1] + co + ", " + nj)
            file.write(take[1] + ", " + nj + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " +take[3].replace(',','') + ", " 
                       + take[5].replace(',','') + ", " + take[7].replace(',','') + "\n")
            sleep(1)
        
        file.write(hold[75].split('\n')[1] + ", " + nj + ", " + str(liegen.geocode(nj).latitude) + ", " 
                   + str(liegen.geocode(nj).longitude) + ", " + hold[75].split('\n')[3].replace(',','') 
                   + ", " + hold[75].split('\n')[5].replace(',','') 
                   + ", " + hold[75].split('\n')[7].replace(',','') + "\n")
        
        file.close()
    
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
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    nm = "NEW MEXICO"
    co = ' County'
    
    csvfile = "COVID-19_cases_nmdoh.csv"
    headers = "County, State, Latitude, Longitude, Cases, Deaths \n"
    
    if (tags[1].find('td').text) == 'Bernalillo County' and (tags[33].find('td').text) == 'Valencia County':

        file = open(csvfile, "w")
        file.write(headers)
        
        for tag in tags[1:]:
            pull = tag.findAll('td')
            locale = liegen.geocode(pull[0].text + ", " + nm)
            catch_TimeOut(pull[0].text + ", " + nm)
            file.write(pull[0].text + ", " + nm + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")
            sleep(1.1)
        
        file.close()
        
        print("New Mexico scraper is complete.")
    else:
        print("ERROR: Must fix New Mexico scraper.")

def nvScrape():
    
    nvNews = 'https://www.livescience.com/nevada-coronavirus-updates.html'

    nvClient = req(nvNews)
    
    site_parse = soup(nvClient.read(), "lxml")
    nvClient.close()
    
    tables = site_parse.find("div", {"itemprop": "articleBody"}).find('ul')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    nv = "NEVADA"
    co = ' County'
    
    csvfile = "COVID-19_cases_nvNews.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases \n"
    
    tags = tables.findAll('li')
    
    if (tags[0].get_text().split(': ')[0]) == 'Clark' and (tags[9].get_text().split(': ')[0]) == 'White Pine':

        file = open(csvfile, "w")
        file.write(headers)
        
        for t in range(0,10):
            locale = liegen.geocode(tags[t].get_text().split(': ')[0] + co + ", " + nv)
            catch_TimeOut(tags[t].get_text().split(': ')[0] + co + ", " + nv)
            file.write(tags[t].get_text().split(': ')[0] + ", " + nv + ", " 
                        + str(locale.latitude) + ", " + str(locale.longitude) + ", "
                        + tags[t].get_text().split(': ')[1].replace(',','') + "\n")
            sleep(1)
        
        file.close()
         
        print("Nevada scraper is complete.")
    else:
        print("ERROR: Must fix Nevada scraper.")

def nyScrape():
    
    nyWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_New_York_(state)'

    nyClient = req(nyWiki)
    
    site_parse = soup(nyClient.read(), "lxml")
    nyClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    ny = "NEW YORK"
    co = ' County'
    
    csvfile = "COVID-19_cases_nydoh.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths, Recoveries\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
                
    if (hold[116].split('\n')[1]) == 'Albany' and (hold[172].split('\n')[1]) == 'Yates':
                
        file = open(csvfile, "w", encoding = 'utf-8')
        file.write(headers)
        
        for h in hold[116:173]:
            take = h.split('\n')
            locale = liegen.geocode(take[1].split('[')[0] + co + ", " + ny)
            catch_TimeOut(take[1].split('[')[0] + co + ", " + ny)
            file.write(take[1].split('[')[0] + ", " + ny + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[3].split('[')[0].replace(',','') + ", " + take[5].replace(',','')
                       + ", " + take[7].replace(',','') + "\n")
            sleep(1)
            
        nycLocale = liegen.geocode(hold[174].split('\n')[1].strip('(a)').strip() + ", " + ny)
        file.write(hold[174].split('\n')[1].strip('(a)').strip() + ", " + ny + ", " + str(nycLocale.latitude) 
                   + ", " + str(nycLocale.longitude) + ", " + hold[174].split('\n')[3].replace(',','') 
                   + ", " + hold[174].split('\n')[5].replace(',','')  + ", " + hold[174].split('\n')[7].replace(',','')  + "\n")    
        
        file.close()
    
        print("New York scraper is complete.")
    else:
        print("ERROR: Must fix New York scraper.")

def ohScrape():
    
    ohWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Ohio'

    ohClient = req(ohWiki)
    
    site_parse = soup(ohClient.read(), "lxml")
    ohClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    oh = "OHIO"
    co = ' County'
    
    csvfile = "COVID-19_cases_ohWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    if (hold[48].split('\n')[1]) == 'Adams' and (hold[130].split('\n')[1]) == 'Wyandot':
                
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[48:131]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + co + ", " + oh)
            catch_TimeOut(take[1] + co + ", " + oh)
            file.write(take[1] + ", " + oh + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
            sleep(1)
        
        file.close()
    
        print("Ohio scraper is complete.")
    else:
        print("ERROR: Must fix Ohio scraper.")

def okScrape():
    
    okDOH = 'https://coronavirus.health.ok.gov/'

    bypass = {'User-Agent': 'Mozilla/5.0'}
    okClient = Request(okDOH, headers=bypass)
    okPage = req(okClient)
    
    site_parse = soup(okPage.read(), "lxml")
    okPage.close()
    
    tables = site_parse.find("table", {"summary": "COVID-19 Cases by County"}).find("tbody")
    
    tags = tables.findAll('tr')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    ok = "OKLAHOMA"
    co = ' County'
    
    csvfile = "COVID-19_cases_okdoh.csv"
    headers = "County, State, Latitude, Longitude, Cases, Deaths \n"
    
    if (tags[0].find('td').text) == 'Adair' and (tags[60].find('td').text) == 'Woodward':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for tag in tags[:61]:
            pull = tag.findAll('td')
            locale = liegen.geocode(pull[0].text + co + ", " + ok)
            catch_TimeOut(pull[0].text + co + ", " + ok)
            file.write(pull[0].text + ", " + ok + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")
            sleep(1)
            
        file.close()
    
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
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    orG = "OREGON"
    co = ' County'
    
    csvfile = "COVID-19_cases_ordoh.csv"
    headers = "County, State, Latitude, Longitude, Positive Cases, Deaths \n"
    
    if (tags[0].find('td').text) == 'Baker' and (tags[36].find('td').text) == 'Total':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for tag in tags[:36]:
            pull = tag.findAll('td')
            locale = liegen.geocode(pull[0].text + co + ", " + orG)
            catch_TimeOut(pull[0].text + co + ", " + orG)
            file.write(pull[0].text + ", " + orG + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + pull[1].text + ", " 
                       + pull[2].text + "\n")
            sleep(1)
        
        file.close()
    
        print("Oregon scraper is complete.")
    else:
        print("ERROR: Must fix Oregon scraper.")

def paScrape():
    
    paDOH = 'https://www.health.pa.gov/topics/disease/coronavirus/Pages/Cases.aspx'

    paClient = req(paDOH)
    
    site_parse = soup(paClient.read(), "lxml")
    paClient.close()
    
    tables = site_parse.find("div", {"class": "ms-rtestate-field", "style": "display:inline"}).find("div", {"style": "text-align:center;"}).find("table", {"class": "ms-rteTable-default"})
    
    tags = tables.findAll('tr')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    pa = "PENNSYLVANIA"
    co = ' County'
    
    csvfile = "COVID-19_cases_padoh.csv"
    headers = "County, State, Latitude, Longitude, Cases, Deaths \n"
    
    if (tags[1].find('td').text) == 'Adams' and (tags[67].find('td').text.strip()) == 'York':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for tag in tags[1:]:
            pull = tag.findAll('td')
            locale = liegen.geocode(pull[0].text + co+ ", " + pa)
            catch_TimeOut(pull[0].text + co+ ", " + pa)
            file.write(pull[0].text + ", " + pa + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + pull[1].text + ", " + pull[2].text + "\n")
            sleep(1)
        
        file.close()
    
        print("Pennsylvania scraper is complete.")
    else:
        print("ERROR: Must fix Pennsylvania scraper.")

def prScrape():
    
    prWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Puerto_Rico'

    prClient = req(prWiki)
    
    site_parse = soup(prClient.read(), "lxml")
    prClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    pr = "PUERTO RICO"
    
    csvfile = "COVID-19_cases_prWiki.csv"
    headers = "Region, State, Latitude, Longitude, Confirmed Cases \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if (hold[47].split('\n')[1]) == 'Arecibo' and (hold[55].split('\n')[1]) == 'Not available':
                
        file = open(csvfile, "w")
        file.write(headers)
                    
        aLocale = liegen.geocode(hold[47].split('\n')[1] + ", PR")
        file.write(hold[47].split('\n')[1] + ", " + pr + ", " + str(aLocale.latitude)
                   + ", " + str(aLocale.longitude) + ", " + hold[47].split('\n')[5] + "\n")
        sleep(1)
        bLocale = liegen.geocode(hold[48].split('\n')[1] + ", PR")
        file.write(hold[48].split('\n')[1] + ", " + pr + ", " + str(bLocale.latitude)
                   + ", " + str(bLocale.longitude) + ", " + hold[48].split('\n')[5] + "\n")
        sleep(1)
        cLocale = liegen.geocode(hold[49].split('\n')[1] + ", PR")
        file.write(hold[49].split('\n')[1] + ", " + pr + ", " + str(cLocale.latitude)
                   + ", " + str(cLocale.longitude) + ", " + hold[49].split('\n')[5] + "\n")
        sleep(1)
        fLocale = liegen.geocode(hold[50].split('\n')[1] + ", PR")
        file.write(hold[50].split('\n')[1] + ", " + pr + ", " + str(fLocale.latitude)
                   + ", " + str(fLocale.longitude) + ", " + hold[50].split('\n')[5] + "\n")
        sleep(1)
        maLocale = liegen.geocode(hold[51].split('\n')[1] + ", PR")
        file.write(hold[51].split('\n')[1] + ", " + pr + ", " + str(maLocale.latitude)
                   + ", " + str(maLocale.longitude) + ", " + hold[51].split('\n')[5] + "\n")
        sleep(1)
        meLocale = liegen.geocode("Canovanas, PR")
        file.write(hold[52].split('\n')[1] + ", " + pr + ", " + str(meLocale.latitude)
                   + ", " + str(meLocale.longitude) + ", " + hold[52].split('\n')[5] + "\n")
        sleep(1)
        pLocale = liegen.geocode(hold[53].split('\n')[1] + ", PR")
        file.write(hold[53].split('\n')[1] + ", " + pr + ", " + str(pLocale.latitude)
                   + ", " + str(pLocale.longitude) + ", " + hold[53].split('\n')[5] + "\n")
        sleep(1)
        file.write(hold[54].split('\n')[1] + ", " + pr + ", " + ""
                   + ", " + "" + ", " + hold[54].split('\n')[5] + "\n")
        file.write(hold[55].split('\n')[1] + ", " + pr + ", " + ""
                   + ", " + "" + ", " + hold[55].split('\n')[5] + "\n")
        
        file.close()
        print("Puerto Rico scraper is complete.")
    else:
        print("ERROR: Must fix Puerto Rico scraper.")
    
def riScrape():
    
    riDOH = 'https://www.nytimes.com/interactive/2020/us/rhode-island-coronavirus-cases.html'

    riClient = req(riDOH)
    
    site_parse = soup(riClient.read(), "lxml")
    riClient.close()
    
    tables = site_parse.find("tbody", {"class": "top-level svelte-yabvh9"})
    
    tags = tables.findAll('td')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    ri = "RHODE ISLAND"
    co = ' County'
    
    csvfile = "COVID-19_cases_riNews.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    hold = []
    
    for t in tags[5:]:
        take = t.text.split('\n')[0]
        hold.append(take)
        
    prov = hold[1]
    provL = liegen.geocode(prov + co + ", " + ri)
    sleep(1)
    provC = hold[2]
    provD = hold[4] 
    kent = hold[7]
    kentL = liegen.geocode(kent + co + ", " + ri)
    sleep(1)
    kentC = hold[8]
    kentD = hold[10]
    wash = hold[13]
    washL = liegen.geocode(wash + co + ", " + ri)
    sleep(1)
    washC = hold[14]
    washD = hold[16]
    new = hold[19]
    newL = liegen.geocode(new + co + ", " + ri)
    sleep(1)
    newC = hold[20]
    newD = hold[22]
    brist = hold[25]
    bristL = liegen.geocode(brist + co + ", " + ri)
    sleep(1)
    bristC = hold[26]
    bristD = hold[28]
    unkn = hold[31]
    unkC = hold[32]
    unkD = hold[34]

    if prov == "Providence" and unkn == "Unknown":
  
        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(prov + ", " + ri + ", " + str(provL.latitude) + ", " 
                   + str(provL.longitude) + ", " + provC + ", " + provD + "\n")
        
        file.write(kent + ", " + ri + ", " + str(kentL.latitude) + ", " 
                   + str(kentL.longitude) + ", " + kentC + ", " + kentD + "\n")
        
        file.write(wash + ", " + ri + ", " + str(washL.latitude) + ", " 
                   + str(washL.longitude) + ", " + washC + ", " + washD + "\n")
        
        file.write(new + ", " + ri + ", " + str(newL.latitude) + ", " 
                   + str(newL.longitude) + ", " + newC + ", " + newD + "\n")
        
        file.write(brist + ", " + ri + ", " + str(bristL.latitude) + ", " 
                   + str(bristL.longitude) + ", " + bristC + ", " + bristD + "\n")
        
        file.write(unkn + ", " + ri + ", " + "" + ", " + "" + ", " + unkC + ", " + unkD + "\n")
        
        file.close()
    
        print("Rhode Island scraper is complete.")
    else:
        print("ERROR: Must fix Rhode Island scraper.")

def scScrape():
    
    scWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_South_Carolina'

    scClient = req(scWiki)
    
    site_parse = soup(scClient.read(), "lxml")
    scClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    sc = "SOUTH CAROLINA"
    co = ' County'
    
    csvfile = "COVID-19_cases_scWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
                
    if (hold[51].split('\n')[1]) == 'Abbeville' and (hold[96].split('\n')[1]) == 'York':
                
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[51:97]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + co + ", " + sc)
            catch_TimeOut(take[1] + co + ", " + sc)
            file.write(take[1] + ", " + sc + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
            sleep(1.1)
        
        file.close()
    
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
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    sd = "SOUTH DAKOTA"
    co = ' County'
    
    csvfile = "COVID-19_cases_sddoh.csv"
    headers = "County, State, Latitude, Longitude, Total Positive Cases, Deaths, Recovered, , Hospitalizations \n"
    
    hold = []
    holdE = []
    
    for t in tags:
        take = t.get_text()
        hold.append(take)
    
    for ta in tages:
        taken = ta.get_text()
        holdE.append(taken)
    
    krankenhaus = holdE[2:4]
    haus = krankenhaus[0]
    hausNo = krankenhaus[1]
    deaths = holdE[4:6]
    mort = deaths[0].strip('**')
    mortNo = deaths[1]
        
    if (hold[0].strip()) == 'Aurora' and (hold[99].strip()) ==  'Yankton' and mort == 'Deaths':

        file = open(csvfile, "w")
        file.write(headers)
        
        locale1 = liegen.geocode(hold[0].strip() + co + ", " + sd)
        file.write(hold[0].strip() + ", " + sd + ", " + str(locale1.latitude) + ", " 
                   + str(locale1.longitude) + ", " + hold[1].strip() + ", " + "" + ", " + hold[2].strip() + "\n")
        sleep(1)
        locale2 = liegen.geocode(hold[3].strip() + co + ", " + sd)
        file.write(hold[3].strip() + ", " + sd + ", " + str(locale2.latitude) + ", " 
                   + str(locale2.longitude) + ", " + hold[4].strip()  + ", " + "" + ", " + hold[5].strip() + "\n")
        sleep(1)
        locale3 = liegen.geocode(hold[6].strip() + co + ", " + sd)
        file.write(hold[6].strip() + ", " + sd + ", " + str(locale3.latitude) + ", " 
                   + str(locale3.longitude) + ", " + hold[7].strip() + ", " + "" + ", " + hold[8].strip() + "\n")
        sleep(1)
        locale4 = liegen.geocode(hold[9].strip() + co + ", " + sd)
        file.write(hold[9].strip() + ", " + sd + ", " + str(locale4.latitude) + ", " 
                   + str(locale4.longitude) + ", " + hold[10].strip() + ", " + "" + ", " + hold[11].strip() + "\n")
        sleep(1)
        locale5 = liegen.geocode(hold[12].strip() + co + ", " + sd)
        file.write(hold[12].strip() + ", " + sd + ", " + str(locale5.latitude) + ", " 
                   + str(locale5.longitude) + ", " + hold[13].strip() + ", "  + "" + ", " + hold[14].strip() + "\n")
        sleep(1)
        locale6 = liegen.geocode(hold[15].strip() + co + ", " + sd)
        file.write(hold[15].strip() + ", " + sd + ", " + str(locale6.latitude) + ", " 
                   + str(locale6.longitude) + ", " + hold[16].strip() + ", "  + "" + ", " + hold[17].strip() + "\n")
        sleep(1)
        locale7 = liegen.geocode(hold[18].strip() + co + ", " + sd)
        file.write(hold[18].strip() + ", " + sd + ", " + str(locale7.latitude) + ", " 
                   + str(locale7.longitude) + ", " + hold[19].strip() + ", " + "" + ", " + hold[20].strip() + "\n")
        sleep(1)
        locale8 = liegen.geocode(hold[21].strip() + co + ", " + sd)
        file.write(hold[21].strip() + ", " + sd + ", " + str(locale8.latitude) + ", " 
                   + str(locale8.longitude) + ", " + hold[22].strip() + ", "  + "" + ", " + hold[23].strip() + "\n")
        sleep(1)
        locale9 = liegen.geocode(hold[24].strip() + co + ", " + sd)
        file.write(hold[24].strip() + ", " + sd + ", " + str(locale9.latitude) + ", " 
                   + str(locale9.longitude) + ", " + hold[25].strip() + ", "  + "" + ", " + hold[26].strip() + "\n")
        sleep(1)
        locale10 = liegen.geocode(hold[27].strip() + co + ", " + sd)
        file.write(hold[27].strip() + ", " + sd + ", " + str(locale10.latitude) + ", " 
                   + str(locale10.longitude) + ", " + hold[28].strip() + ", "  + "" + ", " + hold[29].strip() + "\n")
        sleep(1)
        locale11 = liegen.geocode(hold[30].strip() + co + ", " + sd)
        file.write(hold[30].strip() + ", " + sd + ", " + str(locale11.latitude) + ", " 
                   + str(locale11.longitude) + ", " + hold[31].strip() + ", "  + "" + ", " + hold[32].strip() + "\n")
        sleep(1)
        locale12 = liegen.geocode(hold[33].strip() + co + ", " + sd)
        file.write(hold[33].strip() + ", " + sd + ", " + str(locale12.latitude) + ", " 
                   + str(locale12.longitude) + ", " + hold[34].strip() + ", "  + "" + ", " + hold[35].strip() + "\n")
        sleep(1)
        locale13 = liegen.geocode(hold[36].strip() + co + ", " + sd)
        file.write(hold[36].strip() + ", " + sd + ", " + str(locale13.latitude) + ", " 
                   + str(locale13.longitude) + ", " + hold[37].strip() + ", "  + "" + ", " + hold[38].strip() + "\n")
        sleep(1)
        locale14 = liegen.geocode(hold[0].strip() + co + ", " + sd)
        file.write(hold[39].strip() + ", " + sd + ", " + str(locale14.latitude) + ", " 
                   + str(locale14.longitude) + ", " + hold[40].strip() + ", " + "" + ", " + hold[41].strip() + "\n")
        sleep(1)
        locale15 = liegen.geocode(hold[42].strip() + co + ", " + sd)
        file.write(hold[42].strip() + ", " + sd + ", " + str(locale15.latitude) + ", " 
                   + str(locale15.longitude) + ", " + hold[43].strip() + ", "  + "" + ", " + hold[44].strip() + "\n")
        sleep(1)
        locale16 = liegen.geocode(hold[45].strip() + co + ", " + sd)
        file.write(hold[45].strip() + ", " + sd + ", " + str(locale16.latitude) + ", " 
                   + str(locale16.longitude) + ", " + hold[46].strip() + ", "  + "" + ", " + hold[47].strip() + "\n")
        sleep(1)
        locale17 = liegen.geocode(hold[48].strip() + co + ", " + sd)
        file.write(hold[48].strip() + ", " + sd + ", " + str(locale17.latitude) + ", " 
                   + str(locale17.longitude) + ", " + hold[49].strip() + ", "  + "" + ", " + hold[50].strip() + "\n")
        sleep(1)
        locale18 = liegen.geocode(hold[51].strip() + co + ", " + sd)
        file.write(hold[51].strip() + ", " + sd + ", " + str(locale18.latitude) + ", " 
                   + str(locale18.longitude) + ", " + hold[52].strip() + ", "  + "" + ", " + hold[53].strip() + "\n")
        sleep(1)
        locale19 = liegen.geocode(hold[54].strip() + co + ", " + sd)
        file.write(hold[54].strip() + ", " + sd + ", " + str(locale19.latitude) + ", " 
                   + str(locale19.longitude) + ", " + hold[55].strip() + ", "  + "" + ", " + hold[56].strip() + "\n")
        sleep(1)
        locale20 = liegen.geocode(hold[57].strip() + co + ", " + sd)
        file.write(hold[57].strip() + ", " + sd + ", " + str(locale20.latitude) + ", " 
                   + str(locale20.longitude) + ", " + hold[58].strip() + ", " + "" + ", " + hold[59].strip() + "\n")
        sleep(1)
        locale21 = liegen.geocode(hold[60].strip() + co + ", " + sd)
        file.write(hold[60].strip() + ", " + sd + ", " + str(locale21.latitude) + ", " 
                   + str(locale21.longitude) + ", " + hold[61].strip() + ", "  + "" + ", " + hold[62].strip() + "\n")
        sleep(1)
        locale22 = liegen.geocode(hold[63].strip() + co + ", " + sd)
        file.write(hold[63].strip() + ", " + sd + ", " + str(locale22.latitude) + ", " 
                   + str(locale22.longitude) + ", " + hold[64].strip() + ", "  + "" + ", " + hold[65].strip() + "\n")
        sleep(1)
        locale23 = liegen.geocode(hold[66].strip() + co + ", " + sd)
        file.write(hold[66].strip() + ", " + sd + ", " + str(locale23.latitude) + ", " 
                   + str(locale23.longitude) + ", " + hold[67].strip() + ", "  + "" + ", " + hold[68].strip() + "\n")
        sleep(1)
        locale24 = liegen.geocode(hold[69].strip() + co + ", " + sd)
        file.write(hold[69].strip() + ", " + sd + ", " + str(locale24.latitude) + ", " 
                   + str(locale24.longitude) + ", " + hold[70].strip() + ", "  + "" + ", " + hold[71].strip() + "\n")
        sleep(1)
        locale25 = liegen.geocode(hold[72].strip() + co + ", " + sd)
        file.write(hold[72].strip() + ", " + sd + ", " + str(locale25.latitude) + ", " 
                   + str(locale25.longitude) + ", " + hold[73].strip() + ", "  + "" + ", " + hold[74].strip() + "\n")
        sleep(1)
        locale26 = liegen.geocode(hold[75].strip() + co + ", " + sd)
        file.write(hold[75].strip() + ", " + sd + ", " + str(locale26.latitude) + ", " 
                   + str(locale26.longitude) + ", " + hold[76].strip() + ", " + "" + ", " + hold[77].strip() + "\n")
        sleep(1)
        locale27 = liegen.geocode(hold[78].strip() + co + ", " + sd)
        file.write(hold[78].strip() + ", " + sd + ", " + str(locale27.latitude) + ", " 
                   + str(locale27.longitude) + ", " + hold[79].strip() + ", " + "" + ", " + hold[80].strip() + "\n")
        sleep(1)
        locale28 = liegen.geocode(hold[81].strip() + co + ", " + sd)
        file.write(hold[81].strip() + ", " + sd + ", " + str(locale28.latitude) + ", " 
                   + str(locale28.longitude) + ", " + hold[82].strip() + ", " + "" + ", " + hold[83].strip() + "\n")
        sleep(1)
        locale29 = liegen.geocode(hold[84].strip() + co + ", " + sd)
        file.write(hold[84].strip() + ", " + sd + ", " + str(locale29.latitude) + ", " 
                   + str(locale29.longitude) + ", " + hold[85].strip() + ", " + "" + ", " + hold[86].strip() + "\n")
        sleep(1)
        locale30 = liegen.geocode(hold[87].strip() + co + ", " + sd)
        file.write(hold[87].strip() + ", " + sd + ", " + str(locale30.latitude) + ", " 
                   + str(locale30.longitude) + ", " + hold[88].strip() + ", " + "" + ", " + hold[89].strip() + "\n")
        sleep(1)
        locale31 = liegen.geocode(hold[90].strip() + co + ", " + sd)
        file.write(hold[90].strip() + ", " + sd + ", " + str(locale31.latitude) + ", " 
                   + str(locale31.longitude) + ", " + hold[91].strip() + ", " + "" + ", " + hold[92].strip() + "\n")
        sleep(1)
        locale32 = liegen.geocode(hold[93].strip() + co + ", " + sd)
        file.write(hold[93].strip() + ", " + sd + ", " + str(locale32.latitude) + ", " 
                   + str(locale32.longitude) + ", " + hold[94].strip() + ", " + "" + ", " + hold[95].strip() + "\n")
        sleep(1)
        locale33 = liegen.geocode(hold[96].strip() + co + ", " + sd)
        file.write(hold[96].strip() + ", " + sd + ", " + str(locale33.latitude) + ", " 
                   + str(locale33.longitude) + ", " + hold[97].strip() + ", " + "" + ", " + hold[98].strip() + "\n")
        sleep(1)
        locale34 = liegen.geocode(hold[99].strip() + co + ", " + sd)
        file.write(hold[99].strip() + ", " + sd + ", " + str(locale34.latitude) + ", " 
                   + str(locale34.longitude) + ", " + hold[100].strip() + ", " + "" + ", " + hold[101].strip() + "\n")
        sleep(1)
        
        file.write("SOUTH DAKOTA" + ", " + sd + ", " + str(liegen.geocode("SOUTH DAKOTA").latitude)
                   + ", " + str(liegen.geocode("SOUTH DAKOTA").longitude) + ", " + "" 
                   + ", " + mortNo + ", " + "" + ", " + "" + ", " + hausNo + "\n")
        
            
        file.close()
    
        print("South Dakota scraper is complete.")
    else:
        print("ERROR: Must fix South Dakota scraper.")
    
def tnScrape():
    
    tndoh = 'https://www.tn.gov/health/cedep/ncov.html'

    tnClient = req(tndoh)
    
    site_parse = soup(tnClient.read(), 'lxml')
    tnClient.close()
    
    tables = site_parse.findAll("div", {"class": "tn-simpletable parbase"})[8].find('tbody')   
    colTable = site_parse.find("div", {"class": "fifth-color bgimg"}).findAll("div", {"class": "tn-simpletable parbase"})
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    tn = "TENNESSEE"
    
    #Fatalities 
    faNo = colTable[1].find('tr').find('td').text
    #Recoveries
    recNo = colTable[3].find('tr').find('td').text
    #Hospitalizations
    hosNo = colTable[5].find('tr').find('td').text
    
    tags = tables.findAll('tr')
    
    csvfile = "COVID-19_cases_tndoh.csv"
    headers = "County, State, Latitude, Longitude, Positive Cases, Deaths, Recoveries, , Hospitalizations \n"
    
    if (tags[1].find('p').text) == 'Anderson County' and (tags[96].find('p').text) == 'Out of State':

        file = open(csvfile, "w")
        file.write(headers)
        
        for tag in tags[1:96]:
            pull = tag.findAll('p')
            locale = liegen.geocode(pull[0].text + ", " + tn)
            catch_TimeOut(pull[0].text + ", " + tn)
            file.write(pull[0].text + ", " + tn + ", " + str(locale.latitude) 
                       + ", " +  str(locale.longitude) + ", " + pull[1].text + ", " 
                       + pull[3].text.replace('\xa0','0') + "\n")
            sleep(1)
            
        file.write(tags[96].find('p').text + ", " + tn + ", " + str(liegen.geocode(tn).latitude) 
                   + ", " + str(liegen.geocode(tn).longitude) + ", "
                   + tags[96].findAll('p')[1].text.replace(',','') + ", " + 
                   tags[96].findAll('p')[3].text.replace(',','').replace('\xa0', '0') + "\n")
        
        file.write(tags[97].find('p').text + ", " + tn + ", " + str(liegen.geocode(tn).latitude) 
                   + ", " + str(liegen.geocode(tn).latitude) + ", "
                   + tags[97].findAll('p')[1].text.replace(',','') + ", " + 
                   tags[97].findAll('p')[3].text.replace(',','').replace('\xa0', '0') + "\n")
        
        file.write(tn + ", " + tn + ", " + str(liegen.geocode(tn).latitude) + ", " 
                   + str(liegen.geocode(tn).longitude) + ", " + "" + ", " + "" 
                   + recNo + ", " + "" + ", " + hosNo + "\n")
        
        
        file.close()
    
        print("Tennessee scraper is complete.")
    else:
        print("ERROR: Must fix Tennessee scraper.")
    
def txScrape():
    
    txNews = 'https://apps.texastribune.org/features/2020/tx-coronavirus-tracker/embeds/daily-tables/table-latest/index.html'

    bypass = {'User-Agent': 'Mozilla/5.0'}
    
    txClient = Request(txNews, headers=bypass)
    txPage = req(txClient)
    
    site_parse = soup(txPage, 'lxml')
    txPage.close()
    
    tables = site_parse.find("table", {"class": "dv-table"}).find('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    tx = "TEXAS"
    co = ' County'
    
    csvfile = "COVID-19_cases_txNews.csv"
    headers = "County, State, Latitude, Longitude, No. of Cases, Deaths \n"
    
    tags = tables.findAll('tr')
    
    if (tags[0].find('td').text) == 'Harris' and (tags[170].find('td').text) == 'Tyler':

        file = open(csvfile, "w", encoding = 'utf-8')
        file.write(headers)
        
        for tag in tags[:10]:
            pull = tag.findAll('td')
            locale = liegen.geocode(pull[0].text + co + ", " + tx)
            catch_TimeOut(pull[0].text + co + ", " + tx)
            file.write(pull[0].text + ", " + tx + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + pull[1].text.replace(',','') + ", " + pull[2].text + "\n")
            sleep(1)
        
        for tag in tags[11:80]:
            pull = tag.findAll('td')
            locale = liegen.geocode(pull[0].text + co + ", " + tx)
            catch_TimeOut(pull[0].text + co + ", " + tx)
            file.write(pull[0].text + ", " + tx + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + pull[1].text.replace(',','') + ", " + pull[2].text + "\n")
            sleep(1)
        
        locale1 = liegen.geocode(tags[80].find('td').text.replace(' ', '') + co + ", " + tx)
        file.write(tags[80].find('td').text.replace(' ', '') + ", " + tx + ", " + str(locale1.latitude) + ", " 
                       + str(locale1.longitude) + ", " + tags[80].findAll('td')[1].text.replace(',','') 
                       + ", " + tags[80].findAll('td')[2].text + "\n")
        
        for tag in tags[81:171]:
            pull = tag.findAll('td')
            locale = liegen.geocode(pull[0].text + co + ", " + tx)
            catch_TimeOut(pull[0].text + co + ", " + tx)
            file.write(pull[0].text + ", " + tx + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + pull[1].text.replace(',','') + ", " + pull[2].text + "\n")
            sleep(1.1)
        
        file.close()
    
        print("Texas scraper is complete.")
    else:
        print("ERROR: Must fix Texas scraper.")


def utScrape():
    
    utNews = 'https://www.livescience.com/utah-coronavirus-updates.html'

    utClient = req(utNews)

    site_parse = soup(utClient.read(), 'lxml')
    utClient.close()
    
    tables = site_parse.find("article", {"class": "news-article", "data-id": "Kk2kmK3UhF5L6dgXZf8wHe"}).find("div", {"itemprop": "articleBody"}).findAll('ul')[1]
    
    liegen = Nominatim(user_agent = 'combiner-atomundwolke@gmail.com')
    ut = "UTAH"
    
    csvfile = "COVID-19_cases_utNews.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases \n"
    
    tags = tables.findAll('li')
    
    if (tags[0].get_text().split('- ')[0].strip()) == 'Bear River' and (tags[12].get_text().split('- ')[0].strip()) == 'Weber-Morgan county':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for t in range(0,13):
            locale = liegen.geocode(tags[t].text.split('- ')[0].strip() + ", " + ut)
            catch_TimeOut(tags[t].text.split('- ')[0].strip() + ", " + ut)
            file.write(tags[t].text.split('- ')[0].strip() + ", " + ut + ", " + str(locale.latitude) 
                       + ", " + str(locale.longitude) + ", " 
                       + tags[t].text.split('- ')[1].strip().split('(')[0].strip() + "\n")
        
            sleep(1)
        file.close()
    
        print("Utah scraper is complete.")
    else:
        print("ERROR: Must fix Utah scraper.")
    
def vaScrape():
    
    vaWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Virginia'

    vaClient = req(vaWiki)
    
    site_parse = soup(vaClient.read(), "lxml")
    vaClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    va = "VIRGINIA"
    
    csvfile = "COVID-19_cases_vaWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    if (hold[52].split('\n')[1]) == 'Accomack County' and (hold[176].split('\n')[1]) == 'York County':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[52:76]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + ", " + va)
            catch_TimeOut(take[1] + ", " + va)
            file.write(take[1] + ", " + va + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + take[3].split('[')[0] 
                       + ", " + take[5].split('[')[0] + "\n")
            sleep(1)
            
        for h in hold[78:82]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + ", " + va)
            catch_TimeOut(take[1] + ", " + va)
            file.write(take[1] + ", " + va + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + take[3].split('[')[0] 
                       + ", " + take[5].split('[')[0] + "\n")
            sleep(1)
        
        for h in hold[83:136]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + ", " + va)
            catch_TimeOut(take[1] + ", " + va)
            file.write(take[1] + ", " + va + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + take[3].split('[')[0] 
                       + ", " + take[5].split('[')[0] + "\n")
            sleep(1.1)
        
        for h in hold[137:148]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + ", " + va)
            catch_TimeOut(take[1] + ", " + va)
            file.write(take[1] + ", " + va + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + take[3].split('[')[0] 
                       + ", " + take[5].split('[')[0] + "\n")
            sleep(1)
        
        for h in hold[149:177]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + ", " + va)
            catch_TimeOut(take[1] + ", " + va)
            file.write(take[1] + ", " + va + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + take[3].split('[')[0] 
                       + ", " + take[5].split('[')[0] + "\n")
            sleep(1)
        
        file.close()
    
        print("Virginia scraper is complete.")
    else:
        print("ERROR: Must fix Virginia scraper.")
    
def viScrape():
    
    viDOH = 'https://doh.vi.gov/covid19usvi'

    viClient = req(viDOH)
    
    site_parse = soup(viClient.read(), "lxml")
    viClient.close()
    
    tables = site_parse.find("div", {"class": "field field-name-body field-type-text-with-summary field-label-hidden"}).find("div", {"class":"row"})

    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    vi = "US VIRGIN ISLANDS"
    
    csvfile = "COVID-19_cases_vidoh.csv"
    headers = "State/Territory, State/Territory, Latitude, Longitude, No. of Cases, Deaths, Recovered, , , , Pending \n"
    
    tags = tables.findAll('p')
    
    pos = tags[3].text.split(': ')[0]
    posNo = tags[3].text.split(': ')[1].split('\xa0')[0]
    
    recov = tags[6].text.split(': ')[0]
    recNo = tags[6].text.split(': ')[1].split('/')[0]
    
    pend = tags[5].text.split(': ')[0]
    pendNo = tags[5].text.split(': ')[1].split(' ')[0]
    
    mort = tags[7].text.split(':\xa0')[0]
    mortNo = tags[7].text.split(':\xa0')[1]
    
    if (pos == 'Positive') and (pend == 'Pending'):
    
        file = open(csvfile, "w")
        file.write(headers)
        
        locale = liegen.geocode(vi)
        sleep(1)
        file.write(vi + ", " + vi + ", " + str(locale.latitude) + ", " 
                   + str(locale.longitude) + posNo + ", " + mortNo + ", " 
                   + recNo + ", " + "" + ", " + "" + ", " + pendNo + "\n")
        
        file.close()
    
        print("US Virgin Islands scraper is complete.")
    else:
        print("ERROR: Must fix US Virgin Islands scraper.")

def vtScrape():
    
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
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
                
    if (hold[50].split('\n')[1]) == 'Addison' and (hold[64].split('\n')[1]) == 'N/A[a]':

        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[50:65]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + co + ", " + vt)
            catch_TimeOut(take[1] + co + ", " + vt)
            file.write(take[1] + ", " + vt + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + take[3] + "\n")
            sleep(1)
        
        file.write(hold[63].split('\n')[1] + ", " + vt + ", " + str(liegen.geocode(vt).latitude) + ", "
                       + str(liegen.geocode(vt).longitude) + ", " + hold[63].split('\n')[3] + "\n")
        
        file.close()
    
        print("Vermont scraper is complete.")
    else:
        print("ERROR: Must fix Vermont scraper.")
    
def waScrape():
    
    waWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Washington_(state)'

    waClient = req(waWiki)
    
    site_parse = soup(waClient.read(), "lxml")
    waClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    wa = "WASHINGTON"
    co = ' County'
    
    csvfile = "COVID-19_cases_waWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    if (hold[50].split('\n')[1]) == 'Adams' and (hold[87].split('\n')[1]) == '(Unassigned by county)':
    
        file = open(csvfile, "w")
        file.write(headers)    
    
        for h in hold[50:87]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + co + ", " + wa)
            catch_TimeOut(take[1] + co + ", " + wa)
            file.write(take[1] + ", " + wa + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[3].split('[')[0].replace(',','') 
                       + ", " + take[5].split('[')[0].replace(',','') + "\n")
            sleep(1)
            
        file.write(hold[87].split('\n')[1] + ", " + wa + ", " + str(liegen.geocode(wa).latitude) + ", " 
                       + str(liegen.geocode(wa).longitude) + ", " + hold[87].split('\n')[3].split('[')[0].replace(',','') 
                       + ", " + hold[87].split('\n')[5].split('[')[0].replace(',','') + "\n")
        
        file.close()
    
        print("Washington scraper is complete.")
    else:
        print("ERROR: Must fix Washington scraper.")
    
def wiScrape():
    
    widoh = 'https://services1.arcgis.com/ISZ89Z51ft1G16OK/arcgis/rest/services/COVID19_WI/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=NAME%2CPOSITIVE%2CDEATHS%2CDATE&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=NAME+ASC&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token='

    wiClient = req(widoh).read().decode('utf-8')
    
    wiJS = json.loads(wiClient)
    
    attr = wiJS.get('features')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    wi = "WISCONSIN"
    co = ' County'
    
    csvfile = "COVID-19_cases_widoh.csv"
    headers = "County, State, Latitude, Longitude, Positive Cases, Deaths \n"
    
    if attr[0].get('attributes').get('NAME') == 'Adams' and attr[71].get('attributes').get('NAME') == 'Wood':
     
        file = open(csvfile, "w")
        file.write(headers)
        
        for a in attr:
            file.write(a.get('attributes').get('NAME') + ", " + wi + ", " 
                           + str(liegen.geocode(a.get('attributes').get('NAME') + co + ", " + wi).latitude) + ", " 
                           + str(liegen.geocode(a.get('attributes').get('NAME') + co + ", " + wi).longitude) + ", "
                           + str(a.get('attributes').get('POSITIVE')) + ", " + str(a.get('attributes').get('DEATHS')) + "\n")
            catch_TimeOut(a.get('attributes').get('NAME') + co + ", " + wi)
            sleep(1)
        
        file.close()
    
        print("Wisconsin scraper is complete.")
    else:
        print("ERROR: Must fix Wisconsin scraper.")
    
def wvScrape():
    
    wvWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_West_Virginia'

    wvClient = req(wvWiki)
    
    site_parse = soup(wvClient.read(), "lxml")
    wvClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    wv = "WEST VIRGINIA"
    
    csvfile = "COVID-19_cases_wvdoh.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    if hold[43].split('\n')[1] == 'Barbour County' and hold[85].split('\n')[1] == 'Wyoming County':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[43:86]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + ", " + wv)
            catch_TimeOut(take[1] + ", " + wv)
            file.write(take[1] + ", " + wv + ", " + str(locale.latitude) + ", "
                       + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
            sleep(1)
        
        file.close()
    
        print("West Virginia scraper is complete.")
    else:
        print("ERROR: Must fix West Virginia scraper.")

def wyScrape():
    
    wyWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Wyoming'

    wyClient = req(wyWiki)
    
    site_parse = soup(wyClient.read(), "lxml")
    wyClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    wy = "WYOMING"
    co = ' County'
    
    csvfile = "COVID-19_cases_wyWiki.csv"
    headers = "County, State, Latitude, Longitude, Confirmed Cases, Deaths \n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if (hold[50].split('\n')[1]) == 'Albany' and (hold[72].split('\n')[1]) == 'Weston':
                
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[50:73]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + co + ", " + wy)
            catch_TimeOut(locale)
            file.write(take[1] + ", " + wy + ", " + str(locale.latitude) + ", " 
                       + str(locale.longitude) + ", " + take[3] + ", " + take[5] + "\n")
            sleep(1.1)
        
        file.close()
    
        print("Wyoming scraper is complete.")
    else:
        print("ERROR: Must fix Wyoming scraper.")
    

def main():
    
    akScrape()
    alScrape()
    arScrape()
    aSamScrape()
    azScrape()
    caScrape()
    coScrape()
    ctScrape()
    dcScrape()
    deScrape()
    flScrape()
    gaScrape()
    guScrape()
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
    mpScrape()
    msScrape()
    mtScrape()
    ncScrape()
    ndScrape()
    neScrape()
    nhScrape()
    njScrape()
    nmScrape()
    nvScrape()
    nyScrape()
    ohScrape()
    okScrape()
    orScrape()
    paScrape()
    prScrape()
    riScrape()
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
    
    path = "C:/Users/Erwac/Desktop/COVID-19/Web Scrapers/US States"

    os.chdir(path)
    
    csvFile = "csv"
    
    alles_COVID = []
    
    alles_COVID = [i for i in glob.glob('COVID-19_*.{}'.format(csvFile))]
    
    hold = []
    
    for i in alles_COVID:
        reader = list(csv.reader(open(i)))
        hold.append(reader)
    
    
    headers = ['County/Region', 'State', 'Latitude', 'Longitude', 
               'Confirmed Cases', 'Deaths', 'Recoveries', 'Released from Isolation',
               'Hospitalized', 'Pending']
    
    f = open("combined.csv","w")
    writer = csv.writer(f)
    writer.writerow(headers)
    
    for col in hold:
        writer.writerows(col[1:])

    f.close()

    
if __name__ == "__main__":
    main()
