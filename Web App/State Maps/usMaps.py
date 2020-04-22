from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px
import math

#Missing counties in maps is result of missing data for those counties

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

#-------------------------ALASKA CHOROPLETH MAP------------------------------#
akDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_akWiki.csv', dtype={'fips':str})
cleanAK = akDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxAK = (math.ceil(cleanAK['Confirmed Cases'].max() / 50.0) * 50.0) + 150

akFig = px.choropleth_mapbox(cleanAK, geojson=counties, locations='fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'aggrnyl',
                             range_color = (0,maxAK),
                             hover_data = ['County', 'Confirmed Cases', 'Latitude', 'Longitude'],
                             zoom = 3, center = {"lat": 63.860036, "lon": -150.255849},
                             opacity = 0.6, labels = {'County':'Community','Confirmed Cases': 'Confirmed Cases'})

akFig.update_layout(mapbox_style="satellite-streets", mapbox_accesstoken='pk')
akFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
akFig.show()

#-------------------------ALABAMA CHOROPLETH MAP------------------------------#
alDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_aldoh.csv', dtype={'fips': str})
cleanAL = alDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxAL = (math.ceil(cleanAL['Confirmed Cases'].max() / 50.0) * 50.0) + 150

#Leaving this here in case we will need it later
#alfips = ['01001','01003','01005','01007','01009','01011','01013','01015','01017','01019','01021','01023','01025','01027','01029',
#          '01031','01033','01035','01037','01039','01041','01043','01045','01047','01049','01051','01053','01055','01057','01059',
#          '01061','01063','01065','01067','01069','01071','01073','01075','01077','01079','01081','01083','01085','01087','01089',
#          '01091','01093','01095','01097','01099','01101','01103','01105','01107','01109','01111','01113','01117','01115','01119',
#          '01121','01123','01125','01127','01129','01131','01133']

alFig = px.choropleth_mapbox(cleanAL, geojson=counties, locations = 'fips', color='Confirmed Cases',
                           color_continuous_scale="viridis",
                           range_color=(0,maxAL),
                           hover_data = ['County', 'Confirmed Cases','Deaths','Latitude','Longitude'],
                           zoom=6, center = {"lat": 32.756902, "lon": -86.844513},
                           opacity=0.6, labels={'Confirmed Cases': 'Confirmed Cases'}
                           )

alFig.update_layout(mapbox_style="satellite-streets", mapbox_accesstoken='pk')
alFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
alFig.show()
#-------------------------ARKANSAS CHOROPLETH MAP------------------------------#

arDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_arWiki.csv', dtype={'fips':str})
cleanAR = arDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxAR = (math.ceil(cleanAR['Confirmed Cases'].max() / 50.0) * 50.0) + 150

arFig = px.choropleth_mapbox(cleanAR, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'sunsetdark', range_color = (0,maxAR),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom = 5.7, center = {"lat": 34.899764, "lon": -92.439213},
                             opacity = 0.6, labels = {"County": "County"})

arFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
arFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
arFig.show()

#-------------------------ARIZONA CHOROPLETH MAP------------------------------#
azDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_azWiki.csv', dtype = {'fips':str})
cleanAZ = azDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxAZ = (math.ceil(cleanAZ['Confirmed Cases'].max() / 50.0) * 50.0) + 150

azFig = px.choropleth_mapbox(cleanAZ, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'picnic', range_color = (0,maxAZ),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.6, center = {"lat": 34.333217, "lon": -111.712983},
                             opacity = 0.6, labels = {"County": "County"})

azFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
azFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
azFig.show()

#-------------------------CALIFORNIA CHOROPLETH MAP------------------------------#
caDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_caWiki.csv', dtype = {'fips':str})
cleanCA = caDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxCA = (math.ceil(caDF['Confirmed Cases'].max() / 50.0) * 50.0) + 150

caFig = px.choropleth_mapbox(caDF, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'mrybm', range_color = (0,maxCA),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom = 4.65, center = {"lat": 37.863942, "lon": -120.753667},
                             opacity = 0.6, labels = {"County": "County"}, 
                             )

caFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
caFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
caFig.update_geos(fitbounds="locations")
caFig.update_layout(
    title = "COVID-19's Impact in California",
)
caFig.show()

#-------------------------COLORADO CHOROPLETH MAP------------------------------#
coDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_coDOH.csv', dtype = {'fips':str})
cleanCO = coDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxCO = (math.ceil(cleanCO['Confirmed Cases'].max() / 50.0) * 50.0) + 150

coFig = px.choropleth_mapbox(cleanCO, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'mint', range_color = (0,maxCO),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.5, center = {"lat": 39.055183, "lon": -105.547831},
                             opacity = 0.6, labels = {"County": "County"})

coFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
coFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
coFig.update_layout(title = (("Impact of COVID-19 in Arizona" + "\n" 
      + "Unknown or pending: " + str(cleanCO.loc[56, 'Confirmed Cases']) + " Cases" + ", "
      + str(cleanCO.loc[56, 'Confirmed Cases']) + " Deaths" + "\n"
      + "Out of State: " + str(cleanCO.loc[57, 'Confirmed Cases']) + " Cases" + ", "
      + str(cleanCO.loc[57, 'Confirmed Cases']) + " Deaths")))
coFig.show()

#-------------------------CONNECTICUT CHOROPLETH MAP------------------------------#
ctDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ctNews.csv', dtype = {'fips':str})
cleanCT = ctDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxCT = (math.ceil(cleanCT['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ctFig = px.choropleth_mapbox(cleanCT, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'curl_r', range_color = (0,maxCT),
                             hover_data = ['County', 'Confirmed Cases'],
                             zoom = 7, center = {"lat": 41.647811, "lon": -72.641075},
                             opacity = 0.6, labels = {"County": "County"})

ctFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
ctFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
ctFig.show()

#-------------------------DELAWARE CHOROPLETH MAP------------------------------#
deDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_deWiki.csv', dtype = {'fips':str})
cleanDE = deDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxDE = (math.ceil(cleanDE['Confirmed Cases'].max() / 50.0) * 50.0) + 150

deFig = px.choropleth_mapbox(cleanDE, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'geyser', range_color = (0,maxDE),
                             hover_data = ['County', 'Confirmed Cases'],
                             zoom = 7.5, center = {"lat": 39.051475, "lon": -75.416010},
                             opacity = 0.6, labels = {"County": "County"})

deFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
deFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
deFig.show()

#-------------------------FLORIDA CHOROPLETH MAP------------------------------#
flDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_flWiki.csv', dtype = {'fips':str})
cleanFL = flDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxFL = (math.ceil(cleanFL['Confirmed Cases'].max() / 50.0) * 50.0) + 150

flFig = px.choropleth_mapbox(cleanFL, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'sunset', range_color = (0,maxFL),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Hospitalizations'],
                             zoom = 5.35, center = {"lat": 28.311684, "lon": -81.446706},
                             opacity = 0.6, labels = {"County": "County"})

flFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
flFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
flFig.show()

#-------------------------GEORGIA CHOROPLETH MAP------------------------------#
gaDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_gadoh.csv', dtype = {'fips':str})
cleanGA = gaDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxGA = (math.ceil(cleanGA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

gaFig = px.choropleth_mapbox(cleanGA, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'teal', range_color = (0,maxGA),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.8, center = {"lat": 32.699989, "lon": -83.427133},
                             opacity = 0.6, labels = {"County": "County"})

gaFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
gaFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
gaFig.show()

##-------------------------GUAM/ MP CHOROPLETH MAP------------------------------#
#guMP = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_gu_mp_Wiki.csv')
#cleanGM = guMP.fillna(0)
#
##Used to round up to a proper max for the range_color function
#maxGM = (math.ceil(cleanGM['Confirmed Cases'].max() / 50.0) * 50.0) + 150
#
#gmFig = px.choropleth_mapbox(cleanGM, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
#                             color_continuous_scale = 'tropic', range_color = (0,maxGM),
#                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
#                             zoom = 5, center = {"lat": 14.272591, "lon": 145.346504},
#                             opacity = 0.6, labels = {"County": "Territory"})
#
#gmFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
#gmFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#gmFig.show()


#-------------------------HAWAI'I CHOROPLETH MAP------------------------------#
hiDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_hidoh.csv', dtype = {'fips':str})
cleanHI = hiDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxHI = (math.ceil(cleanHI['Total Cases'].max() / 50.0) * 50.0) + 150

hiFig = px.choropleth_mapbox(cleanHI, geojson = counties, locations = 'fips', color = 'Total Cases',
                             color_continuous_scale = 'magma_r', range_color = (0,maxHI),
                             hover_data = ['County', 'Total Cases', 'Deaths', 'Released from Isolation', 'Hospitalization'],
                             zoom = 5.8, center = {"lat": 20.906635, "lon": -157.027297},
                             opacity = 0.6, labels = {"County": "County"})

hiFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
hiFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
hiFig.show()

#---------------------------IDAHO CHOROPLETH MAP------------------------------#
idDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_idWiki.csv', dtype = {'fips':str})
cleanID = idDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxID = (math.ceil(cleanID['Confirmed Cases'].max() / 50.0) * 50.0) + 150

idFig = px.choropleth_mapbox(cleanID, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'plotly3', range_color = (0,maxID),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 4.9, center = {"lat": 45.570854, "lon": -115.131137},
                             opacity = 0.55, labels = {"County": "County"})

idFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
idFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
idFig.show()


#---------------------------ILLINOIS CHOROPLETH MAP------------------------------#
ilDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ilWiki.csv', dtype = {'fips':str})
cleanIL = ilDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxIL = (math.ceil(cleanIL['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ilFig = px.choropleth_mapbox(cleanIL, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'plasma_r', range_color = (0,maxIL),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom = 5.5, center = {"lat": 40.0190, "lon": -88.3000},
                             opacity = 0.6, labels = {"County": "County"})

ilFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
ilFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
ilFig.show()

#---------------------------INDIANA CHOROPLETH MAP------------------------------#
inDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_inWiki.csv', dtype = {'fips':str})
cleanIN = inDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxIN = (math.ceil(cleanIN['Confirmed Cases'].max() / 50.0) * 50.0) + 150

inFig = px.choropleth_mapbox(cleanIN, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'ylgnbu', range_color = (0,maxIN),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.6, center = {"lat": 40.013050, "lon": -86.208909},
                             opacity = 0.6, labels = {"County": "County"})

inFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
inFig.update_layout(margin={"r":100,"t":0,"l":100,"b":0})
inFig.show()

#---------------------------IOWA CHOROPLETH MAP------------------------------#
ioDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ioWiki.csv', dtype = {'fips':str})
cleanIO = ioDF.fillna(0)


#Used to round up to a proper max for the range_color function
maxIO = (math.ceil(cleanIO['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ioFig = px.choropleth_mapbox(cleanIO, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'rdpu', range_color = (0,maxIO),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.5, center = {"lat": 42.074622, "lon": -93.500036},
                             opacity = 0.6, labels = {"County": "County"})

ioFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
ioFig.update_layout(margin={"r":100,"t":0,"l":100,"b":0})
ioFig.show()

#---------------------------KANSAS CHOROPLETH MAP------------------------------#
kaDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_kaWiki.csv', dtype = {'fips':str})
cleanKA = kaDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxKA = (math.ceil(cleanKA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

kaFig = px.choropleth_mapbox(cleanKA, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'darkmint', range_color = (0,maxKA),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.6, center = {"lat": 38.541749, "lon": -98.428791},
                             opacity = 0.6, labels = {"County": "County"})

kaFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
kaFig.update_layout(margin={"r":100,"t":0,"l":100,"b":0})
kaFig.show()

#---------------------------KENTUCKY CHOROPLETH MAP------------------------------#
kyDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_kyNews.csv', dtype = {'fips':str})
cleanKY = kyDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxKY = (math.ceil(cleanKY['Confirmed Cases'].max() / 50.0) * 50.0) + 150

kyFig = px.choropleth_mapbox(cleanKY, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'twilight', range_color = (0,maxKY),
                             color_continuous_midpoint = maxKY/2,
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.8, center = {"lat": 37.526671, "lon": -85.290470},
                             opacity = 0.6, labels = {"County": "County"})

kyFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
kyFig.update_layout(margin={"r":90,"t":0,"l":90,"b":0})
kyFig.show()

#---------------------------LOUISIANA CHOROPLETH MAP------------------------------#
laDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_laWiki.csv', dtype = {'fips':str})
cleanLA = laDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxLA = (math.ceil(cleanLA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

laFig = px.choropleth_mapbox(cleanLA, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'bluyl', range_color = (0,maxLA),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 6, center = {"lat": 31.220691, "lon": -92.381019},
                             opacity = 0.6, labels = {"County": "Parish"})

laFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
laFig.update_layout(margin={"r":100,"t":0,"l":100,"b":0})
laFig.show()

#---------------------------MASSACHUSETTS CHOROPLETH MAP------------------------------#
maDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_maNews.csv', dtype = {'fips':str})
cleanMA = maDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxMA = (math.ceil(cleanMA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

maFig = px.choropleth_mapbox(cleanMA, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'brwnyl', range_color = (0,maxMA),
                             hover_data = ['County', 'Confirmed Cases'],
                             zoom = 6.5, center = {"lat": 42.357952, "lon": -72.062769},
                             opacity = 0.6, labels = {"County": "County"})

maFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
maFig.update_layout(margin={"r":0,"t":90,"l":90,"b":0})
maFig.show()

#---------------------------MARYLAND CHOROPLETH MAP------------------------------#
mdDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_mdWiki.csv', dtype = {'fips':str})
cleanMD = mdDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxMD = (math.ceil(cleanMD['Confirmed Cases'].max() / 50.0) * 50.0) + 150

mdFig = px.choropleth_mapbox(cleanMD, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'purpor', range_color = (0,maxMD),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom = 6.6, center = {"lat": 39.026261, "lon": -76.808917},
                             opacity = 0.6, labels = {"County": "County"})

mdFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
mdFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
mdFig.show()

#---------------------------MAINE CHOROPLETH MAP------------------------------#
meDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_meDDS.csv', dtype = {'fips':str})
cleanME = meDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxME = (math.ceil(cleanME['Confirmed Cases'].max() / 50.0) * 50.0) + 150

meFig = px.choropleth_mapbox(cleanME, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'emrld', range_color = (0,maxME),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom = 5.8, center = {"lat": 45.274323, "lon": -69.202765},
                             opacity = 0.6, labels = {"County": "County"})

meFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
meFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
meFig.show()

#---------------------------MICHIGAN CHOROPLETH MAP------------------------------#
miDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_midoh.csv', dtype = {'fips':str})
cleanMI = miDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxMI = (math.ceil(cleanMI['Confirmed Cases'].max() / 50.0) * 50.0) + 150

miFig = px.choropleth_mapbox(cleanMI, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'spectral_r', range_color = (0,maxMI),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.45, center = {"lat": 44.488022, "lon": -84.746015},
                             opacity = 0.6, labels = {"County": "County"})

miFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
miFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
miFig.show()

#---------------------------MINNESOTA CHOROPLETH MAP------------------------------#
mnDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_mndoh.csv', dtype = {'fips':str})
cleanMN = mnDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxMN = (math.ceil(cleanMN['Confirmed Cases'].max() / 50.0) * 50.0) + 150

mnFig = px.choropleth_mapbox(cleanMN, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'tealgrn_r', range_color = (0,maxMN),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.3, center = {"lat": 46.441920, "lon": -93.361527},
                             opacity = 0.6, labels = {"County": "County"})

mnFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
mnFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
mnFig.show()

#---------------------------MISSOURI CHOROPLETH MAP------------------------------#
moDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_modoh.csv', dtype = {'fips':str})
cleanMO = moDF.fillna(0)
aggrr = {'Confirmed Cases': 'sum', 'Deaths':'sum', 'County':'first','fips':'first'}
realness = cleanMO.groupby(['County']).aggregate(aggrr)

#Used to round up to a proper max for the range_color function
maxMO = (math.ceil(cleanMO['Confirmed Cases'].max() / 50.0) * 50.0) + 150

moFig = px.choropleth_mapbox(realness, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'temps', range_color = (0,maxMO),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.8, center = {"lat": 38.462767, "lon": -92.574534},
                             opacity = 0.6, labels = {"County": "County"})

moFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
moFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
moFig.show()

#---------------------------MISSISSIPPI CHOROPLETH MAP------------------------------#
msDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_msdoh.csv', dtype = {'fips':str})
cleanMS = msDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxMS = (math.ceil(cleanMS['Confirmed Cases'].max() / 50.0) * 50.0) + 150

msFig = px.choropleth_mapbox(cleanMS, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'balance', range_color = (0,maxMS),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.7, center = {"lat": 32.940921, "lon": -89.702028},
                             opacity = 0.6, labels = {"County": "County"})

msFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
msFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
msFig.show()

#---------------------------MONTANA CHOROPLETH MAP------------------------------#
mtDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_mtdoh.csv', dtype = {'fips':str})
cleanMT = mtDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxMT = (math.ceil(cleanMT['Confirmed Cases'].max() / 50.0) * 50.0) + 150

mtFig = px.choropleth_mapbox(cleanMT, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'sunset_r', range_color = (0,maxMT),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5, center = {"lat": 47.072205, "lon": -109.398931},
                             opacity = 0.6, labels = {"County": "County"})

mtFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
mtFig.update_layout(margin={"r":0,"t":100,"l":0,"b":0})
mtFig.show()

#---------------------------NORTH CAROLINA CHOROPLETH MAP------------------------------#
ncDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ncdoh.csv', dtype = {'fips':str})
cleanNC = ncDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxNC = (math.ceil(cleanNC['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ncFig = px.choropleth_mapbox(cleanNC, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'delta', range_color = (0,maxNC),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.6, center = {"lat": 35.591409, "lon": -78.979338},
                             opacity = 0.7, labels = {"County": "County"})

ncFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
ncFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
ncFig.show()

#---------------------------NORTH DAKOTA CHOROPLETH MAP------------------------------#
ndDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ndWiki.csv', dtype = {'fips':str})
cleanNA = ndDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxND = (math.ceil(cleanNA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ndFig = px.choropleth_mapbox(cleanNA, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'tealrose', range_color = (0,maxND),
                             hover_data = ['County', 'Confirmed Cases'],
                             zoom = 6, center = {"lat": 47.528438, "lon": -100.445038},
                             opacity = 0.6, labels = {"County": "County"})

ndFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
ndFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
ndFig.show()

#---------------------------NEBRASKA CHOROPLETH MAP------------------------------#
neDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_neWiki.csv', dtype = {'fips':str})
cleanNE = neDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxNE = (math.ceil(cleanNE['Confirmed Cases'].max() / 50.0) * 50.0) + 150

neFig = px.choropleth_mapbox(cleanNE, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'teal', range_color = (0,maxNE),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 6, center = {"lat": 41.527111, "lon": -99.810728},
                             opacity = 0.6, labels = {"County": "County"})

neFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
neFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
neFig.show()

#---------------------------NEW HAMPSHIRE CHOROPLETH MAP-----------------------------#
nhDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_nhNews.csv', dtype = {'fips':str})
cleanNH = nhDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxNH = (math.ceil(cleanNH['Confirmed Cases'].max() / 50.0) * 50.0) + 150

nhFig = px.choropleth_mapbox(cleanNH, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'phase', range_color = (0,maxNH),
                             hover_data = ['County', 'Confirmed Cases'],
                             zoom = 6.2, center = {"lat": 43.989517, "lon": -71.469112},
                             opacity = 0.6, labels = {"County": "County"})

nhFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
nhFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
nhFig.show()

#---------------------------NEW JERSEY CHOROPLETH MAP-----------------------------#
njDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_njWiki.csv', dtype = {'fips':str})
cleanNJ = njDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxNJ = (math.ceil(cleanNJ['Confirmed Cases'].max() / 50.0) * 50.0) + 150

njFig = px.choropleth_mapbox(cleanNJ, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'curl', range_color = (0,maxNJ),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom = 6.5, center = {"lat": 40.267895, "lon": -74.412674},
                             opacity = 0.6, labels = {"County": "County"})

njFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
njFig.update_layout(margin={"r":100,"t":0,"l":100,"b":0})
njFig.show()

#---------------------------NEW MEXICO CHOROPLETH MAP-----------------------------#
nmDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_nmdoh.csv', dtype = {'fips':str})
cleanNM = nmDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxNM = (math.ceil(cleanNM['Confirmed Cases'].max() / 50.0) * 50.0) + 150

nmFig = px.choropleth_mapbox(cleanNM, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'purp_r', range_color = (0,maxNM),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.5, center = {"lat": 34.481461, "lon": -106.059789},
                             opacity = 0.7, labels = {"County": "County"})

nmFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
nmFig.update_layout(margin={"r":100,"t":0,"l":100,"b":0})
nmFig.show()

#---------------------------NEVADA CHOROPLETH MAP-----------------------------#
nvDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_nvNews.csv', dtype = {'fips':str})
cleanNV = nvDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxNV = (math.ceil(cleanNV['Confirmed Cases'].max() / 50.0) * 50.0) + 150

nvFig = px.choropleth_mapbox(cleanNV, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'curl', range_color = (0,maxNV),
                             hover_data = ['County', 'Confirmed Cases'],
                             zoom = 5.2, center = {"lat": 38.502032, "lon": -117.023060},
                             opacity = 0.6, labels = {"County": "County"})

nvFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
nvFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
nvFig.show()

#---------------------------NEW YORK CHOROPLETH MAP-----------------------------#
nyDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_nydoh.csv', dtype = {'fips':str})
cleanNY = nyDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxNY = (math.ceil(cleanNY['Confirmed Cases'].max() / 50.0) * 50.0) + 150

nyFig = px.choropleth_mapbox(cleanNY, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'geyser', range_color = (0,maxNY),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths','Recoveries'],
                             zoom = 5.5, center = {"lat": 42.917153, "lon": -75.519960},
                             opacity = 0.6, labels = {"County": "County"})

nyFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
nyFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
nyFig.show()

#---------------------------OHIO CHOROPLETH MAP-----------------------------#
ohDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ohWiki.csv', dtype = {'fips':str})
cleanOH = ohDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxOH = (math.ceil(cleanOH['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ohFig = px.choropleth_mapbox(cleanOH, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'tealrose', range_color = (0,maxOH),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 6, center = {"lat": 40.300325, "lon": -82.700806},
                             opacity = 0.6, labels = {"County": "County"})

ohFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
ohFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
ohFig.show()

#---------------------------OKLAHOMA CHOROPLETH MAP-----------------------------#
okDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_okdoh.csv', dtype = {'fips':str})
cleanOK = okDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxOK = (math.ceil(cleanOK['Confirmed Cases'].max() / 50.0) * 50.0) + 150

okFig = px.choropleth_mapbox(cleanOK, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'haline', range_color = (0,maxOK),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom = 5.8, center = {"lat": 35.732412, "lon": -97.386798},
                             opacity = 0.6, labels = {"County": "County"})

okFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
okFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
okFig.show()

#---------------------------OREGON CHOROPLETH MAP-----------------------------#
orDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ordoh.csv', dtype = {'fips':str})
cleanOR = orDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxOR = (math.ceil(cleanOR['Confirmed Cases'].max() / 50.0) * 50.0) + 150

orFig = px.choropleth_mapbox(cleanOR, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'redor', range_color = (0,maxOR),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.5, center = {"lat": 43.940439, "lon": -120.605284},
                             opacity = 0.6, labels = {"County": "County"})

orFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
orFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
orFig.show()

#---------------------------PENNSYLVANIA CHOROPLETH MAP-----------------------------#
paDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_padoh.csv', dtype = {'fips':str})
cleanPA = paDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxPA = (math.ceil(cleanPA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

paFig = px.choropleth_mapbox(cleanPA, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'sunset', range_color = (0,maxPA),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 5.8, center = {"lat": 40.896699, "lon": -77.838908},
                             opacity = 0.6, labels = {"County": "County"})

paFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
paFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
paFig.show()

##---------------------------PUERTO RICO CHOROPLETH MAP-----------------------------#
#prDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_prWiki.csv',encoding = 'ISO-8859-1', dtype={'fips':str})
#prDF.head()
##Used to round up to a proper max for the range_color function
#maxPR = (math.ceil(prDF['Confirmed Cases'].max() / 50.0) * 50.0) + 150
#
#prFig = px.choropleth_mapbox(prDF, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
#                             color_continuous_scale = 'tropic', range_color = (0,maxPR),
#                             hover_data = ['County', 'Confirmed Cases'],
#                             zoom = 7, center = {"lat": 18.215691, "lon": -66.414655},
#                             opacity = 0.6, labels = {"County": "Region"})
#
#prFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
#prFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#prFig.show()

#-----------------------RHODE ISLAND CHOROPLETH MAP----------------------------#
riDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_riNews.csv', dtype = {'fips':str})
cleanRI = riDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxRI = (math.ceil(cleanRI['Confirmed Cases'].max() / 50.0) * 50.0) + 150

riFig = px.choropleth_mapbox(cleanRI, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'phase', range_color = (0,maxRI),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 8, center = {"lat": 41.640049, "lon": -71.524728},
                             opacity = 0.6, labels = {"County": "County"})

riFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
riFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
riFig.show()

#-----------------------SOUTH CAROLINA CHOROPLETH MAP----------------------------#
scDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_scWiki.csv', dtype = {'fips':str})
cleanSC = scDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxSC = (math.ceil(cleanSC['Confirmed Cases'].max() / 50.0) * 50.0) + 150

scFig = px.choropleth_mapbox(cleanSC, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'tealgrn', range_color = (0,maxSC),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths'],
                             zoom = 6.1, center = {"lat": 33.877856, "lon": -80.864605},
                             opacity = 0.6, labels = {"County": "County"})

scFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
scFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
scFig.show()

#-----------------------SOUTH DAKOTA CHOROPLETH MAP----------------------------#
sdDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_sddoh.csv', dtype = {'fips':str})
cleanSD = sdDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxSD = (math.ceil(cleanSD['Confirmed Cases'].max() / 50.0) * 50.0) + 150

sdFig = px.choropleth_mapbox(cleanSD, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'cividis', range_color = (0,maxSD),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries', 'Hospitalization'],
                             zoom = 5.5, center = {"lat": 44.576328, "lon": -100.291920},
                             opacity = 0.6, labels = {"County": "County"})

sdFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
sdFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
sdFig.show()

#-----------------------TENNESSEE CHOROPLETH MAP----------------------------#
tnDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_tnWiki.csv', dtype = {'fips':str})
cleanTN = tnDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxTN = (math.ceil(cleanTN['Confirmed Cases'].max() / 50.0) * 50.0) + 150

tnFig = px.choropleth_mapbox(cleanTN, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'matter', range_color = (0,maxTN),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom = 6, center = {"lat": 35.866924, "lon": -85.881291},
                             opacity = 0.6, labels = {"County": "County"})

tnFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
tnFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
tnFig.show()

#-----------------------TEXAS CHOROPLETH MAP----------------------------#
txDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_txgit.csv', dtype = {'fips':str})
cleanTX = txDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxTX = (math.ceil(cleanTX['Confirmed Cases'].max() / 50.0) * 50.0) + 150

txFig = px.choropleth_mapbox(cleanTX, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'agsunset', range_color = (0,maxTX),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom = 4.5, center = {"lat": 31.364552, "lon": -99.161239},
                             opacity = 0.6, labels = {"County": "County"})

txFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
txFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
txFig.show()

#-----------------------UTAH CHOROPLETH MAP----------------------------#
utDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_utNews.csv', dtype = {'fips':str})
cleanUT = utDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxUT = (math.ceil(cleanUT['Confirmed Cases'].max() / 50.0) * 50.0) + 150

utFig = px.choropleth_mapbox(cleanUT, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'tealrose', range_color = (0,maxUT),
                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries', 'Hospitalizations'],
                             zoom = 5.4, center = {"lat": 39.323777, "lon": -111.678222},
                             opacity = 0.6, labels = {"County": "County"})

utFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
utFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
utFig.show()

#-----------------------VIRGINIA CHOROPLETH MAP----------------------------#
vaDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_vaWiki.csv', dtype = {'fips':str})
cleanVA = vaDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxVA = (math.ceil(cleanVA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

vaFig = px.choropleth_mapbox(cleanVA, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'matter', range_color = (0,maxVA),
                             hover_data = ['County', 'Confirmed Cases','Deaths'],
                             zoom = 5.5, center = {"lat": 37.510857, "lon": -78.666367},
                             opacity = 0.6, labels = {"County": "County"})

vaFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
vaFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
vaFig.show()

#-----------------------VERMONT CHOROPLETH MAP----------------------------#
vtDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_vtWiki.csv', dtype = {'fips':str})
cleanVT = vtDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxVT = (math.ceil(cleanVT['Confirmed Cases'].max() / 50.0) * 50.0) + 150

vtFig = px.choropleth_mapbox(cleanVT, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'purp', range_color = (0,maxVT),
                             hover_data = ['County', 'Confirmed Cases','Deaths'],
                             zoom = 6.5, center = {"lat": 44.075207, "lon": -72.735624},
                             opacity = 0.6, labels = {"County": "County"})

vtFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
vtFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
vtFig.show()

#-----------------------WASHINGTON CHOROPLETH MAP----------------------------#
waDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_waWiki.csv', dtype = {'fips':str})
cleanWA = waDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxWA = (math.ceil(cleanWA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

waFig = px.choropleth_mapbox(cleanWA, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'temps', range_color = (0,maxWA),
                             hover_data = ['County', 'Confirmed Cases','Deaths'],
                             zoom = 5.5, center = {"lat": 47.572970, "lon": -120.320940},
                             opacity = 0.65, labels = {"County": "County"})

waFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
waFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
waFig.show()

#-----------------------WISCONSIN CHOROPLETH MAP----------------------------#
wiDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_widoh.csv', dtype = {'fips':str})
cleanWI = wiDF.fillna(0)
#Used to round up to a proper max for the range_color function
maxWI = (math.ceil(cleanWI['Confirmed Cases'].max() / 50.0) * 50.0) + 150

wiFig = px.choropleth_mapbox(cleanWI, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'tropic', range_color = (0,maxWI),
                             hover_data = ['County', 'Confirmed Cases','Deaths'],
                             zoom = 5.6, center = {"lat": 44.672245, "lon": -89.878727},
                             opacity = 0.6, labels = {"County": "County"})

wiFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
wiFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
wiFig.show()

#-----------------------WEST VIRGINIA CHOROPLETH MAP----------------------------#
wvDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_wvdoh.csv', dtype = {'fips':str})
cleanWV = wvDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxWV = (math.ceil(cleanWV['Confirmed Cases'].max() / 50.0) * 50.0) + 150

wvFig = px.choropleth_mapbox(cleanWV, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'thermal_r', range_color = (0,maxWV),
                             hover_data = ['County', 'Confirmed Cases','Deaths'],
                             zoom = 6, center = {"lat": 38.718442, "lon": -80.735224},
                             opacity = 0.7, labels = {"County": "County"})

wvFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
wvFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
wvFig.show()


#-----------------------WYOMING CHOROPLETH MAP----------------------------#
wyDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_wyWiki.csv', dtype = {'fips':str})
cleanWY = wyDF.fillna(0)

#Used to round up to a proper max for the range_color function
maxWY = (math.ceil(cleanWY['Confirmed Cases'].max() / 50.0) * 50.0) + 150

wyFig = px.choropleth_mapbox(cleanWY, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
                             color_continuous_scale = 'mygbm', range_color = (0,maxWY),
                             hover_data = ['County', 'Confirmed Cases','Deaths'],
                             zoom = 5.5, center = {"lat": 42.999627, "lon": -107.551451},
                             opacity = 0.6, labels = {"County": "County"})

wyFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk')
wyFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
wyFig.show()
