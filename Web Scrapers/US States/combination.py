import json
import os, glob
import csv
from urllib.request import Request, urlopen
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import geocoder
from time import sleep
import addfips
import pandas as pd

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

fips = addfips.AddFIPS()

def akScrape():
    
    akWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Alaska'
    
    akClient = req(akWiki)
    
    site_parse = soup(akClient.read(), "lxml")
    akClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_akWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases\n"
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    
    #fips = addfips.AddFIPS()
    ak = "ALASKA"
    
    anch = liegen.geocode("Anchorage, Alaska")                      #1
    sleep(1)   
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    #Anchor Point
    anchor = hold[98].split('\n')
    #Anchorage
    anrage = hold[99].split('\n')
    #Bethel
    bethel = hold[100].split('\n')
    #Chugiak
    chugiak = hold[101].split('\n')
    #Craig
    craig = hold[102].split('\n')
    #Delta Junction
    delta = hold[103].split('\n')
    #Eagle River
    eagle = hold[104].split('\n')
    #Fairbanks
    fair = hold[105].split('\n')
    #North Pole
    north = hold[114].split('\n')
    #Girdwood
    gird = hold[106].split('\n')
    #Homer
    homer = hold[107].split('\n')
    #Juneau
    juneau = hold[109].split('\n')
    #Kenai
    kenai = hold[110].split('\n')
    #Ketchikan
    ketch = hold[111].split('\n')
    #Kodiak
    kodiak = hold[112].split('\n')
    #Nome
    nome = hold[113].split('\n')
    #Palmer
    palmer = hold[115].split('\n')
    #Petersburg
    peters = hold[116].split('\n')
    #Seward
    seward = hold[117].split('\n')
    #Soldotna
    sold = hold[118].split('\n')
    #Sterling
    sterl = hold[119].split('\n')
    #Yukon-Koyukuk
    yukon = hold[120].split('\n')
    #Wasilla 
    wasilla = hold[121].split('\n')
    
    
    
    if (hold[98].split('\n')[1]) == 'Anchor Point' and (hold[122].split('\n')[1]) == 'Total':
        
        file = open(csvfile, "w")
        file.write(headers)
        
        #Anchor Point, AK
        file.write(anchor[1] + "," + ak + "," 
                   #+ str(fips.get_county_fips("Kenai Peninsula", state = ak)).strip() 
                   + "03110"
                   + "," + str(geocoder.opencage("Anchor Point, AK",key='').latlng).strip('[]')
                   + "," + anchor[3].replace('\xa0','0') + "\n")
        #Anchorage, AK
        #file.write(hold[89].split('\n')[1] + "," + ak + "," + str(fips.get_county_fips("Anchorage", state = ak)).strip() + "," + str(anch.latitude) + "," + str(anch.longitude) + "," + hold[89].split('\n')[3] + "\n")
        #sleep(1)
        #Bethel, AK
        file.write(bethel[1] + "," + ak + "," 
                   #+ str(fips.get_county_fips("Bethel", state = ak)).strip() 
                   + "06520"
                   + "," + str(geocoder.opencage("Bethel, AK",key='').latlng).strip('[]') 
                   + "," + bethel[3].replace('\xa0','0') + "\n")
        #Chugiak, AK
        file.write(chugiak[1] + "," + ak + "," 
                   #+ str(fips.get_county_fips("Anchorage", state = ak)).strip() + "," 
                   + "14440" + ","
                   + str(geocoder.opencage("Chugiak, AK",key='').latlng).strip('[]') + "," 
                   + chugiak[3].replace('\xa0','0') + "\n")
        #Craig, AK
        file.write(craig[1] + "," + ak + "," 
                   + "02201" + "," + str(geocoder.opencage("Craig, AK",key='').latlng).strip('[]') 
                   + "," + craig[3].replace('\xa0','0') + "\n")
        #Delta Junction, AK
        file.write(delta[1] + "," + ak + "," 
                   #+ str(fips.get_county_fips("Southeast Fairbanks", state = ak)).strip() + "," 
                   + "18620" + ","
                   + str(geocoder.opencage("Delta Junction, AK",key='').latlng).strip('[]') + "," 
                   + delta[3].replace('\xa0','0') + "\n")
        #Eagle River, AK
        file.write(eagle[1] + "," + ak + "," 
                   #+ str(fips.get_county_fips("Anchorage", state = ak)).strip() 
                   + "20490"
                   + "," + str(geocoder.opencage("Eagle River, AK",key='').latlng).strip('[]') 
                   + "," + eagle[3].replace('\xa0','0') + "\n")
        #Fairbanks, AK
        file.write((fair[1] + '/' + hold[110].split('\n')[1]) 
                    + "," + ak + "," + str(fips.get_county_fips("Fairbanks North Star", state = ak)).strip() 
                    + "," + str(geocoder.opencage("Fairbanks, AK",key='').latlng).strip('[]') 
                    + "," + str(int(fair[3]) + int(north[3])) + "\n")
        #Fairbanks North Star
#        file.write(hold[54].split('\n')[1].split(', ')[0] + "," + ak + "," + str(fips.get_county_fips("Fairbanks North Star", state = ak)).strip() + "," + str(liegen.geocode("Fairbanks, AK").latitude) + "," + str(liegen.geocode("Fairbanks, AK").longitude) + "," + hold[54].split('\n')[3] + "\n")
#        sleep(1)
        #Girdwood, AK/ Anchorage
        file.write(gird[1] + "," + ak + "," 
                   + str(fips.get_county_fips("Anchorage", state = ak)).strip() 
                   + "," + str(geocoder.opencage("Girdwood, AK",key='').latlng).strip('[]') 
                   + "," + str(int(gird[3]) + int(anrage[3]))  + "\n")
        #Homer, AK
        file.write(homer[1] + "," + ak + "," 
                   #+ str(fips.get_county_fips("Kenai Peninsula", state = ak)).strip() 
                   + "33140"
                   + "," + str(geocoder.opencage("Homer, AK",key='').latlng).strip('[]') 
                   + "," + homer[3].replace('\xa0','0') + "\n")
        #Juneau, AK
        file.write(juneau[1] + "," + ak + "," 
                   + str(fips.get_county_fips("Juneau", state = ak)).strip() 
                   + "," + str(geocoder.opencage("Juneau, AK",key='').latlng).strip('[]') 
                   + "," + hold[105].split('\n')[3].replace('\xa0','0') + "\n")
        #Kenai, AK
        file.write(kenai[1] + "," + ak + "," 
                   + str(fips.get_county_fips("Kenai Peninsula", state = ak)).strip() 
                   + "," + str(geocoder.opencage("Kenai, AK",key='').latlng).strip('[]') 
                   + "," + kenai[3].replace('\xa0','0') + "\n")
        #Ketchikan, AK
        file.write(ketch[1] + "," + ak + "," 
                   + str(fips.get_county_fips("Ketchikan Gateway", state = ak)).strip() 
                   + "," + str(geocoder.opencage("Ketchikan, AK",key='').latlng).strip('[]') 
                   + "," + ketch[3].replace('\xa0','0') + "\n")
        #North Pole
        #file.write(hold[102].split('\n')[1] + "," + ak + "," + str(fips.get_county_fips("Fairbanks North Star", state = ak)).strip() + "," + str(geocoder.opencage("North Pole, AK",key='').latlng).strip('[]') + "," + hold[102].split('\n')[3] + "\n")
        #Palmer, AK
        file.write(palmer[1] + "," + ak + "," 
                   + str(fips.get_county_fips("Matanuska-Susitna", state = ak)).strip() 
                   + "," + str(geocoder.opencage("Palmer, AK",key='').latlng).strip('[]') 
                   + "," + palmer[3].replace('\xa0','0') + "\n")
        #Petersburg, AK
        file.write(peters[1] + "," + ak + "," 
                   + str(fips.get_county_fips("Petersburg", state = ak)).strip() + "," 
                   + str(geocoder.opencage("Petersburg, AK",key='').latlng).strip('[]') 
                   + "," + peters[3].replace('\xa0','0') + "\n")
        #Seward, AK
        file.write(seward[1] + "," + ak + "," 
                   #+ str(fips.get_county_fips("Kenai Peninsula", state = ak)).strip() + "," 
                   + "68560" + ","
                   + str(geocoder.opencage("Seward, AK",key='').latlng).strip('[]') + "," 
                   + seward[3].replace('\xa0','0') + "\n")
        #Soldotna, AK
        file.write(sold[1] + "," + ak + "," 
                   #+ str(fips.get_county_fips("Kenai Peninsula", state = ak)).strip() + "," 
                   + "71640" + ","
                   + str(geocoder.opencage("Soldotna, AK",key='').latlng).strip('[]') 
                   + "," + sold[3].replace('\xa0','0') + "\n")
        #Sterling, AK
        file.write(sterl[1] + "," + ak + "," 
                   #+ str(fips.get_county_fips("Kenai Peninsula", state = ak)).strip() 
                   + "73070"
                   + "," + str(geocoder.opencage("Sterling, AK",key='').latlng).strip('[]') 
                   + "," + sterl[3].replace('\xa0','0') + "\n")
        #Yukon-Koyukuk, AK
        file.write(yukon[1] + "," + ak + "," 
                   + str(fips.get_county_fips("Yukon-Koyukuk", state = ak)).strip() 
                   + "," + str(geocoder.opencage("Yukon-Koyukuk, AK",key='').latlng).strip('[]') 
                   + "," + yukon[3].replace('\xa0','0') + "\n")
        #Wasilla, AK
        file.write(wasilla[1] + "," + ak + "," 
                   #+ str(fips.get_county_fips("Matanuska-Susitna", state = ak)).strip() + "," 
                   + "83080" + ","
                   + str(geocoder.opencage("Wasilla, AK",key='').latlng).strip('[]') 
                   + "," + wasilla[3].replace('\xa0','0') + "\n")
        #Simply for purposes of allocating counties on map visualization
        file.write("Aleutians East" + "," + ak + "," + str(fips.get_county_fips("Aleutians East", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Aleutians West" + "," + ak + "," + str(fips.get_county_fips("Aleutians West", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Denali" + "," + ak + "," + str(fips.get_county_fips("Denali", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Dillingham" + "," + ak + "," + str(fips.get_county_fips("Dillingham", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Haines" + "," + ak + "," + str(fips.get_county_fips("Haines", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Kodiak Island" + "," + ak + "," + str(fips.get_county_fips("Kodiak Island", state = ak)).strip() + "," + kodiak[3].replace('\xa0','0') + "," + "" + "," + "" + "\n")
        file.write("Lake and Peninsula" + "," + ak + "," + str(fips.get_county_fips("Lake and Peninsula", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Nome" + "," + ak + "," + str(fips.get_county_fips("Nome", state = ak)).strip() + "," + "" + "," + "" + "," + nome[3].replace('\xa0','0') + "\n")
        file.write("Northwest Attic" + "," + ak + "," + "02188" + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Sitka" + "," + ak + "," + str(fips.get_county_fips("Sitka", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Skagway" + "," + ak + "," + str(fips.get_county_fips("Skagway", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Valdez-Cordova" + "," + ak + "," + str(fips.get_county_fips("Valdez-Cordova", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Kusilvak" + "," + ak + "," + str(fips.get_county_fips("Kusilvak", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Wrangell" + "," + ak + "," + str(fips.get_county_fips("Wrangell", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        file.write("Yakutat" + "," + ak + "," + str(fips.get_county_fips("Yakutat", state = ak)).strip() + "," + "" + "," + "" + "," + "" + "\n")
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    al = "ALABAMA"
    
    test = []
    
    if(attr[0].get('attributes').get('CNTYNAME')) == 'Bibb':
        test = True
    else:
        test = False
    
    if test == True:
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for a in attr:
            file.write(a.get('attributes').get('CNTYNAME') + "," + "ALABAMA" + "," + str(fips.get_county_fips(a.get('attributes').get('CNTYNAME'), state=al)).strip() + ","
                       + str(geocoder.opencage(a.get('attributes').get('CNTYNAME') + " ALABAMA", key='').latlng).strip('[]') + "," 
                       + str(a.get('attributes').get('CONFIRMED')) + "," + str(a.get('attributes').get('DIED')) + "\n")
        
        file.close()
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    ar = "ARKANSAS"
    
    hold = []
        
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if (hold[64].split('\n')[1]) == 'Arkansas' and (hold[139].split('\n')[1]) == 'Missing county information':
        
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[64:139]:
            take = h.split('\n')
            file.write(take[1] + "," + ar + "," + fips.get_county_fips(take[1], state = ar) + ","
                       + str(geocoder.opencage(h.split('\n')[1] + "," + ar, key='').latlng).strip('[]') 
                       +  "," + take[3] + "," + take[5] + "," + take[7] +"\n")
        
        file.write(hold[139].split('\n')[1] + "," + ar +  "," + fips.get_state_fips(ar) + ","
                   + str(geocoder.opencage(ar, key='').latlng).strip('[]') 
                   +","+ hold[139].split('\n')[3] + "," 
                   + hold[139].split('\n')[5] + "," 
                   + hold[139].split('\n')[7] +"\n")
            
        file.close()
        
        print("Arkansas scraper is complete.")
    else:
        print("ERROR: Must fix Arkansas scraper.")
        
def aSamScrape():
    
    asWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

    asClient = req(asWiki)
    
    site_parse = soup(asClient.read(), "lxml")
    asClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_asWiki.csv"
    headers = "Region,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    
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
        
        file.write(hold[19].split('\n')[3] + "," + aSam + "," + fips.get_state_fips(aSam) + "," + str(asGeo.latitude) 
                   + "," + str(asGeo.longitude) + "," + hold[19].split('\n')[5].replace(',','') 
                   + "," + hold[19].split('\n')[7].replace(',','') + "," 
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
    
    az = "ARIZONA"
    
    csvfile = "COVID-19_cases_azWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)
    
    if (hold[60].split('\n')[1]) == 'Apache' and (hold[74].split('\n')[1]) == 'Yuma':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[60:75]:
            take = h.split('\n')
            file.write(take[1] + "," + az + "," + str(fips.get_county_fips(take[1], state = az)).strip()
                       + "," + str(geocoder.opencage(take[1] + "," + az, key='').latlng).strip('[]') + "," 
                       + take[3].replace(',','') + "," + take[5].replace(',','') + "\n")
                
        file.close()
        print("Arizona scraper is complete.")
    else:
        print("ERROR: Must fix Arizona scraper.")
    
    
def caScrape():
    
    caWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_California'
    
    caClient = req(caWiki)
    
    site_parse = soup(caClient.read(), 'lxml')
    caClient.close()
    
    tables = site_parse.find("div", {"class": "tp-container"}).find_all('tbody')
    
    ca = "CALIFORNIA"
    
    csvfile = "COVID-19_cases_caWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)
    
    if (hold[0].split('\n')[1]) == 'Los Angeles' and (hold[57].split('\n')[1]) == 'Trinity':

        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[:58]:
            take = h.split('\n')
            file.write(take[1].split('[')[0] + "," + ca + "," + str(fips.get_county_fips(take[1].split('[')[0], state = ca)).strip() 
            + "," + str(geocoder.opencage(take[1].strip('[c]') + "," + ca, key='').latlng).strip('[]')  
            + "," + take[3].replace(',','') + "," + take[5].replace(',','') + "," + take[7].replace('–', '0') + "\n")
                    
        file.close()
        print("California scraper is complete.")
    else:
        print("ERROR: Must fix California scraper.")
    
def coScrape():

    codoh = 'https://covid19.colorado.gov/case-data'
    
    coClient = req(codoh)
    
    site_parse = soup(coClient.read(), 'lxml')
    coClient.close()
    
    tables = site_parse.findAll("div", {"class": "field field--name-field-card-body field--type-text-long field--label-hidden field--item"})[10]
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    co = "COLORADO"
    
    test = tables.findAll('tr')
    
    adamsTest = test[1].find('td').text
    outTest = test[58].find('td').text
    
    csvfile = "COVID-19_cases_coDOH.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    if adamsTest == 'Adams' and outTest == 'Out of state':

        file = open(csvfile, "w")
        file.write(headers)
        
        for t in test[1:43]:
                pull = t.findAll('td')
                file.write(pull[0].text + "," + co + "," + str(fips.get_county_fips(pull[0].text, state = co)).strip() + ","
                           + str(geocoder.opencage(test[1].find('td').text + "," + co, key='').latlng).strip('[]') 
                           + "," + pull[1].text.replace(',','').strip() 
                           + "," + pull[2].text.replace(',','').strip() + "\n")
                
        file.write(test[43].find('td').text.replace('Philips','Phillips') + "," + co + "," 
                   + str(fips.get_county_fips(test[43].find('td').text.replace('Philips','Phillips'),state=co)).strip() + "," 
                   + str(geocoder.opencage(test[43].find('td').text.replace('Philips','Phillips') + ", " + co,key='').latlng).strip('[]')
                   + "," + test[43].findAll('td')[1].text.strip().replace(',','').strip()
                   + "," + test[43].findAll('td')[2].text.strip().replace(',','').strip() + "\n")
        
        for t in test[44:57]:
                pull = t.findAll('td')
                file.write(pull[0].text + "," + co + "," + str(fips.get_county_fips(pull[0].text, state = co)).strip() + ","
                           + str(geocoder.opencage(test[1].find('td').text + "," + co, key='').latlng).strip('[]') 
                           + "," + pull[1].text.replace(',','').strip() 
                           + "," + pull[2].text.replace(',','').strip() + "\n")
        
        file.write(test[57].find('td').text + "," + co + "," + str(fips.get_state_fips(co)).strip() + "," 
                   + str(liegen.geocode(co).latitude) + "," + str(liegen.geocode(co).longitude) + "," 
                   + test[57].findAll('td')[1].text.strip().replace(',','').strip()
                   + "," +test[57].findAll('td')[2].text.strip().replace(',','').strip() + "\n")
        sleep(1)
        file.write(test[58].find('td').text + "," + co + "," + str(fips.get_state_fips(co)).strip() + "," 
                   + str(liegen.geocode(co).longitude) + "," + str(liegen.geocode(co).longitude) + "," 
                   + test[58].findAll('td')[1].text.strip().replace(',','').strip() 
                   + "," + test[58].findAll('td')[2].text.strip().replace(',','').strip() + "\n")
        sleep(1)
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases\n"
    
    hold = []
    
    for li in tags:
        take = li.get_text()
        hold.append(take)

    if hold[0].split('County')[0].strip() == 'Fairfield' and hold[8].split('validation')[0].strip() == 'Pending address':

        file = open(csvfile, "w")
        file.write(headers)
                
        for h in hold[:8]:
            locale = liegen.geocode(h.split(' County')[0] + ' County' + "," + ct)
            file.write(h.split(' County')[0] + "," + ct + "," 
                       + str(fips.get_county_fips(h.split(' County')[0], state = ct)).strip() 
                       + "," + str(locale.latitude) + "," + str(locale.longitude) 
                       + "," + h.split(' County')[1].strip().replace(',','') + "\n")
            sleep(1)
            catch_TimeOut((h.split(' County')[0] + 'County' + "," + ct))
        
        file.write('Pending address' + "," + ct + "," + str(fips.get_state_fips(ct)).strip()
                    + "," + str(liegen.geocode(ct).latitude) + "," 
                    + str(liegen.geocode(ct).longitude) + "," 
                    + hold[8].split('validation')[1].strip().replace(',','') + "\n")
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    
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

    if hold[26].split('\n')[3] == "District of Columbia":
    
        file = open(csvfile, "w")
        file.write(headers)
            
        file.write(hold[26].split('\n')[3] + "," + dc + "," 
                   + str(fips.get_county_fips("Washington", state= "DC")).strip() + "," + str(dcGeo.latitude) 
                   + "," + str(dcGeo.longitude) + "," + hold[26].split('\n')[5].replace(',','')
                   + "," + hold[26].split('\n')[7].replace(',','') + "," 
                   + hold[26].split('\n')[9].replace(',','') + "\n")
        
        file.close()
    
        print("DC scraper is complete.")
    else:
        print("ERROR: Must fix DC scraper.")
    
def deScrape():
    
    deWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Delaware'

    deClient = req(deWiki)
    
    site_parse = soup(deClient.read(), 'lxml')
    deClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).findAll('tbody')[2]
    
    pull = tables.findAll('td')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    de = "DELAWARE"
    
    csvfile = "COVID-19_cases_deWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases\n"
    
    kent = pull[2].text.strip() + " County"
    kentC = pull[3].text.strip().replace(',','')
    kLocale = liegen.geocode(kent + "," + de)
    sleep(1)
    newCastle = pull[0].text.strip() + " County"
    newC = pull[1].text.strip().replace(',','')
    nLocale = liegen.geocode(newCastle + "," + de)
    sleep(1)
    suss = pull[4].text.strip() + " County"
    sussC = pull[5].text.strip().replace(',','')
    sLocale = liegen.geocode(suss + "," + de)
    
    if kent == 'Kent County' and suss == 'Sussex County':
 
        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(kent + ","+ de + "," + str(fips.get_county_fips(kent, state = de)).strip() + "," + str(kLocale.latitude) + "," + str(kLocale.longitude) + "," + kentC + "\n")
        file.write(newCastle + ","+ de + "," + str(fips.get_county_fips(newCastle, state = de)).strip() + "," + str(nLocale.latitude) + "," + str(nLocale.longitude) + "," + newC + "\n")
        file.write(suss + ","+ de + "," + str(fips.get_county_fips(suss, state = de)).strip() + "," + str(sLocale.latitude) + "," + str(sLocale.longitude) + "," + sussC + "\n")
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,,,Hospitalizations\n"
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    
    fl = "FLORIDA"
    co = ' County'
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

    if (hold[69].split('\n')[1]) == 'Alachua' and (hold[135].split('\n')[1]) == 'Washington':
    
        file = open(csvfile, "w")
        file.write(headers)
            
        for h in hold[69:136]:
            take = h.split('\n')
            file.write(take[1] + "," + fl + "," + str(fips.get_county_fips(take[1], state = fl)).strip() + ","
                       + str(geocoder.opencage(h.split('\n')[1] + "," + fl, key='').latlng).strip('[]') 
                       + "," + take[3].replace(',','') + "," + take[7].replace(',','') + "," 
                       + "" + "," + "" + "," + take[5].replace(',','') +"\n")
        file.write(hold[136].split('\n')[1] + "," + fl + "," + str(fips.get_state_fips(fl)).strip() 
                   + "," + str(liegen.geocode(fl).latitude) + "," 
                   + str(liegen.geocode(fl).longitude) + "," + hold[136].split('\n')[3].replace(',','') 
                   + "," + hold[136].split('\n')[7].replace(',','') + "," + "" + "," + "" 
                   + "," + hold[136].split('\n')[5].replace(',','') +"\n")
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    if (tables[5].find('td').text) == 'Fulton' and (tables[162].find('td').text) == 'Unknown':

        file = open(csvfile, "w")
        file.write(headers)
        
        for t in tables[5:162]:
                pull = t.findAll('td')
                file.write(pull[0].text + ","+ ga + "," + str(fips.get_county_fips(pull[0].text, state = ga)).strip() + ","
                           + str(geocoder.opencage(pull[0].text + " County" + "," + ga, key='').latlng).strip('[]')
                           + "," + pull[1].text + "," + pull[2].text + "\n")
        
        file.write(tables[162].find('td').text + ","+ ga + "," + str(fips.get_state_fips(ga)).strip() 
                   + "," + str(liegen.geocode(ga).latitude) + "," 
                   + str(liegen.geocode(ga).longitude) + "," + tables[162].findAll('td')[1].text.strip() 
                   + "," + tables[162].findAll('td')[2].text.strip() + "\n")
        
        file.close()
    
        print("Georgia scraper is complete.")
    else:
        print("ERROR: Must fix Georgia scraper.")
        
def guScrape():
    
    guWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

    guClient = req(guWiki)
    
    site_parse = soup(guClient.read(), "lxml")
    guClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_gu_mp_Wiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    
    gu = "GUAM"
    
    guGeo = liegen.geocode(gu)
    
    sleep(1)
    
    mp = "NORTHERN MARIANA ISLANDS"
    
    mpGeo = liegen.geocode(mp)
    
    sleep(1)

    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

    if hold[29].split('\n')[3] == "Guam" and hold[54].split('\n')[3] == "Northern Mariana Islands":
    
        file = open(csvfile, "w")
        file.write(headers)
            
        file.write(hold[29].split('\n')[3] + "," + gu + "," 
                   + str(fips.get_county_fips(gu, state=gu)).strip() + "," + str(guGeo.latitude) 
                   + "," + str(guGeo.longitude) + "," + hold[29].split('\n')[5].replace(',','').replace('–','0')
                   + "," + hold[29].split('\n')[7].replace(',','').replace('–','0') + "," 
                   + hold[29].split('\n')[9].replace(',','').replace('–','0') + "\n")
    
        file.write(hold[54].split('\n')[3] + "," + mp + "," + str(fips.get_county_fips("Rota",state=mp)).strip() + ","  + str(mpGeo.latitude) 
                   + "," + str(mpGeo.longitude) + "," + hold[54].split('\n')[5].replace(',','').replace('–','0') 
                   + "," + hold[54].split('\n')[7].replace(',','').replace('–','0') + "," 
                   + hold[54].split('\n')[9].replace(',','').replace('\xa0','0').replace('–','0') + "\n")
        
        file.close()
    
        print("Guam/Northern Mariana scraper is complete.")
    else:
        print("ERROR: Must fix Guam/Northern Mariana scraper.")

    
def hiScrape():
    
    hidoh = 'https://health.hawaii.gov/coronavirusdisease2019/what-you-should-know/current-situation-in-hawaii/'

    hiClient = req(hidoh)
    
    site_parse = soup(hiClient.read(), "lxml")
    hiClient.close()
    
    tables = site_parse.find("div", {"class": "primary-content secondary"}).findAll("div", {"class": "wp-block-group"})    

    hi= "HAWAII"
    
    csvfile = "COVID-19_cases_hidoh.csv"
    headers = "County,State,fips,Latitude,Longitude,Total Cases,Deaths,Recoveries,Released from Isolation,Hospitalization,Pending\n"
    
    hawaii = tables[3].find('th').text
    haLocale = str(geocoder.opencage(hawaii + "," + hi, key='').latlng).strip('[]')
    haFIPS = str(fips.get_county_fips(hawaii,state=hi)).strip()
    haTotal = tables[3].findAll('td')[1].text.split(' ')[0]
    haIso = tables[3].findAll('td')[3].text.split(' ')[0]
    haHosp = tables[3].findAll('td')[5].text.split(' ')[0]
    haDeaths = tables[3].findAll('td')[7].text.split(' ')[0]

    honolulu = tables[4].find('th').text
    honLocale = str(geocoder.opencage(honolulu + "," + hi, key='').latlng).strip('[]')
    honFIPS = str(fips.get_county_fips(honolulu,state=hi)).strip()
    honTotal = tables[4].findAll('td')[1].text.split(' ')[0]
    honIso = tables[4].findAll('td')[3].text.split(' ')[0]
    honHosp = tables[4].findAll('td')[5].text.split(' ')[0]
    honDeaths = tables[4].findAll('td')[7].text.split(' ')[0]

    kauai = tables[5].find('th').text
    kauLocale = str(geocoder.opencage(kauai + "," + hi, key='').latlng).strip('[]')
    kauFIPS = str(fips.get_county_fips(kauai,state=hi)).strip()
    kauTotal = tables[5].findAll('td')[1].text.split(' ')[0]
    kauIso = tables[5].findAll('td')[3].text.split(' ')[0]
    kauHosp = tables[5].findAll('td')[5].text.split(' ')[0]
    kauDeaths = tables[5].findAll('td')[7].text.split(' ')[0]

    maui = tables[6].find('th').text
    mauiLocale = str(geocoder.opencage(maui + "," + hi, key='').latlng).strip('[]')
    mauiFIPS = str(fips.get_county_fips(maui,state=hi)).strip()
    mauiTotal = tables[6].findAll('td')[1].text.split(' ')[0]
    mauiIso = tables[6].findAll('td')[3].text.split(' ')[0]
    mauiHosp = tables[6].findAll('td')[5].text.split(' ')[0]
    mauiDeaths = tables[6].findAll('td')[7].text.split(' ')[0]

    outliers = site_parse.find("div", {"class": "primary-content secondary"}).findAll("table", {"class": "has-fixed-layout"})
    outHI = outliers[5].findAll('th')[0].text
    outHIno = outliers[5].findAll('th')[1].text.split(' ')[0]

    pending = outliers[6].findAll('th')[0].text
    penNo = outliers[6].findAll('th')[1].text.split(' ')[0]

    if hawaii == 'HAWAII COUNTY' and pending == 'County Pending':

        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(hawaii + "," + hi + "," + haFIPS + "," + haLocale + "," + haTotal + "," + haDeaths + "," + "" 
                   + "," + haIso + "," + haHosp + "," + penNo + "\n")
        
        file.write(honolulu + "," + hi + "," + honFIPS + "," + honLocale + "," + honTotal + "," + honDeaths + "," + "" 
                   + "," + honIso + "," + honHosp + "," + "" + "\n")
        
        
        file.write(kauai + "," + hi + "," + kauFIPS + "," + kauLocale + "," + kauTotal + "," + kauDeaths + "," + "" 
                   + "," + kauIso + "," + kauHosp + "," + "" + "\n")
        
        file.write(maui + "," + hi + "," + mauiFIPS + "," + mauiLocale + "," + mauiTotal + "," + mauiDeaths + "," + "" 
                   + "," + mauiIso + "," + mauiHosp + "," + "" + "\n")
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)
    
    if (hold[52].split('\n')[1]) == 'Ada' and (hold[83].split('\n')[1]) == 'Washington':

        file = open(csvfile, "w")
        file.write(headers)
                    
        for h in hold[52:84]:
            take = h.split('\n')
            file.write(take[1] + "," + iD + "," + str(fips.get_county_fips(take[1],state=iD)).strip() + "," 
                       + str(geocoder.opencage(take[1] + ", " + iD, key='').latlng).strip('[]') 
                       + "," + take[3] + "," + take[11] + "\n")        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull[2:]:
            take = p.get_text()
            hold.append(take)
    
    if (hold[79].split('\n')[1]) == 'Adams' and (hold[174].split('\n')[1]) == 'Woodford':
    
        file = open(csvfile, "w")
        file.write(headers)
                    
        for h in hold[79:88]:
            take = h.split('\n')
            file.write(take[1] + "," + il + "," + str(fips.get_county_fips(take[1], state=il)).strip() + ","
                       + str(geocoder.opencage(h.split('\n')[1] + co + "," + il, key='').latlng).strip('[]') 
                       + "," + take[3].replace(',','') + "," + take[5].replace(',','')
                       + "," + take[7].replace(',','').replace('–','0') + "\n")
        
#        file.write(hold[88].split('\n')[1] + "," + il + "," + str(fips.get_county_fips(hold[85].split('\n')[1], il)).strip() + "," 
#                   + str(geocoder.opencage(hold[88].split('\n')[1], key='').latlng).strip('[]')
#                   + "," + hold[88].split('\n')[9].replace(',','') + "," + hold[88].split('\n')[5].replace(',','') + "," 
#                   + hold[88].split('\n')[7].replace(',','').split('[')[0] + "\n")
        
        for h in hold[88:175]:
            take = h.split('\n')
            file.write(take[1] + "," + il + "," + str(fips.get_county_fips(take[1], state=il)).strip() + ","
                       + str(geocoder.opencage(h.split('\n')[1] + co + "," + il, key='').latlng).strip('[]') 
                       + "," + take[3].replace(',','') + "," + take[5].replace(',','')
                       + "," + take[7].replace(',','').replace('–','0') + "\n")

        file.close()
        
        print("Illinois scraper is complete.")
    else:
        print("ERROR: Must fix Illinois scraper.")

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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)

    if (hold[65].split('\n')[1]) == 'Adams' and (hold[156].split('\n')[1]) == 'Whitley':
    
        file = open(csvfile, "w")
        file.write(headers)
            
        for h in hold[65:157]:
            take = h.split('\n')
            file.write(take[1] + "," + inD + "," + str(fips.get_county_fips(take[1],state=inD)).strip() + ","
                       + str(geocoder.opencage(h.split('\n')[1] + co + "," + inD, key='').latlng).strip('[]') 
                       + "," + take[2].replace(',','') + "," + take[3].replace(',','') + "\n")        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
        
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
                
    if (hold[67].split('\n')[1]) == 'Adair' and (hold[149].split('\n')[1]) == 'Wright':

        file = open(csvfile, "w")
        file.write(headers)
    
        for h in hold[67:150]:
            take = h.split('\n')
            file.write(take[1] + "," + io + "," + str(fips.get_county_fips(take[1],state=io)).strip() + "," 
                       + str(geocoder.opencage(h.split('\n')[1] + co + "," + io, key='').latlng).strip('[]') 
                       + "," + take[3] + "," + take[5] + "\n")
            
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
    
    ka = "KANSAS"
    co = ' County'
    
    csvfile = "COVID-19_cases_kaWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    if (hold[67].split('\n')[1]) == 'Atchison' and (hold[140].split('\n')[1]) == 'Wyandotte':
       
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[67:141]:
            take = h.split('\n')
            file.write(take[1] + "," + ka + "," + str(fips.get_county_fips(take[1],state=ka)).strip() + ","
                       + str(geocoder.opencage(h.split('\n')[1] + co + "," + ka, key='').latlng).strip('[]') 
                       + "," + take[3].split(' (')[0] + "," + take[4].replace('-','0') + "\n")        
        file.close()
    
        print("Kansas scraper is complete.")
    else:
        print("ERROR: Must fix Kansas scraper.")
    
def kyScrape():
    
    kyJson = 'https://static01.nyt.com/newsgraphics/2020/03/16/coronavirus-maps/b2d7b66583e8633797d7334e882bb87fd854c828/data/timeseries/USA-21.json'
    kyClient = req(kyJson).read().decode('utf-8')
    kJS = json.loads(kyClient)
    
    attr = kJS.get('data')
    
    test = []
    
    if(attr[1].get('subregion')) == 'Fayette':
        test = True
    else:
        test = False

    ky = "KENTUCKY"
    
    csvfile = "COVID-19_cases_kyNews.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
        
    if test == True:

        file = open(csvfile, "w")
        file.write(headers)
            
        for a in attr[1:]:
            file.write(a.get('subregion') + "," + ky + "," + str(fips.get_county_fips(a.get('subregion'), state=ky)).strip() + ","
                       + str(geocoder.opencage(a.get('subregion') + ", " + ky, key='').latlng).strip('[]') + "," 
                       + str(a.get('cases')[-1:]).strip('[]') + "," + str(a.get('deaths')[-1:]).strip('[]') + "," + str(a.get('recovered')[-1:]).strip('[]') + "\n")
            
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
    la = "LOUISIANA"
    
    csvfile = "COVID-19_cases_laWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
        
    if (hold[112].split('\n')[1]) == 'Acadia' and (hold[177].split('\n')[1]) == 'Winn':
            
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[112:178]:
            take = h.split('\n')
            file.write(take[1] + "," + la + "," + str(fips.get_county_fips(take[1],state=la)).strip() + ","
                       + str(geocoder.opencage(h.split('\n')[1] + "," + la, key='').latlng).strip('[]') 
                       + "," + take[5].replace(',','') + "," 
                       + take[7].replace(',','') + "\n")
                
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases\n"
    
    tags = tables.findAll('li')
    
    if (tags[0].get_text().split(': ')[0]) == 'Middlesex' and (tags[14].get_text().split(': ')[0]) == 'Nantucket':

        file = open(csvfile, "w")
        file.write(headers)
        
        for t in range(0,15):
            locale = liegen.geocode(tags[t].get_text().split(': ')[0] + co + "," + ma)
            catch_TimeOut(tags[t].get_text().split(': ')[0] + co + "," + ma)
            file.write(tags[t].get_text().split(': ')[0] + "," + ma + "," + str(fips.get_county_fips(tags[t].get_text().split(': ')[0],state=ma)).strip() 
                       + "," + str(locale.latitude) + "," + str(locale.longitude) + ","
                       + tags[t].get_text().split(': ')[1].replace(',','') + "\n")
            sleep(1)
        
#        file.write(tags[14].get_text().split(': ')[0] + "," + ma + "," + str(fips.get_state_fips(ma) + "," + str(liegen.geocode(ma).latitude)) + "," 
#                   + str(liegen.geocode(ma).longitude) + "," + tags[14].get_text().split(': ')[1].replace(',','') + "\n")
        
        file.close()
         
        print("Massachusetts scraper is complete.")
    else:
        print("ERROR: Must fix Massachusetts scraper.")

def mdScrape():
    
    mdWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Maryland'

    mdClient = req(mdWiki)
    
    site_parse = soup(mdClient.read(), "lxml")
    mdClient.close()
    
    #This was done in order to add DC into the map 
    dcWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

    dcClient = req(dcWiki)
    
    site_parseDC = soup(dcClient.read(), "lxml")
    dcClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    tablesDC = site_parseDC.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    md = "MARYLAND"
    co = ' County'    
    dc = "WASHINGTON DC"
    
    dcGeo = liegen.geocode(dc)
    
    sleep(1)
    
    hold = []
    holdDC = []

    
    csvfile = "COVID-19_cases_mdWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
                
    
    for t in tablesDC:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            holdDC.append(take)

    if (hold[93].split('\n')[1]) == 'Allegany' and (hold[117].split('\n')[1]) == 'Unassigned' and holdDC[26].split('\n')[3] == "District of Columbia":
                
        file = open(csvfile, "w")
        file.write(headers)
            
        for h in hold[93:117]:
            take = h.split('\n')
            file.write(take[1] + "," + md + "," + str(fips.get_county_fips(take[1],state=md)).strip() + ","
                       + str(geocoder.opencage(h.split('\n')[1] + co + "," + md, key='').latlng).strip('[]') 
                       + "," + take[3].replace(',','') + "," + take[5].replace(',','') + "," 
                       + take[7].replace(',','') + "\n")
            
        file.write(hold[117].split('\n')[1] + "," + md + "," + str(fips.get_state_fips(md)).strip() + "," + str(liegen.geocode(md).latitude) + "," 
                   + str(liegen.geocode(md).longitude) + "," 
                   + hold[117].split('\n')[3].replace(',','') + "," + hold[117].split('\n')[5].replace(',','') + "," 
                   + hold[117].split('\n')[7].replace(',','') + "\n")
        
        file.write(holdDC[26].split('\n')[3] + "," + dc + "," 
                   + str(fips.get_county_fips("Washington", state= "DC")).strip() + "," + str(dcGeo.latitude) 
                   + "," + str(dcGeo.longitude) + "," + holdDC[26].split('\n')[5].replace(',','')
                   + "," + holdDC[26].split('\n')[7].replace(',','') + "," 
                   + holdDC[26].split('\n')[9].replace(',','') + "\n")
        
        file.close()
    
        print("Maryland scraper is complete.")
    else:
        print("ERROR: Must fix Maryland scraper.")
    
def meScrape():
    
    meDDS = 'https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml'

    meClient = req(meDDS)
    
    site_parse = soup(meClient.read(), "lxml")
    meClient.close()
    
    tables = site_parse.find("div", {"id": "Accordion1"}).findAll("td")[23:108]
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    me = "MAINE"
    co = ' County'
        
    csvfile = "COVID-19_cases_meDDS.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries,,Hospitalizations\n"
    
    hold = []
    
    for t in tables:
        take = t.get_text()
        hold.append(take)
        
    andr = hold[0:5]
    anC = andr[0]
    anCC = andr[1].replace('\xa0','')
    anR = andr[2].replace('\xa0','')
    anH = andr[3].replace('\xa0','')
    anD = andr[4].replace('\xa0','')
    anLocale = liegen.geocode(anC + co + "," + me)
    sleep(1)
    aroo = hold[5:10]
    arC = aroo[0]
    arCC = aroo[1].replace('\xa0','')
    arR = aroo[2].replace('\xa0','')
    arH = aroo[3].replace('\xa0','')
    arD = aroo[4].replace('\xa0','')
    arLocale = liegen.geocode(arC + co + "," + me)
    sleep(1)
    cumb = hold[10:15]
    cumbC = cumb[0]
    cumbCC = cumb[1].replace('\xa0','')
    cumbR = cumb[2].replace('\xa0','')
    cumbH = cumb[3].replace('\xa0','')
    cumbD = cumb[4].replace('\xa0','')
    cLocale = liegen.geocode(cumbC + co + "," + me)
    sleep(1)
    frank = hold[15:20]
    frC = frank[0]
    frCC = frank[1].replace('\xa0','')
    frR = frank[2].replace('\xa0','')
    frH = frank[3].replace('\xa0','')
    frD = frank[4].replace('\xa0','')
    fLocale = liegen.geocode(frC + co + "," + me)
    sleep(1)
    hanc = hold[20:25]
    haC = hanc[0]
    haCC = hanc[1].replace('\xa0','')
    haR = hanc[2].replace('\xa0','')
    haH = hanc[3].replace('\xa0','')
    haD = hanc[4].replace('\xa0','')
    hLocale = liegen.geocode(haC + co + "," + me)
    sleep(1)
    kenne = hold[25:30]
    keC = kenne[0]
    keCC = kenne[1].replace('\xa0','')
    keR = kenne[2].replace('\xa0','')
    keH = kenne[3].replace('\xa0','')
    keD = kenne[4].replace('\xa0','')
    keLocale = liegen.geocode(keC + co + "," + me)
    sleep(1)
    knox = hold[30:35]
    knC = knox[0]
    knCC = knox[1].replace('\xa0','')
    knR = knox[2].replace('\xa0','')
    knH = knox[3].replace('\xa0','')
    knD = knox[4].replace('\xa0','')
    knLocale = liegen.geocode(knC + co + "," + me)
    sleep(1)
    linc = hold[35:40]
    linC = linc[0]
    linCC = linc[1].replace('\xa0','')
    linR = linc[2].replace('\xa0','')
    linH = linc[3].replace('\xa0','')
    linD = linc[4].replace('\xa0','')
    lLocale = liegen.geocode(linC + co + "," + me)
    sleep(1)
    ox = hold[40:45]
    oxC = ox[0]
    oxCC = ox[1].replace('\xa0','')
    oxR = ox[2].replace('\xa0','')
    oxH = ox[3].replace('\xa0','')
    oxD = ox[4].replace('\xa0','')
    oxLocale = liegen.geocode(oxC + co + "," + me)
    sleep(1)
    peno = hold[45:50]
    penC = peno[0]
    penCC = peno[1].replace('\xa0','')
    penR = peno[2].replace('\xa0','')
    penH = peno[3].replace('\xa0','')
    penD = peno[4].replace('\xa0','')
    peLocale = liegen.geocode(penC + co + "," + me)
    sleep(1)
    pisca = hold[50:55]
    piC = pisca[0]
    piCC = pisca[1].replace('\xa0','')
    piR = pisca[2].replace('\xa0','')
    piH = pisca[3].replace('\xa0','')
    piD = pisca[4].replace('\xa0','')
    piLocale = liegen.geocode(piC + co + "," + me)
    sleep(1)
    saga = hold[55:60]
    sC = saga[0]
    sCC = saga[1].replace('\xa0','')
    sR = saga[2].replace('\xa0','')
    sH = saga[3].replace('\xa0','')
    sD = saga[4].replace('\xa0','')
    saLocale = liegen.geocode(sC + co + "," + me)
    sleep(1)
    somer = hold[60:65]
    soC = somer[0]
    soCC = somer[1].replace('\xa0','')
    soR = somer[2].replace('\xa0','')
    soH = somer[3].replace('\xa0','')
    soD = somer[4].replace('\xa0','')
    soLocale = liegen.geocode(soC + co + "," + me)
    sleep(1)
    waldo = hold[65:70]
    wdC = waldo[0]
    wdCC = waldo[1].replace('\xa0','')
    wdR = waldo[2].replace('\xa0','')
    wdH = waldo[3].replace('\xa0','')
    wdD = waldo[4].replace('\xa0','')
    wdLocale = liegen.geocode(wdC + co + "," + me)
    sleep(1)
    wash = hold[70:75]
    wsC = wash[0]
    wsCC = wash[1].replace('\xa0','')
    wsR = wash[2].replace('\xa0','')
    wsH = wash[3].replace('\xa0','')
    wsD = wash[4].replace('\xa0','')
    waLocale = liegen.geocode(wsC + co + "," + me)
    sleep(1)
    york = hold[75:80]
    yC = york[0]
    yCC = york[1].replace('\xa0','')
    yR = york[2].replace('\xa0','')
    yH = york[3].replace('\xa0','')
    yD = york[4].replace('\xa0','')
    yoLocale = liegen.geocode(yC + co + "," + me)
    sleep(1)
    unk = hold[80:85]
    uC = unk[0]
    uCC = unk[1].replace('\xa0','')
    uR = unk[2].replace('\xa0','')
    uH = unk[3].replace('\xa0','')
    uD = unk[4].replace('\xa0','')
    
    if anC == 'Androscoggin' and uC == 'Unknown':
       
        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(anC + "," + me + "," + str(fips.get_county_fips(anC,state=me)).strip() + "," + str(anLocale.latitude) + "," 
                   + str(anLocale.longitude) + "," + anCC + "," + anD + "," + anR + "," + "" + "," + anH +"\n")
        
        file.write(arC + "," + me + "," + str(fips.get_county_fips(arC,state=me)).strip() + "," + str(arLocale.latitude) + "," 
                   + str(arLocale.longitude) + "," + arCC + "," + arD + "," + arR + "," + "" + "," + arH +"\n")
        
        file.write(cumbC + "," + me + "," + str(fips.get_county_fips(cumbC,state=me)).strip() + "," + str(cLocale.latitude) + "," 
                   + str(cLocale.longitude) + "," + cumbCC + "," + cumbD + "," + cumbR + "," + "" + "," + cumbH +"\n")
        
        file.write(frC + "," + me + "," + str(fips.get_county_fips(frC,state=me)).strip() + "," + str(fLocale.latitude) + "," 
                   + str(fLocale.longitude) + "," + frCC + "," + frD + "," + frR + "," + "" + "," + frH +"\n")
        
        file.write(haC + "," + me + "," + str(fips.get_county_fips(haC,state=me)).strip() + "," + str(hLocale.latitude) + "," 
                   + str(hLocale.longitude) + "," + haCC + "," + haD + "," + haR + "," + "" + "," + haH +"\n")
        
        file.write(keC + "," + me + "," + str(fips.get_county_fips(keC,state=me)).strip() + "," + str(keLocale.latitude) + "," 
                   + str(keLocale.longitude) + "," + keCC + "," + keD + "," + keR + "," + "" + "," + keH +"\n")
        
        file.write(knC + "," + me + "," + str(fips.get_county_fips(knC,state=me)).strip() + "," + str(knLocale.latitude) + "," 
                   + str(knLocale.longitude) + "," + knCC + "," + knD + "," + knR + "," + "" + "," + knH +"\n")
        
        file.write(linC + "," + me + "," + str(fips.get_county_fips(linC,state=me)).strip() + "," + str(lLocale.latitude) + "," 
                   + str(lLocale.longitude) + "," + linCC + "," + linD + "," + linR + "," + "" + "," + linH +"\n")
        
        file.write(oxC + "," + me + "," + str(fips.get_county_fips(oxC,state=me)).strip() + "," + str(oxLocale.latitude) + "," 
                   + str(oxLocale.longitude) + "," + oxCC + "," + oxD + "," + oxR + "," + "" + "," + oxH +"\n")
        
        file.write(penC + "," + me + "," + str(fips.get_county_fips(penC,state=me)).strip() + "," + str(peLocale.latitude) + "," 
                   + str(peLocale.longitude) + "," + penCC + "," + penD + "," + penR + "," + "" + "," + penH +"\n")
        
        file.write(piC + "," + me + "," + str(fips.get_county_fips(piC,state=me)).strip() + "," + str(piLocale.latitude) + "," 
                   + str(piLocale.longitude) + "," + piCC + "," + piD + "," + piR + "," + "" + "," + piH +"\n")
        
        file.write(sC + "," + me + "," + str(fips.get_county_fips(sC,state=me)).strip() + "," + str(saLocale.latitude) + "," 
                   + str(saLocale.longitude) + "," + sCC + "," + sD + "," + sR + "," + "" + "," + sH +"\n")
        
        file.write(soC + "," + me + "," + str(fips.get_county_fips(soC,state=me)).strip() + "," + str(soLocale.latitude) + "," 
                   + str(soLocale.longitude) + "," + soCC + "," + soD + "," + soR + "," + "" + "," + soH +"\n")
        
        file.write(wdC + "," + me + "," + str(fips.get_county_fips(wdC,state=me)).strip() + "," + str(wdLocale.latitude) + "," 
                   + str(wdLocale.longitude) + "," + wdCC + "," + wdD + "," + wdR + "," + "" + "," + wdH +"\n")
        
        file.write(wsC + "," + me + "," + str(fips.get_county_fips(wsC,state=me)).strip() + "," + str(waLocale.latitude) + "," 
                   + str(waLocale.longitude) + "," + wsCC + "," + wsD + "," + wsR + "," + "" + "," + wsH +"\n")
    
        file.write(yC + "," + me + "," + str(fips.get_county_fips(yC,state=me)).strip() + "," + str(yoLocale.latitude) + "," 
                   + str(yoLocale.longitude) + "," + yCC + "," + yD + "," + yR + "," + "" + "," + yH +"\n")
        
        file.write(uC + "," + me + "," + str(fips.get_state_fips(me)).strip() + "," + str(liegen.geocode(me).latitude) 
                   + "," + str(liegen.geocode(me).longitude) + "," + uCC + "," + uD + "," + uR + "," + "" + "," + uH +"\n")
        
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
    
    alcona = site_parse.find("div", {"class": "fullContent"}).findAll("th")[0].text
    alNo = site_parse.find("div", {"class": "fullContent"}).findAll("th")[1].text
    alMort = site_parse.find("div", {"class": "fullContent"}).findAll("th")[2].text.replace('\xa0','0')
    
    csvfile = "COVID-19_cases_midoh.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    if (tags[0].find('td').text.strip()) == 'Alcona' and (tags[82].find('td').text.strip()) == 'Out of State':

        file = open(csvfile, "w")
        file.write(headers)
        
        #Alcona
#        file.write(alcona + "," + mi + "," + str(fips.get_county_fips(alcona, state=mi)).strip() + ","
#                       + str(geocoder.opencage(alcona + co + "," + mi, key='').latlng).strip('[]') 
#                       + "," + alNo + "," + alMort + "\n")
        
        for tag in tags[0:19]:
            pull = tag.findAll('td')
            file.write(pull[0].text + "," + mi + "," + str(fips.get_county_fips(pull[0].text,state=mi)).strip() + ","
                       + str(geocoder.opencage(pull[0].text + co + "," + mi, key='').latlng).strip('[]') 
                       + "," + pull[1].text.replace('\xa0','0') + "," + pull[2].text.replace('\xa0','0') + "\n")
            
        for tag in tags[20:72]:
            pull = tag.findAll('td')
            file.write(pull[0].text + "," + mi + "," + str(fips.get_county_fips(pull[0].text,state=mi)).strip() + ","
                       + str(geocoder.opencage(pull[0].text + co + "," + mi, key='').latlng).strip('[]') 
                       + "," + pull[1].text.replace('\xa0','0') + "," + pull[2].text.replace('\xa0','0') + "\n")
        
        #St.Clair
        file.write(tags[72].findAll('td')[0].text + "," + mi + "," + "26147" + ","
                       + str(geocoder.opencage(tags[72].findAll('td')[0].text + co + "," + mi, key='').latlng).strip('[]') 
                       + "," + tags[72].findAll('td')[1].text.replace('\xa0','0') + "," + tags[72].findAll('td')[1].text.replace('\xa0','0') + "\n")
        #St.Joseph
        file.write(tags[73].findAll('td')[0].text + "," + mi + "," + "26149" + ","
                       + str(geocoder.opencage(tags[73].findAll('td')[0].text + co + "," + mi, key='').latlng).strip('[]') 
                       + "," + tags[73].findAll('td')[1].text.replace('\xa0','0') + "," + tags[73].findAll('td')[1].text.replace('\xa0','0') + "\n")
        
        for tag in tags[74:77]:
            pull = tag.findAll('td')
            file.write(pull[0].text + "," + mi + "," + str(fips.get_county_fips(pull[0].text,state=mi)).strip() + ","
                       + str(geocoder.opencage(pull[0].text + co + "," + mi, key='').latlng).strip('[]') 
                       + "," + pull[1].text.replace('\xa0','0') + "," + pull[2].text.replace('\xa0','0') + "\n")
        
        #Detroit City merged into Wayne county data
        file.write(tags[77].findAll('td')[0].text + "," + mi + "," + str(fips.get_county_fips(tags[77].findAll('td')[0].text,state=mi)).strip() + ","
                       + str(geocoder.opencage(tags[77].findAll('td')[0].text + co + "," + mi, key='').latlng).strip('[]')
                       + "," + str((int(tags[18].findAll('td')[1].text)) + (int(tags[76].findAll('td')[1].text))) + ","
                       + str((int(tags[19].findAll('td')[2].text)) + (int(tags[77].findAll('td')[2].text))) + "\n")
        
        file.write(tags[78].findAll('td')[0].text + "," + mi + "," + str(fips.get_county_fips(tags[78].findAll('td')[0].text,state=mi)).strip() + ","
                       + str(geocoder.opencage(tags[78].findAll('td')[0].text + co + "," + mi, key='').latlng).strip('[]') 
                       + "," + tags[78].findAll('td')[1].text.replace('\xa0','0') + "," + tags[78].findAll('td')[1].text.replace('\xa0','0') + "\n")
        
        file.write("MI Department of Corrections" + "," + mi + "," + str(fips.get_state_fips(mi)).strip() + "," + str(liegen.geocode(mi).latitude) + "," 
                   + str(liegen.geocode(mi).longitude) + "," + tags[79].findAll('td')[1].text.strip() + "," 
                   + tags[79].findAll('td')[2].text.strip() + "\n")
        sleep(1)
        file.write("Federal Correctional Institute" + "," + mi + "," + str(fips.get_state_fips(mi)).strip() + "," + str(liegen.geocode(mi).latitude) + "," 
                   + str(liegen.geocode(mi).longitude) + "," + tags[80].findAll('td')[1].text.strip() + "," 
                   + tags[80].findAll('td')[2].text.strip() + "\n")
        sleep(1)
        file.write(tags[81].find('td').text.strip() + "," + mi + "," + str(fips.get_state_fips(mi)).strip() + "," + str(liegen.geocode(mi).latitude) + "," 
                   + str(liegen.geocode(mi).longitude) + "," + tags[81].findAll('td')[1].text.strip() + "," 
                   + tags[81].findAll('td')[2].text.strip() + "\n")
        sleep(1)
        file.write(tags[82].find('td').text.strip() + "," + mi + "," + str(fips.get_state_fips(mi)).strip() + "," + str(liegen.geocode(mi).latitude) + "," 
                   + str(liegen.geocode(mi).longitude) + "," + tags[82].findAll('td')[1].text.strip() + "," 
                   + tags[82].findAll('td')[2].text.strip() + "\n")
        
        file.close()
    
        print("Michigan scraper is complete.")
    else:
        print("ERROR: Must fix Michigan scraper.")

def mnScrape():
    
    mnDOH = 'https://www.health.state.mn.us/diseases/coronavirus/situation.html'

    mnClient = req(mnDOH)
    
    site_parse = soup(mnClient.read(), "lxml")
    mnClient.close()
    
    tables = site_parse.find("div", {"class": "clearfix"}).findAll("tbody")[9]

    tags = tables.findAll('td')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    mn = "MINNESOTA"
    co = ' County'
    
    csvfile = "COVID-19_cases_mndoh.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for td in tags:
        take = td.get_text()
        hold.append(take)
        
    if hold[0] == 'Aitkin' and hold[231] == 'Yellow Medicine':    
        
        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(hold[0] + "," + mn + "," + str(fips.get_county_fips(hold[0],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[0] + co + "," + mn, key='').latlng).strip('[]') + "," 
                   + hold[1].replace(',','') + "," + hold[2].replace(',','') + "\n")
        #sleep(1)
        file.write(hold[3] + "," + mn + "," + str(fips.get_county_fips(hold[3],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[3] + co + "," + mn, key='').latlng).strip('[]') + "," 
                   + hold[4].replace(',','') + "," + hold[5].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[6] + "," + mn + "," + str(fips.get_county_fips(hold[6],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[6] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[7].replace(',','') 
                   + "," + hold[8].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[9] + "," + mn + "," + str(fips.get_county_fips(hold[9],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[9] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[10].replace(',','') 
                   + "," + hold[11].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[12] + "," + mn + "," + str(fips.get_county_fips(hold[12],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[12] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[13].replace(',','') 
                   + "," + hold[14].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[15] + "," + mn + "," + str(fips.get_county_fips(hold[15],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[15] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[16].replace(',','') 
                   + "," + hold[17].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[18] + "," + mn + "," + str(fips.get_county_fips(hold[18],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[18] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[19].replace(',','') 
                   + "," + hold[20].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[21] + "," + mn + "," + str(fips.get_county_fips(hold[21],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[21] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[22].replace(',','') 
                   + "," + hold[23].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[24] + "," + mn + ","  + str(fips.get_county_fips(hold[24],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[24] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[25].replace(',','') 
                   + "," + hold[26].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[27] + "," + mn + "," + str(fips.get_county_fips(hold[27],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[27] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[28].replace(',','') 
                   + "," + hold[29].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[30] + "," + mn + "," + str(fips.get_county_fips(hold[30],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[30] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[31].replace(',','') 
                   + "," + hold[32].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[33] + "," + mn + "," + str(fips.get_county_fips(hold[33],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[33] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[34].replace(',','') 
                   + "," + hold[35].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[36] + "," + mn + ","  + str(fips.get_county_fips(hold[36],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[36] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[37].replace(',','') 
                   + "," + hold[38].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[39] + "," + mn + "," + str(fips.get_county_fips(hold[39],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[39] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[40].replace(',','') 
                   + "," + hold[41].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[42] + "," + mn + "," + str(fips.get_county_fips(hold[42],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[42] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[43].replace(',','') 
                   + "," + hold[44].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[45] + "," + mn + ","  + str(fips.get_county_fips(hold[45],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[45] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[46].replace(',','') 
                   + "," + hold[47].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[48] + "," + mn + "," + str(fips.get_county_fips(hold[48],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[48] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[49].replace(',','') 
                   + "," + hold[50].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[51] + "," + mn + "," + str(fips.get_county_fips(hold[51],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[51] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[52].replace(',','') 
                   + "," + hold[53].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[54] + "," + mn + ","  + str(fips.get_county_fips(hold[54],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[54] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[55].replace(',','') 
                   + "," + hold[56].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[57] + "," + mn + ","  + str(fips.get_county_fips(hold[57],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[57] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[58].replace(',','') 
                   + "," + hold[59].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[60] + "," + mn + "," + str(fips.get_county_fips(hold[60],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[60] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[61].replace(',','') 
                   + "," + hold[62].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[63] + "," + mn + "," + str(fips.get_county_fips(hold[63],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[63] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[64].replace(',','') 
                   + "," + hold[65].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[66] + "," + mn + "," + str(fips.get_county_fips(hold[66],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[66] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[67].replace(',','') 
                   + "," + hold[68] +"\n")
        #sleep(1)
        file.write(hold[69] + "," + mn + ","  + str(fips.get_county_fips(hold[69],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[69] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[70].replace(',','') 
                   + "," + hold[71].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[72] + "," + mn + "," + str(fips.get_county_fips(hold[72],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[72] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[73].replace(',','') 
                   + "," + hold[74].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[75] + "," + mn + ","  + str(fips.get_county_fips(hold[75],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[75] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[76].replace(',','') 
                   + "," + hold[77].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[78] + "," + mn + "," + str(fips.get_county_fips(hold[78],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[78] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[79].replace(',','') 
                   + "," + hold[80].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[81] + "," + mn + ","  + str(fips.get_county_fips(hold[81],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[81] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[82].replace(',','') 
                   + "," + hold[83].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[84] + "," + mn + "," + str(fips.get_county_fips(hold[84],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[84] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[85].replace(',','') 
                   + "," + hold[86].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[87] + "," + mn + "," + str(fips.get_county_fips(hold[87],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[87] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[88].replace(',','') 
                   + "," + hold[89].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[90] + "," + mn + "," + str(fips.get_county_fips(hold[90],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[90] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[91].replace(',','') 
                   + "," + hold[92].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[93] + "," + mn + "," + str(fips.get_county_fips(hold[93],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[93] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[94].replace(',','') 
                   + "," + hold[95].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[96] + "," + mn + ","  + str(fips.get_county_fips(hold[96],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[96] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[97].replace(',','') 
                   + "," + hold[98].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[99] + "," + mn + "," + str(fips.get_county_fips(hold[99],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[99] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[100].replace(',','') 
                   + "," + hold[101].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[102] + "," + mn + "," + str(fips.get_county_fips(hold[102],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[102] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[103].replace(',','') 
                   + "," + hold[104].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[105] + "," + mn + "," + str(fips.get_county_fips(hold[105],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[105] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[106].replace(',','') 
                   + "," + hold[107].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[108] + "," + mn + "," + str(fips.get_county_fips(hold[108],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[108] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[109].replace(',','') 
                   + "," + hold[110].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[111] + "," + mn + ","  + str(fips.get_county_fips(hold[111],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[111] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[112].replace(',','') 
                   + "," + hold[113].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[114] + "," + mn + ","  + str(fips.get_county_fips(hold[114],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[114] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[115].replace(',','') 
                   + "," + hold[116].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[117] + "," + mn + ","  + str(fips.get_county_fips(hold[117],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[117] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[118].replace(',','') 
                   + "," + hold[119].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[120] + "," + mn + "," + str(fips.get_county_fips(hold[120],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[120] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[121].replace(',','') 
                   + "," + hold[122].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[123] + "," + mn + "," + str(fips.get_county_fips(hold[123],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[123] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[124].replace(',','') 
                   + "," + hold[125].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[126] + "," + mn + ","  + str(fips.get_county_fips(hold[126],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[126] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[127].replace(',','') 
                   + "," + hold[128].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[129] + "," + mn + "," + str(fips.get_county_fips(hold[129],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[129] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[130].replace(',','') 
                   + "," + hold[131].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[132] + "," + mn + ","  + str(fips.get_county_fips(hold[132],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[132] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[133].replace(',','') 
                   + "," + hold[134].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[135] + "," + mn + "," + str(fips.get_county_fips(hold[135],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[135] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[136].replace(',','') 
                   + "," + hold[137].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[138] + "," + mn + ","  + str(fips.get_county_fips(hold[138],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[138] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[139].replace(',','') 
                   + "," + hold[140].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[141] + "," + mn + ","  + str(fips.get_county_fips(hold[141],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[141] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[142].replace(',','') 
                   + "," + hold[143].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[144] + "," + mn + ","  + str(fips.get_county_fips(hold[144],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[144] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[145].replace(',','') 
                   + "," + hold[146].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[147] + "," + mn + ","  + str(fips.get_county_fips(hold[147],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[147] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[148].replace(',','') 
                   + "," + hold[149].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[150] + "," + mn + ","  + str(fips.get_county_fips(hold[150],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[150] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[151].replace(',','') 
                   + "," + hold[152].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[153] + "," + mn + ","  + str(fips.get_county_fips(hold[153],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[153] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[154].replace(',','') 
                   + "," + hold[155].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[156] + "," + mn + "," + str(fips.get_county_fips(hold[156],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[156] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[157].replace(',','') 
                   + "," + hold[158].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[159] + "," + mn + ","  + str(fips.get_county_fips(hold[159],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[159] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[160].replace(',','') 
                   + "," + hold[161].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[162] + "," + mn + ","  + str(fips.get_county_fips(hold[162],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[162] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[163].replace(',','') 
                   + "," + hold[164].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[165] + "," + mn + ","  + str(fips.get_county_fips(hold[165],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[165] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[166].replace(',','') 
                   + "," + hold[167].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[168] + "," + mn + "," + str(fips.get_county_fips(hold[168],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[168] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[169].replace(',','') 
                   + "," + hold[170].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[171] + "," + mn + "," + str(fips.get_county_fips(hold[171],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[171] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[172].replace(',','') 
                   + "," + hold[173].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[174] + "," + mn + "," + str(fips.get_county_fips(hold[174],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[174] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[175].replace(',','') 
                   + "," + hold[176].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[177] + "," + mn + "," + str(fips.get_county_fips(hold[177],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[177] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[178].replace(',','') 
                   + "," + hold[179].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[180] + "," + mn + "," + str(fips.get_county_fips(hold[180],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[180] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[181].replace(',','') 
                   + "," + hold[182].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[183] + "," + mn + ","  + str(fips.get_county_fips(hold[183],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[183] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[184].replace(',','') 
                   + "," + hold[185].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[186] + "," + mn + ","  + str(fips.get_county_fips(hold[186],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[186] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[187].replace(',','') 
                   + "," + hold[188].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[189] + "," + mn + "," + str(fips.get_county_fips(hold[189],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[189] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[190].replace(',','') 
                   + "," + hold[191].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[192] + "," + mn + ","  + str(fips.get_county_fips(hold[192],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[192] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[193].replace(',','') 
                   + "," + hold[194].replace(',','') +"\n")
        #sleep(1)
        file.write(hold[195] + "," + mn + ","  + str(fips.get_county_fips(hold[195],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[195] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[196].replace(',','') 
                   + "," + hold[197].replace(',','') +"\n")
        file.write(hold[198] + "," + mn + ","  + str(fips.get_county_fips(hold[198],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[198] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[199].replace(',','') 
                   + "," + hold[200].replace(',','') +"\n")
        file.write(hold[201] + "," + mn + ","  + str(fips.get_county_fips(hold[201],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[201] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[202].replace(',','') 
                   + "," + hold[203].replace(',','') +"\n")
        file.write(hold[204] + "," + mn + ","  + str(fips.get_county_fips(hold[204],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[204] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[205].replace(',','') 
                   + "," + hold[206].replace(',','') +"\n")
        file.write(hold[207] + "," + mn + ","  + str(fips.get_county_fips(hold[207],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[207] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[208].replace(',','') 
                   + "," + hold[209].replace(',','') +"\n")
        file.write(hold[210] + "," + mn + ","  + str(fips.get_county_fips(hold[210],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[210] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[211].replace(',','') 
                   + "," + hold[212].replace(',','') +"\n")
        file.write(hold[213] + "," + mn + ","  + str(fips.get_county_fips(hold[213],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[213] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[214].replace(',','') 
                   + "," + hold[215].replace(',','') +"\n")
        file.write(hold[216] + "," + mn + ","  + str(fips.get_county_fips(hold[216],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[216] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[217].replace(',','') 
                   + "," + hold[218].replace(',','') +"\n")
        file.write(hold[219] + "," + mn + ","  + str(fips.get_county_fips(hold[219],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[219] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[220].replace(',','') 
                   + "," + hold[221].replace(',','') +"\n")
        file.write(hold[222] + "," + mn + ","  + str(fips.get_county_fips(hold[222],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[222] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[223].replace(',','') 
                   + "," + hold[224].replace(',','') +"\n")
        file.write(hold[225] + "," + mn + ","  + str(fips.get_county_fips(hold[225],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[225] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[226].replace(',','') 
                   + "," + hold[227].replace(',','') +"\n")
        file.write(hold[228] + "," + mn + ","  + str(fips.get_county_fips(hold[228],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[228] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[229].replace(',','') 
                   + "," + hold[230].replace(',','') +"\n")
        file.write(hold[231] + "," + mn + ","  + str(fips.get_county_fips(hold[231],state=mn)).strip() + ","
                   + str(geocoder.opencage(hold[231] + co + "," + mn, key='').latlng).strip('[]') + "," + hold[232].replace(',','') 
                   + "," + hold[233].replace(',','') +"\n")
        
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

    mo = "MISSOURI"
    co = ' County'
    
    csvfile = "COVID-19_cases_modoh.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    if (tables[1].find('td').text) == 'Adair' and (tables[167].find('td').text) == 'TBD':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        #Pull from the county case table
        for t in tables[1:118]:
            pull = t.findAll('td')
            locale = geocoder.opencage(pull[0].text + co + "," + mo, key='')
            file.write(pull[0].text + "," + mo + "," + str(fips.get_county_fips(pull[0].text, state=mo)).strip() + "," + str(locale.latlng).strip('[]')
                        + "," + pull[1].text + "," + "" + "\n")
            
        file.write(tables[118].findAll('td')[0].text + "," + mo + "," + str(fips.get_state_fips(mo)).strip() + "," + str(geocoder.opencage(mo, key='').latlng).strip('[]')
                   + "," + tables[118].findAll('td')[1].text + "," + "" + "\n")
        
        #Pull from the county death table
        for t in tables[136:167]:
            pull = t.findAll('td')
            locale = geocoder.opencage(pull[0].text + co + "," + mo, key='')
            file.write(pull[0].text + "," + mo + "," + str(fips.get_county_fips(pull[0].text,state=mo)).strip() + "," + str(locale.latlng).strip('[]')
                       + "," + "" + "," + pull[1].text + "\n")
            
#        file.write(tables[164].findAll('td')[0].text + "," + mo + "," + str(fips.get_state_fips(mo)).strip() + "," + str(geocoder.opencage(mo, key='').latlng).strip('[]')
#                   + "," + "" + "," + tables[164].findAll('td')[1].text + "\n")
        
        file.close()
    
        print("Missouri scraper is complete.")
    else:
        print("ERROR: Must fix Missouri scraper.")

def mpScrape():
    
    mpWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States'

    mpClient = req(mpWiki)
    
    site_parse = soup(mpClient.read(), "lxml")
    mpClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_mpWiki.csv"
    headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    
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
        
        file.write(hold[54].split('\n')[3] + "," + mp + "," + str(fips.get_county_fips("Rota",state=mp)).strip() + ","  + str(mpGeo.latitude) 
                   + "," + str(mpGeo.longitude) + "," + hold[54].split('\n')[5].replace(',','') 
                   + "," + hold[54].split('\n')[7].replace(',','') + "," 
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    if (tables[0].find('td').text) == 'Adams' and (tables[80].find('td').text) == 'Yazoo':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for t in tables[:81]:
            pull = t.findAll('td')
            locale = geocoder.opencage(pull[0].text + co + "," + ms, key='')
            file.write(pull[0].text + "," + ms + "," + str(fips.get_county_fips(pull[0].text, state=ms)).strip() + "," + str(locale.latlng).strip('[]') + "," 
                       + pull[1].text.replace(' ','0') + "," + pull[2].text.replace(' ','0') + "\n")
        
        file.close()
    
        print("Mississippi scraper is complete.")
    else:
        print("ERROR: Must fix Mississippi scraper.")

def mtScrape():
    
    mtDOH = 'https://dphhs.mt.gov/publichealth/cdepi/diseases/coronavirusmt/demographics'
    
    mtClient = req(mtDOH)
    
    site_parse = soup(mtClient.read(), "lxml")
    mtClient.close()
    
    tables = site_parse.find("div", {"id": "dnn_ctr93751_HtmlModule_lblContent"}).findAll("table")[1].find("tbody")
    
    tags = tables.findAll("tr")
    
    mt = "MONTANA"
    co = ' County'
    
    csvfile = "COVID-19_cases_mtdoh.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    if tags[0].find('td').text.split('\n')[0] == 'Beaverhead' and tags[29].find('td').text.split('\n')[0] == 'Total':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for t in tags[:29]:
            pull = t.findAll("td")
            locale = geocoder.opencage(pull[0].text.split('\n')[0] + co + "," + mt, key='')
            file.write(pull[0].text.split('\n')[0] + "," + mt + "," 
                       + str(fips.get_county_fips(pull[0].text.split('\n')[0], state=mt)).strip() 
                       + "," + str(locale.latlng).strip('[]') + "," 
                       + pull[1].text.split('\n')[0].replace('\xa0','0').replace(',','') 
                       + "," + pull[2].text.split('\n')[0].replace('\xa0','0').replace(',','') + "\n")
            
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    tags = tables.findAll('tr')
    
    if (tags[0].find('td').text) == 'Alamance County' and (tags[92].find('td').text) == 'Yadkin County':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for tag in tags:
            pull = tag.findAll('td')
            locale = geocoder.opencage(pull[0].text + "," + nc, key='')
            file.write(pull[0].text + "," + nc + "," + str(fips.get_county_fips(pull[0].text, state = nc)).strip()
                       + "," + str(locale.latlng).strip('[]') + "," 
                       + pull[1].text.replace(',','') + "," + pull[2].text.replace(',','') + "\n")
        
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

    nd = "NORTH DAKOTA"
    co = ' County'
    
    csvfile = "COVID-19_cases_ndWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases\n"
    
    hold = []

    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if hold[60].split('\n')[1] == 'Barnes' and hold[92].split('\n')[1] == 'Williams':

        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[60:93]:
            locale = geocoder.opencage(h.split('\n')[1] + co + "," + nd, key='')
            take = h.split('\n')
            file.write(take[1] + "," + nd + "," + str(fips.get_county_fips(take[1],state=nd)).strip() + "," + str(locale.latlng).strip('[]') + "," + take[3] + "\n")
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if (hold[61].split('\n')[1]) == 'Adams' and (hold[113].split('\n')[1]) == 'TBD':
                            
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[61:113]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + co + "," + ne, key='')
            file.write(take[1] + "," + ne + "," 
                       + str(fips.get_county_fips(take[1],state=ne)).strip() 
                       + "," + str(locale.latlng).strip('[]') + "," 
                       + take[3] + "," + take[5] + "\n")
        
        file.write(hold[113].split('\n')[1] + "," + ne + "," 
                   + str(fips.get_state_fips(ne)).strip() 
                   + "," + str(liegen.geocode(ne).latitude)
                   + "," + str(liegen.geocode(ne).longitude) + "," 
                   + hold[113].split('\n')[3] + "," + hold[113].split('\n')[5] + "\n")
        
        file.close()
    
        print("Nebraska scraper is complete.")
    else:
        print("ERROR: Must fix Nebraska scraper.")

        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases\n"
    
    tags = tables.findAll('li')

    if (tags[0].get_text().split(' ')[0]) == 'Belknap' and (tags[11].get_text().split(' ')[0]) == 'Sullivan':

        file = open(csvfile, "w")
        file.write(headers)
            
        for t in range(0,5):
            locale = liegen.geocode(tags[t].get_text().split(' ')[0] + "," + nh)
            catch_TimeOut(tags[t].get_text().split(' ')[0])
            file.write(tags[t].get_text().split(' ')[0] + "," + nh + "," 
                       + str(fips.get_county_fips(tags[t].get_text().split(' ')[0],state=nh)).strip() + "," + str(locale.latitude) 
                       + "," + str(locale.longitude) + "," + tags[t].get_text().split(' ')[1] + "\n")
            sleep(1)
        localeH = liegen.geocode("Hillsborough, New Hampshire")
        file.write("Hillsborough" + "," + nh + "," 
                       + str(fips.get_county_fips("Hillsborough",state=nh)).strip() + "," + str(localeH.latitude) 
                       + "," + str(localeH.longitude) + "," + str(int(tags[5].get_text().split(' - ')[1].split(' ')[1]) 
                       + int(tags[6].get_text().split(' - ')[1].split(' ')[1]) 
                       + int(tags[7].get_text().split(' - ')[1].split(' ')[1])) + "\n")
        for t in range(8,len(tags)):
            locale = liegen.geocode(tags[t].get_text().split(' ')[0] + "," + nh)
            catch_TimeOut(tags[t].get_text().split(' ')[0])
            file.write(tags[t].get_text().split(' ')[0] + "," + nh + "," 
                       + str(fips.get_county_fips(tags[t].get_text().split(' ')[0],state=nh)).strip() + "," + str(locale.latitude) 
                       + "," + str(locale.longitude) + "," + tags[t].get_text().split(' ')[1] + "\n")
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
                
    if (hold[70].split('\n')[1]) == 'Atlantic' and (hold[91].split('\n')[1]) == 'Under investigation':
            
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[70:91]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + co + "," + nj, key='')
            file.write(take[1] + "," + nj + "," + str(fips.get_county_fips(take[1], state=nj)).strip() + "," + str(locale.latlng).strip('[]') + "," 
                       + take[3].replace(',','') + "," 
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        
        file.write(hold[91].split('\n')[1] + "," + nj + "," + str(fips.get_state_fips(nj)).strip() + "," + str(liegen.geocode(nj).latitude) + "," 
                   + str(liegen.geocode(nj).longitude) + "," + hold[91].split('\n')[3].replace(',','') 
                   + "," + hold[91].split('\n')[5].replace(',','') 
                   + "," + hold[91].split('\n')[7].replace(',','') + "\n")
        
        file.close()
    
        print("New Jersey scraper is complete.")
    else:
        print("ERROR: Must fix New Jersey scraper.")

    
def nmScrape():
    
    nmWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_New_Mexico'

    nmClient = req(nmWiki)
    
    site_parse = soup(nmClient.read(), "lxml")
    nmClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    nm = "NEW MEXICO"

    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)    
    
    csvfile = "COVID-19_cases_nmdoh.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    if (hold[61].split('\n')[1]) == 'Bernalillo' and (hold[87].split('\n')[1]) == 'Valencia':

        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[61:67]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + nm, key='')
            file.write(take[1] + "," + nm + "," + str(fips.get_county_fips(take[1],state=nm)).strip() + "," 
                       + str(locale.latlng).strip('[]') + "," 
                       + take[3].replace(',','') + "," 
                       + take[5].replace(',','') + "\n")
            
        file.write("Dona Ana" + "," + nm + "," + "35013" 
                   + "," + str(geocoder.opencage("Dona Ana County" + ", " + nm, key='').latlng).strip('[]') + "," 
                   + hold[67].split('\n')[3].replace(',','') + "," 
                   + hold[67].split('\n')[5].replace(',','') + "\n")
        
        for h in hold[68:88]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + nm, key='')
            file.write(take[1] + "," + nm + "," + str(fips.get_county_fips(take[1],state=nm)).strip() + "," 
                       + str(locale.latlng).strip('[]') + "," 
                       + take[3].replace(',','') + "," 
                       + take[5].replace(',','') + "\n")
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases\n"
    
    tags = tables.findAll('li')
    
    if (tags[0].get_text().split(': ')[0]) == 'Clark' and (tags[11].get_text().split(': ')[0]) == 'Lander':

        file = open(csvfile, "w")
        file.write(headers)
        
        for t in range(0,len(tags)):
            locale = liegen.geocode(tags[t].get_text().split(': ')[0] + co + "," + nv)
            catch_TimeOut(tags[t].get_text().split(': ')[0] + co + "," + nv)
            file.write(tags[t].get_text().split(': ')[0] + "," + nv + "," 
                       + str(fips.get_county_fips(tags[t].get_text().split(': ')[0],state=nv)).strip() + "," 
                       + str(locale.latitude) + "," + str(locale.longitude) + ","
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
    
    nycDF = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/boro.csv')
    nycDF.head()
    nycBo = nycDF['BOROUGH_GROUP'].tolist()
    nycCase = nycDF['COVID_CASE_COUNT'].tolist()
    brnx = nycBo[0].strip('The ')
    brnxNo = nycCase[0]
    brook = nycBo[1]
    brookNo = nycCase[1] 
    manh = nycBo[2]
    manNo = nycCase[2]
    queens = nycBo[3]
    queensNo = nycCase[3]
    staten = nycBo[4]
    statenNo = nycCase[4]
    
    csvfile = "COVID-19_cases_nydoh.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
                
    if (hold[130].split('\n')[1]) == 'Albany' and (hold[186].split('\n')[1]) == 'Yates' and staten == 'Staten Island':
                
        file = open(csvfile, "w", encoding = 'utf-8')
        file.write(headers)
        
        for h in hold[130:187]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1].split('[')[0] + co + "," + ny, key='')
            file.write(take[1].split('[')[0] + "," + ny + "," 
                       + str(fips.get_county_fips(take[1].split('[')[0],state=ny)).strip() + "," 
                       + str(locale.latlng).strip('[]') + "," 
                       + take[3].split('[')[0].replace(',','') + "," + take[5].replace(',','')
                       + "," + take[7].replace(',','') + "\n")
            
        bronx = liegen.geocode(brnx + "," + ny)
        file.write(brnx + "," + ny + "," + str(fips.get_county_fips(brnx,state=ny)).strip() + "," + str(bronx.latitude)
                   + "," + str(bronx.longitude) + "," + str(brnxNo) + "," + ""  + "," + ""  + "\n")    
        
        brooklyn = liegen.geocode(brook + "," + ny)
        file.write(brook + "," + ny + "," + str(fips.get_county_fips(brook,state=ny)).strip() + "," + str(brooklyn.latitude)
                   + "," + str(brooklyn.longitude) + "," + str(brookNo) + "," + ""  + "," + ""  + "\n")    
        
        hattan = liegen.geocode(manh + "," + ny)
        file.write(manh + "," + ny + "," + str(fips.get_county_fips(manh,state=ny)).strip() + "," + str(hattan.latitude)
                   + "," + str(hattan.longitude) + "," + str(manNo) + "," + ""  + "," + ""  + "\n")  
        
        queen = liegen.geocode(queens + "," + ny)
        file.write(queens + "," + ny + "," + str(fips.get_county_fips(queens,state=ny)).strip() + "," + str(queen.latitude)
                   + "," + str(queen.longitude) + "," + str(queensNo) + "," + ""  + "," + ""  + "\n")
        
        island = liegen.geocode(staten + "," + ny)
        file.write(staten + "," + ny + "," + str(fips.get_county_fips(staten,state=ny)).strip() + "," + str(island.latitude)
                   + "," + str(island.longitude) + "," + str(statenNo) + "," + ""  + "," + ""  + "\n")
        
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
    
    oh = "OHIO"
    co = ' County'
    
    csvfile = "COVID-19_cases_ohWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    if (hold[64].split('\n')[1]) == 'Adams' and (hold[151].split('\n')[1]) == 'Wyandot':
                
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[64:152]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + co + "," + oh, key='')
            file.write(take[1].split('[')[0] + "," + oh + "," + str(fips.get_county_fips(take[1],state=oh)).strip() + "," 
                       + str(locale.latlng).strip('[]') + "," 
                       + take[3].replace(',','') + "," + take[5].replace(',','') + "\n")
        
        file.close()
    
        print("Ohio scraper is complete.")
    else:
        print("ERROR: Must fix Ohio scraper.")

def okScrape():
    
    testUrl = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'
    testClient = req(testUrl)
    
    site_parse = soup(testClient.read(), 'lxml')
    testClient.close()
    
    tables = site_parse.find("div", {"class": "Box mb-3 Box--condensed"})
    
    tags = tables.find('tbody')
    
    att = tags.findAll('tr', {"class":"js-navigation-item"})[-2]
    
    current = att.find('a').text
    
    git = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
           
    newUrl = git + current
    
    df = pd.read_csv(newUrl)
        
    okDF = df.groupby('Province_State').get_group('Oklahoma')
    okie = okDF[okDF.Admin2 != 'Unassigned']
    hold = okie.reindex(columns = ['Admin2', 'Province_State', 'FIPS', 'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered'])
    newHold = hold.rename(columns = {'Admin2' : 'County', 'Province_State' : 'State', 'FIPS' : 'fips', 'Lat' : 'Latitude', 'Long_' : 'Longitude', 'Confirmed'  :'Confirmed Cases', 'Recovered':'Recoveries'})
    newHold = newHold.fillna(0)
    newHold = newHold.astype({'fips':'int64'})
    
    newHold.to_csv('COVID-19_cases_okdoh.csv',index=False, header=True)
    
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    if (tags[0].find('td').text) == 'Baker' and (tags[36].find('td').text) == 'Total':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for tag in tags[:36]:
            pull = tag.findAll('td')
            locale = geocoder.opencage(pull[0].text.strip() + co + "," + orG, key='')
            file.write(pull[0].text.strip() + "," + orG + "," + str(fips.get_county_fips(pull[0].text,state=orG)).strip() + "," 
                       + str(locale.latlng).strip('[]') + ","
                       + pull[1].text + "," + pull[2].text + "\n")
        
        file.close()
    
        print("Oregon scraper is complete.")
    else:
        print("ERROR: Must fix Oregon scraper.")

def paScrape():
    
    paDOH = 'https://www.health.pa.gov/topics/disease/coronavirus/Pages/Cases.aspx'

    paClient = req(paDOH)
    
    site_parse = soup(paClient.read(), "lxml")
    paClient.close()
    
    tables = site_parse.find("div", {"class": "ms-rtestate-field","style": "display:inline"}).find("div", {"style": "text-align:center;"}).find("table", {"class": "ms-rteTable-default"})
    
    tags = tables.findAll('tr')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    pa = "PENNSYLVANIA"
    co = ' County'
    
    csvfile = "COVID-19_cases_padoh.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    if (tags[1].find('td').text) == 'Adams' and (tags[67].find('td').text.strip()) == 'York':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for tag in tags[1:]:
            pull = tag.findAll('td')
            locale = geocoder.opencage(pull[0].text.strip() + co + "," + pa, key='')
            file.write(pull[0].text.strip() + "," + pa + "," + str(fips.get_county_fips(pull[0].text.strip(),state=pa)).strip() + "," 
                       + str(locale.latlng).strip('[]') + "," 
                       + pull[1].text + "," + pull[3].text + "\n")
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if (hold[59].split('\n')[1]) == 'Arecibo' and (hold[67].split('\n')[1].split(' [')[0]) == 'Not available':
                
        file = open(csvfile, "w")
        file.write(headers)
                    
        aLocale = liegen.geocode(hold[59].split('\n')[1] + ", PR")
        file.write(hold[59].split('\n')[1] + "," + pr + "," 
                   + str(fips.get_county_fips(hold[59].split('\n')[1],state=pr)).strip() + "," + str(aLocale.latitude)
                   + "," + str(aLocale.longitude) + "," + hold[59].split('\n')[5] + "\n")
        sleep(1)
        bLocale = liegen.geocode(hold[60].split('\n')[1] + ", PR")
        file.write(hold[60].split('\n')[1] + "," + pr + "," 
                   + str(fips.get_county_fips(hold[60].split('\n')[1],state=pr)).strip() + "," + str(bLocale.latitude)
                   + "," + str(bLocale.longitude) + "," + hold[60].split('\n')[5] + "\n")
        sleep(1)
        cLocale = liegen.geocode(hold[61].split('\n')[1] + ", PR")
        file.write(hold[61].split('\n')[1] + "," + pr + "," + str(fips.get_county_fips(hold[61].split('\n')[1],state=pr)).strip() + "," 
                   + str(cLocale.latitude) + "," 
                   + str(cLocale.longitude) + "," + hold[61].split('\n')[5] + "\n")
        sleep(1)
        fLocale = liegen.geocode(hold[62].split('\n')[1] + ", PR")
        file.write(hold[62].split('\n')[1] + "," + pr + "," + str(fips.get_county_fips(hold[62].split('\n')[1],state=pr)).strip() + "," 
                   + str(fLocale.latitude) + "," 
                   + str(fLocale.longitude) + "," + hold[62].split('\n')[5] + "\n")
        sleep(1)
        maLocale = liegen.geocode(hold[63].split('\n')[1] + ", PR")
        file.write(hold[63].split('\n')[1] + "," + pr + "," + "72097" + ","
                   + str(maLocale.latitude) + "," 
                   + str(maLocale.longitude) + "," + hold[63].split('\n')[5] + "\n")
        sleep(1)
        meLocale = liegen.geocode("Canovanas, PR")
        file.write(hold[64].split('\n')[1].split(' (')[0] + "," + pr + "," + str(fips.get_county_fips("Canovanas",state=pr)).strip() + "," 
                   + str(meLocale.latitude) + "," 
                   + str(meLocale.longitude) + "," + hold[64].split('\n')[5] + "\n")
        sleep(1)
        pLocale = liegen.geocode(hold[65].split('\n')[1] + ", PR")
        file.write(hold[65].split('\n')[1] + "," + pr + "," + str(fips.get_county_fips(hold[65].split('\n')[1],state=pr)).strip() + "," 
                   + str(pLocale.latitude) + "," 
                   + str(pLocale.longitude) + "," + hold[65].split('\n')[5] + "\n")
        sleep(1)
        file.write(hold[66].split('\n')[1] + "," + pr + "," + str(fips.get_state_fips(pr)).strip() + "," + ""
                   + "," + "" + "," + hold[66].split('\n')[5] + "\n")
        file.write(hold[67].split('\n')[1].split(' [')[0] + "," + pr + "," 
                   + str(fips.get_state_fips(pr)).strip() + "," 
                   + str(liegen.geocode(pr).latitude)
                   + "," + str(liegen.geocode(pr).longitude) + "," + hold[67].split('\n')[5] + "\n")
        
        file.close()
        print("Puerto Rico scraper is complete.")
    else:
        print("ERROR: Must fix Puerto Rico scraper.")
    
def riScrape():
    
    riDOH = 'https://www.nytimes.com/interactive/2020/us/rhode-island-coronavirus-cases.html'

    riClient = req(riDOH)
    
    site_parse = soup(riClient.read(), "lxml")
    riClient.close()
    
    tables = site_parse.findAll("div", {"class": "g-svelte"})[9]
    
    tags = tables.findAll('td')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    ri = "RHODE ISLAND"
    co = ' County'
    
    csvfile = "COVID-19_cases_riNews.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tags[6:]:
        take = t.text.split('\n')[1].strip()
        hold.append(take)
        
    prov = hold[0]
    provL = liegen.geocode(prov + co + "," + ri)
    sleep(1)
    provC = hold[1].replace(',','').replace('—','0')
    provD = hold[3].replace(',','').replace('—','0') 
    kent = hold[12]
    kentL = liegen.geocode(kent + co + "," + ri)
    sleep(1)
    kentC = hold[13].replace(',','').replace('—','0')
    kentD = hold[15].replace(',','').replace('—','0')
    wash = hold[18]
    washL = liegen.geocode(wash + co + "," + ri)
    sleep(1)
    washC = hold[19].replace(',','').replace('—','0')
    washD = hold[21].replace(',','').replace('—','0')
    new = hold[24]
    newL = liegen.geocode(new + co + "," + ri)
    sleep(1)
    newC = hold[25].replace(',','').replace('—','0')
    newD = hold[27].replace(',','').replace('—','0')
    brist = hold[30]
    bristL = liegen.geocode(brist + co + "," + ri)
    sleep(1)
    bristC = hold[31].replace(',','').replace('—','0')
    bristD = hold[33].replace(',','').replace('—','0')
    unkn = hold[6]
    unkC = hold[7].replace(',','').replace('—','0')
    unkD = hold[9].replace(',','').replace('—','0')

    if prov == "Providence" and unkn == "Unknown":
  
        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(prov + "," + ri + "," + str(fips.get_county_fips(prov,state=ri)).strip() 
                   + "," + str(provL.latitude) + "," 
                   + str(provL.longitude) + "," + provC + "," + provD + "\n")
        
        file.write(kent + "," + ri + "," + str(fips.get_county_fips(kent,state=ri)).strip()
                   + "," + str(kentL.latitude) + "," 
                   + str(kentL.longitude) + "," + kentC + "," + kentD + "\n")
        
        file.write(wash + "," + ri + "," + str(fips.get_county_fips(wash,state=ri)).strip() 
                   + "," + str(washL.latitude) + "," 
                   + str(washL.longitude) + "," + washC + "," + washD + "\n")
        
        file.write(new + "," + ri + "," + str(fips.get_county_fips(new,state=ri)).strip() 
                   + "," + str(newL.latitude) + "," 
                   + str(newL.longitude) + "," + newC + "," + newD + "\n")
        
        file.write(brist + "," + ri + "," + str(fips.get_county_fips(brist,state=ri)).strip() 
                   + "," + str(bristL.latitude) + "," 
                   + str(bristL.longitude) + "," + bristC + "," + bristD + "\n")
        
        file.write(unkn + "," + ri + "," + str(fips.get_state_fips(ri)).strip() +"," 
                   + "" + "," + "" + "," + unkC + "," + unkD + "\n")
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
                
    if (hold[63].split('\n')[1]) == 'Abbeville' and (hold[108].split('\n')[1]) == 'York':
                
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[63:109]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + co + "," + sc, key='')
            file.write(take[1] + "," + sc + "," + str(fips.get_county_fips(take[1],state=sc)).strip() 
                       + "," + str(locale.latlng).strip('[]') + "," 
                       + take[3] + "," + take[5] + "\n")
        
        file.close()
    
        print("South Carolina scraper is complete.")
    else:
        print("ERROR: Must fix South Carolina scraper.")

def sdScrape():
    
    sdWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_South_Dakota'

    sdClient = req(sdWiki)
    
    site_parse = soup(sdClient.read(), "lxml")
    sdClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
    sd = "SOUTH DAKOTA"
    co = ' County'
    
    csvfile = "COVID-19_cases_sdWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    
    hold = []
    
    for t in tables:
        pull = t.findAll('tr')
        for p in pull:
            take = p.get_text()
            hold.append(take)
                
    if (hold[56].split('\n')[1]) == 'Aurora' and (hold[97].split('\n')[1]) == 'Yankton':
                
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[56:98]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + co + "," + sd, key='')
            file.write(take[1] + "," + sd + "," + str(fips.get_county_fips(take[1],state=sd)).strip() 
                       + "," + str(locale.latlng).strip('[]') + "," 
                       + take[3].replace(',','') + "," + take[7].replace(',','') + "," + take[5].replace(',','') + "\n")
        
        file.close()

    
        print("South Dakota scraper is complete.")
    else:
        print("ERROR: Must fix South Dakota scraper.")
    
def tnScrape():
    
    tnWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Tennessee'
    
    tnClient = req(tnWiki)
    
    site_parse = soup(tnClient.read(), "lxml")
    tnClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    csvfile = "COVID-19_cases_tnWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries\n"
    tn = "TENNESSEE"
    co = ' County'
    
    hold = []
        
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)    
                
    if (hold[164].split('\n')[1]) == 'Anderson' and (hold[256].split('\n')[1]) == 'Pending':
        
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[164:255]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1].split('[')[0] + co + "," + tn, key='')
            file.write(take[1].split('[')[0] + "," + tn + "," + str(fips.get_county_fips(take[1].split('[')[0],state=tn)).strip() 
                       + "," + str(locale.latlng).strip('[]') 
                       +  "," + take[3].split('[')[0].replace(',','') + "," 
                       + take[5].split('[')[0].replace(',','') + "," + take[7].split('[')[0].replace(',','') +"\n")
        
        file.write(hold[255].split('\n')[1].split('[')[0] + "," + tn +  "," + str(fips.get_state_fips(tn)).strip() + ","  
                   + str(geocoder.opencage(tn, key='').latlng).strip('[]') 
                   +","+ hold[255].split('\n')[3] + "," + hold[255].split('\n')[5] + "," + hold[255].split('\n')[7] +"\n")
        file.write(hold[256].split('\n')[1].split('[')[0] + "," + tn +  "," + str(fips.get_state_fips(tn)).strip() + ","
                   + str(geocoder.opencage(tn, key='').latlng).strip('[]') 
                   +","+ hold[256].split('\n')[3] + "," + hold[256].split('\n')[5] + "," + hold[256].split('\n')[7] +"\n")
            
        file.close()
        
        print("Tennessee scaper is complete.")
    else:
        print("ERROR: Must fix Tennessee scraper.")
    
def txScrape():
    
    txUrl = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'
    txClient = req(txUrl)
    
    site_parse = soup(txClient.read(), 'lxml')
    txClient.close()
    
    tables = site_parse.find("div", {"class": "Box mb-3 Box--condensed"})
    
    tags = tables.find('tbody')
    
    att = tags.findAll('tr', {"class":"js-navigation-item"})[-2]
    
    current = att.find('a').text
    
    git = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
           
    newUrl = git + current
    
    txdf = pd.read_csv(newUrl)
    
    hold = []
    newHold = []
        
    txDF = txdf.groupby('Province_State').get_group('Texas')
    tex = txDF[txDF.Admin2 != 'Unassigned']
    hold = tex.reindex(columns = ['Admin2', 'Province_State', 'FIPS', 'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered'])
    newHold = hold.rename(columns = {'Admin2' : 'County', 'Province_State' : 'State', 'FIPS' : 'fips', 'Lat' : 'Latitude', 'Long_' : 'Longitude', 'Confirmed'  :'Confirmed Cases', 'Recovered':'Recoveries'})
    newHold = newHold.fillna(0)
    newHold = newHold.astype({'fips':'int64'})
    
    newHold.to_csv('COVID-19_cases_txgit.csv',index=False, header=True)

def utScrape():
    
    #Central Utah Health District broken into separate counties
    cenUT = 'https://centralutahpublichealth.org/'
    utClient = req(cenUT)
    
    site_parse = soup(utClient.read(), 'lxml')
    utClient.close()
    
    juab = site_parse.find("div", {"class":"n2-ss-layer n2-ow"}).findAll("div", {"class":"n2-ss-layer n2-ow"})[15]
    juabCo = "Juab COunty"
    juabCase = str([int(n) for n in (juab.findAll('p')[0].text.split()) if n.isdigit()][0])
    juabHosp = str([int(n) for n in (juab.findAll('p')[0].text.split()) if n.isdigit()][1])
    millard = site_parse.find("div", {"class":"n2-ss-layer n2-ow"}).findAll("div", {"class":"n2-ss-layer n2-ow"})[16]
    millCo = "Millard County"
    millCase = str([int(n) for n in (millard.findAll('p')[0].text.split()) if n.isdigit()][0])
    millHosp = str([int(n) for n in (millard.findAll('p')[0].text.split()) if n.isdigit()][1])
    piute = site_parse.find("div", {"class":"n2-ss-layer n2-ow"}).findAll("div", {"class":"n2-ss-layer n2-ow"})[24]
    piuteCo = "Piute County"
    piuteCase = str([int(n) for n in (piute.findAll('p')[0].text.split()) if n.isdigit()][0])
    piuteHosp = str([int(n) for n in (piute.findAll('p')[0].text.split()) if n.isdigit()][1])
    sanpete = site_parse.find("div", {"class":"n2-ss-layer n2-ow"}).findAll("div", {"class":"n2-ss-layer n2-ow"})[29]
    sanpeteCo = "Sanpete County"
    speteCase = str([int(n) for n in (sanpete.findAll('p')[0].text.split()) if n.isdigit()][0])
    speteHosp = str([int(n) for n in (sanpete.findAll('p')[0].text.split()) if n.isdigit()][1])
    sevier = site_parse.find("div", {"class":"n2-ss-layer n2-ow"}).findAll("div", {"class":"n2-ss-layer n2-ow"})[33]
    sevCo = "Sevier County"
    sevCase = str([int(n) for n in (sevier.findAll('p')[0].text.split()) if n.isdigit()][0])
    sevHosp = str([int(n) for n in (sevier.findAll('p')[0].text.split()) if n.isdigit()][1])
    wayne = site_parse.find("div", {"class":"n2-ss-layer n2-ow"}).findAll("div", {"class":"n2-ss-layer n2-ow"})[38]
    wayCo = "Wayne County"
    wayCase = str([int(n) for n in (wayne.findAll('p')[0].text.split()) if n.isdigit()][0])
    wayHosp = str([int(n) for n in (wayne.findAll('p')[0].text.split()) if n.isdigit()][1])
    
    #Bear River Health District broken into counties
    bearRiv = 'https://brhd.org/coronavirus/'

    utClient1 = req(bearRiv)
    
    site_parse1 = soup(utClient1.read(), 'lxml')
    utClient1.close()
    
    bearTab = site_parse1.find("div", {"class":"et_pb_row et_pb_row_3"}).findAll("div", {"class":"et_pb_text_inner"})
    
    counties = []
    for t in bearTab[1:4]:
        take = t.text
        counties.append(take)
    cases = []
    for t in bearTab[6:9]:
        take = t.text
        cases.append(take)
    khaus  = []
    for t in bearTab[11:14]:
        take = t.text
        khaus.append(take)
    mort = []
    for t in bearTab[16:19]:
        take = t.text
        mort.append(take)
    
    bearRiver = list(zip(counties, cases, khaus, mort))
    
    boxElder = bearRiver[0]
    boxCo = boxElder[0]
    boxCase = boxElder[1]
    boxKhaus = boxElder[2]
    boxMort = boxElder[3]

    cache = bearRiver[1]
    cacheCo = cache[0]
    cacheCase = cache[1]
    cacheKhaus = cache[2]
    cacheMort = cache[3]
    
    rich = bearRiver[2]
    richCo = rich[0]
    richCase = rich[1]
    richKhaus = rich[2]
    richMort = rich[3]
    
    #Davis County
    davisCounty = 'http://www.daviscountyutah.gov/health/covid-19'
    utClient2 = req(davisCounty)
    
    site_parse2 = soup(utClient2.read(), 'lxml')
    utClient2.close()
    
    davTab = site_parse2.find("section", {"class":"pv-15 stats fixed-bg default-bg hovered"})
    
    stats = davTab.findAll('span')
    davCo = "Davis County"
    davCases = stats[1].text
    davKhaus = stats[3].text
    davMort = stats[5].text
    
    #Salt lake County
    saltWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Utah'
    utClient3 = req(saltWiki)
    
    site_parse3 = soup(utClient3.read(), 'lxml')
    utClient3.close()
    
    saltTab = site_parse3.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    hold = []
    
    for t in saltTab:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    salt = hold[67].split('\n')
    saltLake = salt[1]
    saltCase = salt[3]
    saltKhaus = salt[5]
    
    #San Juan County
    sanjuan = hold[68].split('\n')
    sanJ = sanjuan[1]
    sanCases = sanjuan[3]
    sanKhaus = sanjuan[5]
    
    #Southeast Utah Health District broken into counties
    seUtah = 'https://www.seuhealth.com/covid-19'
    utClient4 = req(seUtah)
    
    site_parse4 = soup(utClient4.read(), 'lxml')
    utClient4.close()
    
    seTab = site_parse4.find("div", {"id": "comp-k8kretvw2inlineContent-gridContainer"}).findAll("div", {"data-packed":"true"})
    carbon = seTab[1].text
    carCase = seTab[2].text.strip("*")
    carRec = seTab[10].text.strip("*")
    emery = seTab[3].text
    emCase = seTab[4].text.strip("*")
    emRec = seTab[12].text.strip("*")
    grand = seTab[5].text
    grCase = seTab[6].text.strip("*")
    grRec = seTab[14].text.strip("*")
    
    #Southwest Utah Health District 
    beaver = "Beaver County"
    beavFips = "49001"
    
    garfield = "Garfield County"
    garFips = "49017"
    garCase = hold[70].split('\n')[3]
    garKhaus = hold[70].split('\n')[5]
    
    iron = "Iron County"
    ironFips = "49021"
    
    kane = "Kane County"
    kaneFips = "49025"
    
    washC = "Washington County"
    washFips = "49053"
    
    #Summit County 
    summit = hold[71].split('\n')
    sumCo = summit[1] + " County"
    sumCase = summit[3]
    sumKhaus = summit[5]
    
    #Tooele County
    tooele = hold[72].split('\n')
    toolCo = tooele[1] + " County"
    toolCase = tooele[3]
    toolKhaus = tooele[5]
    
    #TriCounty Health District broken into counties
    triUT = 'https://tricountyhealth.com/local-covid-19-situational-update/'
    utClient5 = req(triUT)
    
    site_parse5 = soup(utClient5.read(), 'lxml')
    utClient5.close()
    
    triTab = site_parse5.find("div", {"class": "et_pb_row et_pb_row_3"}).findAll("div", {"class": "et_pb_text_inner"})    
    uintah = triTab[0].text.split('\n')
    uintahCo = "Uintah County"
    uintahCase = uintah[1].split(": ")[1]
    uintahKhaus = uintah[2].split(": ")[1]
    
    duchesne = triTab[1].text.split('\n')
    duchCo = "Duchesne County"
    duchCase = duchesne[1].split(": ")[1]
    duchKhaus = duchesne[2].split(": ")[1]
    
    daggett = triTab[2].text.split('\n')
    daggCo = "Daggett County"
    daggCase = daggett[1].split(": ")[1]
    daggKhaus = daggett[2].split(": ")[1]

    #Utah County
    utah = hold[74].split('\n')
    utahCo = utah[1]
    utahCase = utah[3]
    utahKhaus = utah[5]
    
    #Wasatch County
    wasa = hold[75].split('\n')
    wasaCo = wasa[1]
    wasaCase = wasa[3]
    wasaKhaus = wasa[5]
    
    #Weber-Morgan Health District
    weber = hold[76].split('\n')
    webCo = weber[1]
    webCase = weber[3]
    webKhaus = weber[5]
    webFips = "49057"
    
    ut = "UTAH"
    
    csvfile = "COVID-19_cases_utNews.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recoveries,,Hospitalizations\n"
    
    if  boxCo == 'Box Elder' and saltLake == 'Salt Lake' and uintah[0] == 'UINTAH COUNTY':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        file.write(juabCo + "," + ut + "," + str(fips.get_county_fips(juabCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(juabCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + juabCase + "," + "" + "," + "" + "," + "" + "," + juabHosp + "\n")
        file.write(millCo + "," + ut + "," + str(fips.get_county_fips(millCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(millCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + millCase + "," + "" + "," + "" + "," + "" + "," + millHosp + "\n")
        file.write(piuteCo + "," + ut + "," + str(fips.get_county_fips(piuteCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(piuteCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + piuteCase + "," + "" + "," + "" + "," + "" + "," + piuteHosp + "\n")
        file.write(sanpeteCo + "," + ut + "," + str(fips.get_county_fips(sanpeteCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(sanpeteCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + speteCase + "," + "" + "," + "" + "," + "" + "," + speteHosp + "\n")
        file.write(sevCo + "," + ut + "," + str(fips.get_county_fips(sevCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(sevCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + sevCase + "," + "" + "," + "" + "," + "" + "," + sevHosp + "\n")
        file.write(wayCo + "," + ut + "," + str(fips.get_county_fips(wayCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(wayCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + wayCase + "," + "" + "," + "" + "," + "" + "," + wayHosp + "\n")
        file.write(boxCo + "," + ut + "," + str(fips.get_county_fips(boxCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(boxCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + boxCase + "," + boxMort + "," + "" + "," + "" + "," + boxKhaus + "\n")
        file.write(cacheCo + "," + ut + "," + str(fips.get_county_fips(cacheCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(cacheCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + cacheCase + "," + cacheMort + "," + "" + "," + "" + "," + cacheKhaus + "\n")
        file.write(richCo + "," + ut + "," + str(fips.get_county_fips(richCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(richCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + richCase + "," + richMort + "," + "" + "," + "" + "," + richKhaus + "\n")
        file.write(davCo + "," + ut + "," + str(fips.get_county_fips(davCo,state=ut)).strip()
                   + "," + str(geocoder.opencage(davCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + davCases + "," + davMort + "," + "" + "," + "" + "," + davKhaus + "\n")
        file.write(saltLake + "," + ut + "," + str(fips.get_county_fips(saltLake,state=ut)).strip() 
                   + "," + str(geocoder.opencage(saltLake + ", " + ut,key='').latlng).strip('[]')
                   + "," + saltCase.replace(',','') + "," + "" + "," + "" + "," + "" + "," + saltKhaus + "\n")
        file.write(sanJ + "," + ut + "," + str(fips.get_county_fips(sanJ,state=ut)).strip() 
                   + "," + str(geocoder.opencage(sanJ + ", " + ut,key='').latlng).strip('[]')
                   + "," + sanCases + "," + "" + "," + "" + "," + "" + "," + sanKhaus + "\n")
        file.write(carbon + "," + ut + "," + str(fips.get_county_fips(carbon,state=ut)).strip() 
                   + "," + str(geocoder.opencage(carbon + ", " + ut,key='').latlng).strip('[]')
                   + "," + carCase + "," + "" + "," + carRec + "," + "" + "," + "" + "\n")
        file.write(emery + "," + ut + "," + str(fips.get_county_fips(emery,state=ut)).strip() 
                   + "," + str(geocoder.opencage(emery + ", " + ut,key='').latlng).strip('[]')
                   + "," + emCase + "," + "" + "," + emRec + "," + "" + "," + "" + "\n")
        file.write(grand + "," + ut + "," + str(fips.get_county_fips(grand,state=ut)).strip() 
                   + "," + str(geocoder.opencage(grand + ", " + ut,key='').latlng).strip('[]')
                   + "," + grCase + "," + "" + "," + grRec + "," + "" + "," + "" + "\n")
        file.write(beaver + "," + ut + "," + str(fips.get_county_fips(beaver,state=ut)).strip() 
                   + "," + str(geocoder.opencage(beaver + ", " + ut,key='').latlng).strip('[]')
                   + "," + "" + "," + "" + "," + "" + "," + "" + "," + "" + "\n")
        file.write(garfield + "," + ut + "," + str(fips.get_county_fips(garfield,state=ut)).strip() 
                   + "," + str(geocoder.opencage(garfield + ", " + ut,key='').latlng).strip('[]')
                   + "," + garCase + "," + "" + "," + "" + "," + "" + "," + garKhaus + "\n")
        file.write(iron + "," + ut + "," + str(fips.get_county_fips(iron,state=ut)).strip() 
                   + "," + str(geocoder.opencage(iron + ", " + ut,key='').latlng).strip('[]')
                   + "," + "" + "," + "" + "," + "" + "," + "" + "," + "" + "\n")
        file.write(kane + "," + ut + "," + str(fips.get_county_fips(kane,state=ut)).strip() 
                   + "," + str(geocoder.opencage(kane + ", " + ut,key='').latlng).strip('[]')
                   + "," + "" + "," + "" + "," + "" + "," + "" + "," + "" + "\n")
        file.write(washC + "," + ut + "," + str(fips.get_county_fips(washC,state=ut)).strip() 
                   + "," + str(geocoder.opencage(washC + ", " + ut,key='').latlng).strip('[]')
                   + "," + "" + "," + "" + "," + "" + "," + "" + "," + "" + "\n")
        file.write(sumCo + "," + ut + "," + str(fips.get_county_fips(sumCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(sumCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + sumCase + "," + "" + "," + "" + "," + "" + "," + sumKhaus + "\n")
        file.write(toolCo + "," + ut + "," + str(fips.get_county_fips(toolCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(toolCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + toolCase + "," + "" + "," + "" + "," + "" + "," + toolKhaus + "\n")
        file.write(uintahCo + "," + ut + "," + str(fips.get_county_fips(uintahCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(uintahCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + uintahCase + "," + "" + "," + "" + "," + "" + "," + uintahKhaus + "\n")
        file.write(duchCo + "," + ut + "," + str(fips.get_county_fips(duchCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(duchCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + duchCase + "," + "" + "," + "" + "," + "" + "," + duchKhaus + "\n")
        file.write(daggCo + "," + ut + "," + str(fips.get_county_fips(daggCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(daggCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + daggCase + "," + "" + "," + "" + "," + "" + "," + daggKhaus + "\n")
        file.write(utahCo + "," + ut + "," + str(fips.get_county_fips(utahCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(utahCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + utahCase + "," + "" + "," + "" + "," + "" + "," + utahKhaus + "\n")
        file.write(wasaCo + "," + ut + "," + str(fips.get_county_fips(wasaCo,state=ut)).strip() 
                   + "," + str(geocoder.opencage(wasaCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + wasaCase + "," + "" + "," + "" + "," + "" + "," + wasaKhaus + "\n")
        file.write(webCo + "," + ut + "," + webFips 
                   + "," + str(geocoder.opencage(webCo + ", " + ut,key='').latlng).strip('[]')
                   + "," + webCase + "," + "" + "," + "" + "," + "" + "," + webKhaus + "\n")
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    if (hold[67].split('\n')[1]) == 'Accomack County' and (hold[192].split('\n')[1]) == 'York County':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[67:69]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1].split(" ")[0] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")            
        
        #Alexandria City 
        file.write("Alexandria" + "," + va + "," + "51510" 
                    + "," + str(geocoder.opencage(hold[69].split('\n')[1].split(' (')[0] + ", " + va,  key='').latlng).strip('[]') + ","
                    + hold[69].split('\n')[5].replace(',','') + "," + hold[69].split('\n')[7].replace(',','') + "\n")

        for h in hold[70:78]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1].split(' (')[0] + "," + va, key='')
            file.write(take[1].split(' (')[0] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].split('[')[0] + "," + take[7].split('[')[0] + "\n")
                           
        #Bristol
        file.write("Bristol" + "," + va + "," + "51520" 
                   + "," + str(geocoder.opencage(hold[78].split('\n')[1]  + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[78].split('\n')[5].replace(',','') + "," + hold[78].split('\n')[7].replace(',','') + "\n")
        
        for h in hold[79:82]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
            
        #Buena Vista
        file.write("Buena Vista" + "," + va + "," + "51530" 
                   + "," + str(geocoder.opencage(hold[82].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[82].split('\n')[5].replace(',','') + "," + hold[82].split('\n')[7].replace(',','') + "\n")
        
        for h in hold[83:88]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        
        #Charlottesville
        file.write("Charlottesville" + "," + va + "," + "51540" 
                   + "," + str(geocoder.opencage(hold[88].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[88].split('\n')[5].replace(',','') + "," + hold[88].split('\n')[7].replace(',','') + "\n")
        
        #Chesapeake
        file.write("Chesapeake" + "," + va + "," + "51550" 
                   + "," + str(geocoder.opencage(hold[89].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[89].split('\n')[5].replace(',','') + "," + hold[89].split('\n')[7].replace(',','') + "\n")
        
        for h in hold[90:92]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        
        #Colonial Heights
        file.write("Colonial Heights" + "," + va + "," + "51570" 
                   + "," + str(geocoder.opencage(hold[92].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[92].split('\n')[5].replace(',','') + "," + hold[92].split('\n')[7].replace(',','') + "\n")
        
        #Covington
        file.write("Covington" + "," + va + "," + "51580" 
                   + "," + str(geocoder.opencage(hold[93].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[93].split('\n')[5].replace(',','') + "," + hold[93].split('\n')[7].replace(',','') + "\n")
        
        for h in hold[94:97]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
            
        #Danville
        file.write("Danville" + "," + va + "," + "51590" 
                   + "," + str(geocoder.opencage(hold[97].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[97].split('\n')[5].replace(',','') + "," + hold[97].split('\n')[7].replace(',','') + "\n")
        
        #Dinwiddie County
        file.write(hold[98].split('\n')[1] + "," + va + "," + str(fips.get_county_fips(hold[98].split('\n')[1],state=va)).strip() 
                   + "," + str(geocoder.opencage(hold[98].split('\n')[1] +", "  + va,  key='').latlng).strip('[]') + ","
                   + hold[98].split('\n')[5].replace(',','') + "," + hold[98].split('\n')[7].replace(',','') + "\n")
        
        #Emporia
        file.write("Emporia" + "," + va + "," + "51595" 
                   + "," + str(geocoder.opencage(hold[99].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[99].split('\n')[5].replace(',','') + "," + hold[99].split('\n')[7].replace(',','') + "\n")
        
        #Essex County
        file.write(hold[100].split('\n')[1] + "," + va + "," + str(fips.get_county_fips(hold[100].split('\n')[1],state=va)).strip() 
                   + "," + str(geocoder.opencage(hold[100].split('\n')[1] +", "  + va,  key='').latlng).strip('[]') + ","
                   + hold[100].split('\n')[5].replace(',','') + "," + hold[100].split('\n')[7].replace(',','') + "\n")

        #Fairfax city
        file.write("Fairfax" + "," + va + "," + "51600" 
                   + "," + str(geocoder.opencage(hold[101].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[101].split('\n')[5].replace(',','') + "," + hold[101].split('\n')[7].replace(',','') + "\n")
        
        #Fairfax County
        file.write(hold[102].split('\n')[1] + "," + va + "," + str(fips.get_county_fips(hold[102].split('\n')[1],state=va)).strip() 
                   + "," + str(geocoder.opencage(hold[102].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[102].split('\n')[5].replace(',','') + "," + hold[102].split('\n')[7].replace(',','') + "\n")
        
        #Falls Church
        file.write("Falls Church" + "," + va + "," + "51610" 
                   + "," + str(geocoder.opencage(hold[103].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[103].split('\n')[5].replace(',','') + "," + hold[103].split('\n')[7].replace(',','') + "\n")
        for h in hold[104:107]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Franklin
        file.write("Franklin" + "," + va + "," + "51620" 
                   + "," + str(geocoder.opencage(hold[108].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[108].split('\n')[5].replace(',','') + "," + hold[108].split('\n')[7].replace(',','') + "\n")
        for h in hold[109:110]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Fredericksburg city
        file.write("Fredericksburg" + "," + va + "," + "51630" 
                   + "," + str(geocoder.opencage(hold[110].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[110].split('\n')[5].replace(',','') + "," + hold[110].split('\n')[7].replace(',','') + "\n")
        #Galax
        file.write("Galax" + "," + va + "," + "51640" 
                   + "," + str(geocoder.opencage(hold[111].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[111].split('\n')[5].replace(',','') + "," + hold[111].split('\n')[7].replace(',','') + "\n")
        for h in hold[112:118]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Hampton
        file.write("Hampton" + "," + va + "," + "51650" 
                   + "," + str(geocoder.opencage(hold[118].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[118].split('\n')[5].replace(',','') + "," + hold[118].split('\n')[7].replace(',','') + "\n")
        #Hanover
        file.write(hold[119].split('\n')[1] + "," + va + "," + str(fips.get_county_fips(hold[119].split('\n')[1],state=va)).strip() 
                   + "," + str(geocoder.opencage(hold[119].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[119].split('\n')[5].replace(',','') + "," + hold[119].split('\n')[7].replace(',','') + "\n")
        #Harrisonburg
        file.write("Harrisonburg" + "," + va + "," + "51660" 
                   + "," + str(geocoder.opencage(hold[120].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[120].split('\n')[5].replace(',','') + "," + hold[120].split('\n')[7].replace(',','') + "\n")
        for h in hold[121:123]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Hopewell
        file.write("Hopewell" + "," + va + "," + "51670" 
                   + "," + str(geocoder.opencage(hold[123].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[123].split('\n')[5].replace(',','') + "," + hold[123].split('\n')[7].replace(',','') + "\n")
        for h in hold[124:131]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Lexington
        file.write("Lexington" + "," + va + "," + "51678" 
                   + "," + str(geocoder.opencage(hold[131].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[131].split('\n')[5].replace(',','') + "," + hold[131].split('\n')[7].replace(',','') + "\n")
        for h in hold[132:135]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Lynchburg
        file.write("Lynchburg" + "," + va + "," + "51680" 
                   + "," + str(geocoder.opencage(hold[135].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[135].split('\n')[5].replace(',','') + "," + hold[135].split('\n')[7].replace(',','') + "\n")
        #Madison County
        file.write(hold[136].split('\n')[1] + "," + va + "," + str(fips.get_county_fips(hold[136].split('\n')[1],state=va)).strip() 
                   + "," + str(geocoder.opencage(hold[136].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[136].split('\n')[5].replace(',','') + "," + hold[136].split('\n')[7].replace(',','') + "\n")
        #Manassas (city)
        file.write("Manassas" + "," + va + "," + "51683" 
                   + "," + str(geocoder.opencage(hold[137].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[137].split('\n')[5].replace(',','') + "," + hold[137].split('\n')[7].replace(',','') + "\n")
        #Manassas Park
        file.write("Manassas Park" + "," + va + "," + "51685" 
                   + "," + str(geocoder.opencage(hold[138].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[138].split('\n')[5].replace(',','') + "," + hold[138].split('\n')[7].replace(',','') + "\n")
        for h in hold[139:145]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Newport News
        file.write("Newport News" + "," + va + "," + "51700" 
                   + "," + str(geocoder.opencage(hold[145].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[145].split('\n')[5].replace(',','') + "," + hold[145].split('\n')[7].replace(',','') + "\n")
        #Norfolk
        file.write("Norfolk" + "," + va + "," + "51710" 
                   + "," + str(geocoder.opencage(hold[146].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[146].split('\n')[5].replace(',','') + "," + hold[146].split('\n')[7].replace(',','') + "\n")
        for h in hold[147:149]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Norton
        file.write("Norton" + "," + va + "," + "51720" 
                   + "," + str(geocoder.opencage(hold[149].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[149].split('\n')[5].replace(',','') + "," + hold[149].split('\n')[7].replace(',','') + "\n")
        for h in hold[150:153]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Petersburg
        file.write("Petersburg" + "," + va + "," + "51730" 
                   + "," + str(geocoder.opencage(hold[153].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[153].split('\n')[5].replace(',','') + "," + hold[153].split('\n')[7].replace(',','') + "\n")
        #Pittsylvania County
        file.write(hold[154].split('\n')[1] + "," + va + "," + str(fips.get_county_fips(hold[154].split('\n')[1],state=va)).strip() 
                   + "," + str(geocoder.opencage(hold[154].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[154].split('\n')[5].replace(',','') + "," + hold[154].split('\n')[7].replace(',','') + "\n")
        #Poquoson
        file.write("Poquoson" + "," + va + "," + "51735" 
                   + "," + str(geocoder.opencage(hold[155].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[155].split('\n')[5].replace(',','') + "," + hold[155].split('\n')[7].replace(',','') + "\n")
        #Portsmouth
        file.write("Portsmouth" + "," + va + "," + "51740" 
                   + "," + str(geocoder.opencage(hold[156].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[156].split('\n')[5].replace(',','') + "," + hold[156].split('\n')[7].replace(',','') + "\n")
        for h in hold[157:162]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Radford
        file.write("Radford" + "," + va + "," + "51750" 
                   + "," + str(geocoder.opencage(hold[162].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[162].split('\n')[5].replace(',','') + "," + hold[162].split('\n')[7].replace(',','') + "\n")
        #Rappahannock County
        file.write(hold[163].split('\n')[1] + "," + va + "," + str(fips.get_county_fips(hold[163].split('\n')[1],state=va)).strip() 
                   + "," + str(geocoder.opencage(hold[163].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[163].split('\n')[5].replace(',','') + "," + hold[163].split('\n')[7].replace(',','') + "\n")
        #Richmond (city)
        file.write("Richmond" + "," + va + "," + "51760" 
                   + "," + str(geocoder.opencage(hold[164].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[164].split('\n')[5].replace(',','') + "," + hold[164].split('\n')[7].replace(',','') + "\n")
        #Richmond County
        file.write(hold[165].split('\n')[1] + "," + va + "," + str(fips.get_county_fips(hold[165].split('\n')[1],state=va)).strip() 
                   + "," + str(geocoder.opencage(hold[165].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[165].split('\n')[5].replace(',','') + "," + hold[165].split('\n')[7].replace(',','') + "\n")
        #Roanoke
        file.write("Roanoke" + "," + va + "," + "51770" 
                   + "," + str(geocoder.opencage(hold[166].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[166].split('\n')[5].replace(',','') + "," + hold[166].split('\n')[7].replace(',','') + "\n")
        for h in hold[167:171]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Salem
        file.write("Salem" + "," + va + "," + "51775" 
                   + "," + str(geocoder.opencage(hold[171].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[171].split('\n')[5].replace(',','') + "," + hold[171].split('\n')[7].replace(',','') + "\n")
        for h in hold[172:178]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Stauton
        file.write("Stauton" + "," + va + "," + "51790" 
                   + "," + str(geocoder.opencage(hold[178].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[178].split('\n')[5].replace(',','') + "," + hold[178].split('\n')[7].replace(',','') + "\n")
        #Suffolk
        file.write("Suffolk" + "," + va + "," + "51800" 
                   + "," + str(geocoder.opencage(hold[179].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[179].split('\n')[5].replace(',','') + "," + hold[179].split('\n')[7].replace(',','') + "\n")
        for h in hold[180:183]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Virginia Beach
        file.write("Virginia Beach" + "," + va + "," + "51810" 
                   + "," + str(geocoder.opencage(hold[183].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[183].split('\n')[5].replace(',','') + "," + hold[183].split('\n')[7].replace(',','') + "\n")
        for h in hold[184:186]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
        #Waynesboro
        file.write("Waynesboro" + "," + va + "," + "51820" 
                   + "," + str(geocoder.opencage(hold[186].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[186].split('\n')[5].replace(',','') + "," + hold[186].split('\n')[7].replace(',','') + "\n")
        #Westmoreland County
        file.write(hold[187].split('\n')[1] + "," + va + "," + str(fips.get_county_fips(hold[187].split('\n')[1],state=va)).strip() 
                   + "," + str(geocoder.opencage(hold[187].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[187].split('\n')[5].replace(',','') + "," + hold[187].split('\n')[7].replace(',','') + "\n")
        #Williamsburg
        file.write("Williamsburg" + "," + va + "," + "51830" 
                   + "," + str(geocoder.opencage(hold[188].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[188].split('\n')[5].replace(',','') + "," + hold[188].split('\n')[7].replace(',','') + "\n")
        #Winchester
        file.write("Winchester" + "," + va + "," + "51840" 
                   + "," + str(geocoder.opencage(hold[189].split('\n')[1] + ", " + va,  key='').latlng).strip('[]') + ","
                   + hold[189].split('\n')[5].replace(',','') + "," + hold[189].split('\n')[7].replace(',','') + "\n")
        for h in hold[190:193]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + va, key='')
            file.write(take[1] + "," + va + "," + str(fips.get_county_fips(take[1], state=va)).strip() 
                       + "," + str(locale.latlng).strip('[]') + ","
                       + take[5].replace(',','') + "," + take[7].replace(',','') + "\n")
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
    headers = "State/Territory,State/Territory,fips,Latitude,Longitude,Confirmed Cases,Deaths,Recovered, , ,Pending\n"
    
    tags = tables.findAll('p')
    
    pos = tags[3].text.split(': ')[0]
    posNo = tags[3].text.split(': ')[1].split('\xa0')[0]
    
    recov = tags[6].text.split(': ')[0]
    recNo = tags[6].text.split(': ')[1].split('/')[0]
    
    pend = tags[5].text.split(': ')[0]
    pendNo = tags[5].text.split(': ')[1].split(' ')[0]
    
    mort = tags[7].text.split(': ')[0]
    mortNo = tags[7].text.split(': ')[1]
    
    if (pos == 'Positive') and (pend == 'Pending'):
    
        file = open(csvfile, "w")
        file.write(headers)
        
        locale = liegen.geocode(vi)
        sleep(1)
        file.write(vi + "," + vi + "," + str(fips.get_state_fips("Virgin Islands")) 
                   + "," + str(locale.latitude) + "," 
                   + str(locale.longitude) + "," + posNo + "," + mortNo + "," 
                   + recNo + "," + "" + "," + "" + "," + pendNo + "\n")
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
                
    if (hold[64].split('\n')[1]) == 'Addison' and (hold[78].split('\n')[1]) == 'Unassigned county':

        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[64:78]:
            take = h.split('\n')
            locale = liegen.geocode(take[1] + co + "," + vt)
            catch_TimeOut(take[1] + co + "," + vt)
            file.write(take[1] + "," + vt + "," + str(fips.get_county_fips(take[1],state=vt)).strip() 
                       + "," + str(locale.latitude) + ","
                       + str(locale.longitude) + "," + take[3] + "," + take[5] + "\n")
            sleep(1.1)
        
        file.write(hold[78].split('\n')[1] + "," + vt + "," + str(fips.get_state_fips(vt)).strip() + "," 
                   + str(liegen.geocode(vt).latitude) + ","
                   + str(liegen.geocode(vt).longitude) + "," + hold[78].split('\n')[3] 
                   + "," + hold[78].split('\n')[5] + "\n")
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    if (hold[74].split('\n')[1]) == 'Adams' and (hold[113].split('\n')[1]) == 'Unassigned':
    
        file = open(csvfile, "w")
        file.write(headers)    
    
        for h in hold[74:113]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + co + "," + wa, key='')
            file.write(take[1] + "," + wa + "," + str(fips.get_county_fips(take[1],state=wa)).strip() + "," 
                       + str(locale.latlng).strip('[]') + "," 
                       + take[3].split('[')[0].replace(',','') 
                       + "," + take[5].split('[')[0].replace(',','') + "\n")
            
        file.write(hold[113].split('\n')[1] + "," + wa + "," + str(fips.get_state_fips(wa)).strip() + "," 
                   + str(liegen.geocode(wa).latitude) + "," 
                   + str(liegen.geocode(wa).longitude) + "," + hold[113].split('\n')[3].split('[')[0].replace(',','') 
                   + "," + hold[113].split('\n')[5].split('[')[0].replace(',','') + "\n")
        
        file.close()
    
        print("Washington scraper is complete.")
    else:
        print("ERROR: Must fix Washington scraper.")
    
def wiScrape():
    
    #Data pulled from Wisconsin's DOH open data source
    widoh = pd.read_csv('https://opendata.arcgis.com/datasets/360c2995846e4af99461cb80d3ed8c27_1.csv')
    #Add state to the dataframe
    widoh['State'] = "WISCONSIN"
    #Add lat, long to the dataframe
    county = widoh['NAME']
    county = county.tolist()
    rose = []
    for c in county:
        locale = geocoder.opencage(c + ", " + "WISCONSIN", key= '').latlng
        rose.append(locale)
    widoh['Latitude/Longitude'] = rose
    #Fix column locations
    lund = widoh.reindex(columns = ['NAME','State','GEOID','Latitude/Longitude','POSITIVE','DEATHS'])
    #Change column names
    nylund = lund.rename(columns = {'NAME': 'County', 'GEOID':'fips', 'POSITIVE':'Confirmed Cases', 'DEATHS':'Deaths'})
    nylund = nylund.fillna(0)
    
    nylund.to_csv('COVID-19_cases_widoh.csv', index = False, header = True)
    
    if widoh['NAME'][0] == 'Adams':
    
        print("Wisconsin scraper is complete.")
    else:
        print("ERROR: Must fix Wisconsin scraper.")
    
def wvScrape():
    
    wvWiki = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_West_Virginia'

    wvClient = req(wvWiki)
    
    site_parse = soup(wvClient.read(), "lxml")
    wvClient.close()
    
    tables = site_parse.find("div", {"class": "mw-parser-output"}).find_all('tbody')
    
    wv = "WEST VIRGINIA"
    
    csvfile = "COVID-19_cases_wvWiki.csv"
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)
    
    if hold[60].split('\n')[1] == 'Barbour County' and hold[107].split('\n')[1] == 'Wyoming County':
    
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[60:108]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + "," + wv, key='')
            file.write(take[1] + "," + wv + "," + str(fips.get_county_fips(take[1],state=wv)).strip() + ","
                       + str(locale.latlng).strip('[]') + ","
                       + take[3] + "," + take[5].split('[')[0] + "\n")
            #sleep(1)
        
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
    headers = "County,State,fips,Latitude,Longitude,Confirmed Cases,Deaths\n"
    
    hold = []
    
    for t in tables:
            pull = t.findAll('tr')
            for p in pull:
                take = p.get_text()
                hold.append(take)

    if (hold[70].split('\n')[1]) == 'Albany' and (hold[92].split('\n')[1]) == 'Weston':
                
        file = open(csvfile, "w")
        file.write(headers)
        
        for h in hold[70:93]:
            take = h.split('\n')
            locale = geocoder.opencage(take[1] + co + "," + wy, key='')
            file.write(take[1] + "," + wy + "," + str(fips.get_county_fips(take[1],state=wy)).strip() + ","
                       + str(locale.latlng).strip('[]') + "," 
                       + take[3] + "," + take[7] + "\n")
        
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
    
    path = "C:/Users/Erwac/Desktop/COVID-19/COVID-19-Outbreak-Visualization-Tool/Web Scrapers/US States"
    os.chdir(path)
    
    csvFile = "csv"
    
    alles_COVID = []
    
    alles_COVID = [i for i in glob.glob('COVID-19_*.{}'.format(csvFile))]
    
    hold = []
    
    for i in alles_COVID:
        reader = list(csv.reader(open(i)))
        hold.append(reader)
    
    
    headers = ['County', 'State', 'fips', 'Latitude', 'Longitude', 
               'Confirmed Cases', 'Deaths', 'Recoveries', 'Released from Isolation',
               'Hospitalized']
    
    f = open("combined.csv","w")
    writer = csv.writer(f)
    writer.writerow(headers)
    
    for col in hold:
        writer.writerows(col[1:])

    f.close()

    
if __name__ == "__main__":
    main()
