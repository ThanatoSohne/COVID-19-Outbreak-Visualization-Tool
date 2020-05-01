import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px
import math
import random as r


# ----------------------Variables and Plots Held Here----------------------------------------------#
# Dropdown menu options for state maps on page 2
states = [{'label': 'Alaska', 'value': 'AK'},
          {'label': 'Alabama', 'value': 'AL'},
          {'label': 'Arkansas', 'value': 'AR'},
          {'label': 'Arizona', 'value': 'AZ'},
          {'label': 'California', 'value': 'CA'},
          {'label': 'Colorado', 'value': 'CO'},
          {'label': 'Connecticut', 'value': 'CT'},
          {'label': 'Delaware', 'value': 'DE'},
          {'label': 'Florida', 'value': 'FL'},
          {'label': 'Georgia', 'value': 'GA'},
          {'label': 'Hawai\'i', 'value': 'HI'},
          {'label': 'Idaho', 'value': 'ID'},
          {'label': 'Illinois', 'value': 'IL'},
          {'label': 'Indiana', 'value': 'IN'},
          {'label': 'Iowa', 'value': 'IO'},
          {'label': 'Kansas', 'value': 'KA'},
          {'label': 'Kentucky', 'value': 'KY'},
          {'label': 'Louisiana', 'value': 'LA'},
          {'label': 'Massachusetts', 'value': 'MA'},
          {'label': 'Maryland', 'value': 'MD'},
          {'label': 'Maine', 'value': 'ME'},
          {'label': 'Michigan', 'value': 'MI'},
          {'label': 'Minnesota', 'value': 'MN'},
          {'label': 'Missouri', 'value': 'MO'},
          {'label': 'Mississippi', 'value': 'MS'},
          {'label': 'Montana', 'value': 'MT'},
          {'label': 'North Carolina', 'value': 'NC'},
          {'label': 'North Dakota', 'value': 'ND'},
          {'label': 'Nebraska', 'value': 'NE'},
          {'label': 'New Hampshire', 'value': 'NH'},
          {'label': 'New Jersey', 'value': 'NJ'},
          {'label': 'New Mexico', 'value': 'NM'},
          {'label': 'Nevada', 'value': 'NV'},
          {'label': 'New York', 'value': 'NY'},
          {'label': 'Ohio', 'value': 'OH'},
          {'label': 'Oklahoma', 'value': 'OK'},
          {'label': 'Oregon', 'value': 'OR'},
          {'label': 'Pennsylvania', 'value': 'PA'},
          {'label': 'Rhode Island', 'value': 'RI'},
          {'label': 'South Carolina', 'value': 'SC'},
          {'label': 'South Dakota', 'value': 'SD'},
          {'label': 'Tennessee', 'value': 'TN'},
          {'label': 'Texas', 'value': 'TX'},
          {'label': 'Utah', 'value': 'UT'},
          {'label': 'Virginia', 'value': 'VA'},
          {'label': 'Vermont', 'value': 'VT'},
          {'label': 'Washington', 'value': 'WA'},
          {'label': 'Wisconsin', 'value': 'WI'},
          {'label': 'West Virginia', 'value': 'WV'},
          {'label': 'Wyoming', 'value': 'WY'},
          ]

# Pull fips codes for accompanying county/state maps

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# ---------------------------WORLD SCATTER GEO MAP----------------------------#
df = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/COVID-19_world_cases_bnoNews.csv')
# df.head()
# Create options for users to change the projection of the map

country = df['Country'].tolist()
cases = df['Cases'].tolist()
deaths = df['Deaths'].tolist()
hope = df['Recovered'].tolist()

geofig = px.scatter_geo(df, lat="Latitude", lon="Longitude", color="Cases",
                        hover_data=["Cases", "New Cases", "Deaths", "New Deaths", "Serious & Critical", "Recovered"],
                        hover_name="Country", color_continuous_scale="balance",
                        size="Cases", projection="orthographic", text="Country",
                        opacity=0.5, size_max=70)
geofig.update_layout(height=400, margin={"r": 0, "t": 0, "l": 0, "b": 0})

# -------------------------ALASKA CHOROPLETH MAP------------------------------#
akDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_akWiki.csv',
    dtype={'fips': str})
cleanAK = akDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxAK = (math.ceil(cleanAK['Confirmed Cases'].max() / 50.0) * 50.0) + 150

akFig = px.choropleth_mapbox(cleanAK, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='aggrnyl',
                             range_color=(0, maxAK),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries', 'Latitude', 'Longitude'],
                             zoom=3, center={"lat": 63.860036, "lon": -150.255849},
                             opacity=0.6, labels={'County': 'Borough', 'Confirmed Cases': 'Confirmed Cases'})

akFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
akFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -------------------------ALABAMA CHOROPLETH MAP------------------------------#
alDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_aldoh.csv',
    dtype={'fips': str})
cleanAL = alDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxAL = (math.ceil(cleanAL['Confirmed Cases'].max() / 50.0) * 50.0) + 150

# Leaving this here in case we will need it later
# alfips = ['01001','01003','01005','01007','01009','01011','01013','01015','01017','01019','01021','01023','01025','01027','01029',
#          '01031','01033','01035','01037','01039','01041','01043','01045','01047','01049','01051','01053','01055','01057','01059',
#          '01061','01063','01065','01067','01069','01071','01073','01075','01077','01079','01081','01083','01085','01087','01089',
#          '01091','01093','01095','01097','01099','01101','01103','01105','01107','01109','01111','01113','01117','01115','01119',
#          '01121','01123','01125','01127','01129','01131','01133']

alFig = px.choropleth_mapbox(cleanAL, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale="viridis",
                             range_color=(0, maxAL),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Latitude', 'Longitude'],
                             zoom=5.5, center={"lat": 32.756902, "lon": -86.844513},
                             opacity=0.6, labels={'Confirmed Cases': 'Confirmed Cases'}
                             )

alFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
alFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -------------------------ARKANSAS CHOROPLETH MAP------------------------------#

arDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_arWiki.csv',
    dtype={'fips': str})
cleanAR = arDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxAR = (math.ceil(cleanAR['Confirmed Cases'].max() / 50.0) * 50.0) + 150

arFig = px.choropleth_mapbox(cleanAR, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='sunsetdark', range_color=(0, maxAR),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=5.5, center={"lat": 34.899764, "lon": -92.439213},
                             opacity=0.6, labels={"County": "County"})

arFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
arFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -------------------------ARIZONA CHOROPLETH MAP------------------------------#
azDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_azWiki.csv',
    dtype={'fips': str})
cleanAZ = azDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxAZ = (math.ceil(cleanAZ['Confirmed Cases'].max() / 50.0) * 50.0) + 150

azFig = px.choropleth_mapbox(cleanAZ, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='picnic', range_color=(0, maxAZ),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.5, center={"lat": 34.333217, "lon": -111.712983},
                             opacity=0.6, labels={"County": "County"})

azFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
azFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -------------------------CALIFORNIA CHOROPLETH MAP------------------------------#
caDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_caWiki.csv',
    dtype={'fips': str})
cleanCA = caDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxCA = (math.ceil(caDF['Confirmed Cases'].max() / 50.0) * 50.0) + 150

caFig = px.choropleth_mapbox(caDF, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='mrybm', range_color=(0, maxCA),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=4.5, center={"lat": 37.863942, "lon": -120.753667},
                             opacity=0.6, labels={"County": "County"},
                             )

caFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
caFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
caFig.update_geos(fitbounds="locations")
caFig.update_layout(
    title="COVID-19's Impact in California",
)
# -------------------------COLORADO CHOROPLETH MAP------------------------------#
coDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_coDOH.csv',
    dtype={'fips': str})
cleanCO = coDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxCO = (math.ceil(cleanCO['Confirmed Cases'].max() / 50.0) * 50.0) + 150

coFig = px.choropleth_mapbox(cleanCO, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='mint', range_color=(0, maxCO),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5, center={"lat": 39.055183, "lon": -105.547831},
                             opacity=0.6, labels={"County": "County"})

coFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
coFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
coFig.update_layout(title=(("Impact of COVID-19 in Arizona" + "\n"
                            + "Unknown or pending: " + str(cleanCO.loc[56, 'Confirmed Cases']) + " Cases" + ", "
                            + str(cleanCO.loc[56, 'Confirmed Cases']) + " Deaths" + "\n"
                            + "Out of State: " + str(cleanCO.loc[57, 'Confirmed Cases']) + " Cases" + ", "
                            + str(cleanCO.loc[57, 'Confirmed Cases']) + " Deaths")))
# -------------------------CONNECTICUT CHOROPLETH MAP------------------------------#
ctDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ctNews.csv',
    dtype={'fips': str})
cleanCT = ctDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxCT = (math.ceil(cleanCT['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ctFig = px.choropleth_mapbox(cleanCT, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='curl_r', range_color=(0, maxCT),
                             hover_data=['County', 'Confirmed Cases'],
                             zoom=6.5, center={"lat": 41.647811, "lon": -72.641075},
                             opacity=0.6, labels={"County": "County"})

ctFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
ctFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -------------------------DELAWARE CHOROPLETH MAP------------------------------#
deDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_deWiki.csv',
    dtype={'fips': str})
cleanDE = deDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxDE = (math.ceil(cleanDE['Confirmed Cases'].max() / 50.0) * 50.0) + 150

deFig = px.choropleth_mapbox(cleanDE, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='geyser', range_color=(0, maxDE),
                             hover_data=['County', 'Confirmed Cases'],
                             zoom=7.1, center={"lat": 39.051475, "lon": -75.416010},
                             opacity=0.6, labels={"County": "County"})

deFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
deFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -------------------------FLORIDA CHOROPLETH MAP------------------------------#
flDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_flWiki.csv',
    dtype={'fips': str})
cleanFL = flDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxFL = (math.ceil(cleanFL['Confirmed Cases'].max() / 50.0) * 50.0) + 150

flFig = px.choropleth_mapbox(cleanFL, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='sunset', range_color=(0, maxFL),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=5.2, center={"lat": 28.311684, "lon": -81.446706},
                             opacity=0.6, labels={"County": "County"})

flFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
flFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -------------------------GEORGIA CHOROPLETH MAP------------------------------#
gaDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_gadoh.csv',
    dtype={'fips': str})
cleanGA = gaDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxGA = (math.ceil(cleanGA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

gaFig = px.choropleth_mapbox(cleanGA, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='teal', range_color=(0, maxGA),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.5, center={"lat": 32.699989, "lon": -83.427133},
                             opacity=0.6, labels={"County": "County"})

gaFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
gaFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
##-------------------------GUAM/ MP CHOROPLETH MAP------------------------------#
# guMP = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_gu_mp_Wiki.csv')
# cleanGM = guMP.fillna(0)
#
##Used to round up to a proper max for the range_color function
# maxGM = (math.ceil(cleanGM['Confirmed Cases'].max() / 50.0) * 50.0) + 150
#
# gmFig = px.choropleth_mapbox(cleanGM, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
#                             color_continuous_scale = 'tropic', range_color = (0,maxGM),
#                             hover_data = ['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
#                             zoom = 5, center = {"lat": 14.272591, "lon": 145.346504},
#                             opacity = 0.6, labels = {"County": "Territory"})
#
# gmFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
# gmFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# gmFig.show()
# -------------------------HAWAI'I CHOROPLETH MAP------------------------------#
hiDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_hidoh.csv',
    dtype={'fips': str})
cleanHI = hiDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxHI = (math.ceil(cleanHI['Total Cases'].max() / 50.0) * 50.0) + 150

hiFig = px.choropleth_mapbox(cleanHI, geojson=counties, locations='fips', color='Total Cases',
                             color_continuous_scale='magma_r', range_color=(0, maxHI),
                             hover_data=['County', 'Total Cases', 'Deaths', 'Released from Isolation',
                                         'Hospitalization'],
                             zoom=5.7, center={"lat": 20.906635, "lon": -157.027297},
                             opacity=0.6, labels={"County": "County"})

hiFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
hiFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------IDAHO CHOROPLETH MAP------------------------------#
idDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_idWiki.csv',
    dtype={'fips': str})
cleanID = idDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxID = (math.ceil(cleanID['Confirmed Cases'].max() / 50.0) * 50.0) + 150

idFig = px.choropleth_mapbox(cleanID, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='plotly3', range_color=(0, maxID),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=4.9, center={"lat": 45.570854, "lon": -115.131137},
                             opacity=0.55, labels={"County": "County"})

idFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
idFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------ILLINOIS CHOROPLETH MAP------------------------------#
ilDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ilWiki.csv',
    dtype={'fips': str})
cleanIL = ilDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxIL = (math.ceil(cleanIL['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ilFig = px.choropleth_mapbox(cleanIL, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='plasma_r', range_color=(0, maxIL),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=5.3, center={"lat": 40.0190, "lon": -88.3000},
                             opacity=0.6, labels={"County": "County"})

ilFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
ilFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------INDIANA CHOROPLETH MAP------------------------------#
inDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_inWiki.csv',
    dtype={'fips': str})
cleanIN = inDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxIN = (math.ceil(cleanIN['Confirmed Cases'].max() / 50.0) * 50.0) + 150

inFig = px.choropleth_mapbox(cleanIN, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='ylgnbu', range_color=(0, maxIN),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.4, center={"lat": 40.013050, "lon": -86.208909},
                             opacity=0.6, labels={"County": "County"})

inFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
inFig.update_layout(margin={"r": 100, "t": 0, "l": 100, "b": 0})
# ---------------------------IOWA CHOROPLETH MAP------------------------------#
ioDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ioWiki.csv',
    dtype={'fips': str})
cleanIO = ioDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxIO = (math.ceil(cleanIO['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ioFig = px.choropleth_mapbox(cleanIO, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='rdpu', range_color=(0, maxIO),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.3, center={"lat": 42.074622, "lon": -93.500036},
                             opacity=0.6, labels={"County": "County"})

ioFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
ioFig.update_layout(margin={"r": 100, "t": 0, "l": 100, "b": 0})
# ---------------------------KANSAS CHOROPLETH MAP------------------------------#
kaDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_kaWiki.csv',
    dtype={'fips': str})
cleanKA = kaDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxKA = (math.ceil(cleanKA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

kaFig = px.choropleth_mapbox(cleanKA, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='darkmint', range_color=(0, maxKA),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.4, center={"lat": 38.541749, "lon": -98.428791},
                             opacity=0.6, labels={"County": "County"})

kaFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
kaFig.update_layout(margin={"r": 100, "t": 0, "l": 100, "b": 0})
# ---------------------------KENTUCKY CHOROPLETH MAP------------------------------#
kyDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_kyNews.csv',
    dtype={'fips': str})
cleanKY = kyDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxKY = (math.ceil(cleanKY['Confirmed Cases'].max() / 50.0) * 50.0) + 150

kyFig = px.choropleth_mapbox(cleanKY, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='twilight', range_color=(0, maxKY),
                             color_continuous_midpoint=maxKY / 2,
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.5, center={"lat": 37.526671, "lon": -85.290470},
                             opacity=0.6, labels={"County": "County"})

kyFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
kyFig.update_layout(margin={"r": 90, "t": 0, "l": 90, "b": 0})
# ---------------------------LOUISIANA CHOROPLETH MAP------------------------------#
laDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_laWiki.csv',
    dtype={'fips': str})
cleanLA = laDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxLA = (math.ceil(cleanLA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

laFig = px.choropleth_mapbox(cleanLA, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='bluyl', range_color=(0, maxLA),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.6, center={"lat": 31.220691, "lon": -92.381019},
                             opacity=0.6, labels={"County": "Parish"})

laFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
laFig.update_layout(margin={"r": 100, "t": 0, "l": 100, "b": 0})
# ---------------------------MASSACHUSETTS CHOROPLETH MAP------------------------------#
maDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_maNews.csv',
    dtype={'fips': str})
cleanMA = maDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxMA = (math.ceil(cleanMA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

maFig = px.choropleth_mapbox(cleanMA, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='brwnyl', range_color=(0, maxMA),
                             hover_data=['County', 'Confirmed Cases'],
                             zoom=6.3, center={"lat": 42.357952, "lon": -72.062769},
                             opacity=0.6, labels={"County": "County"})

maFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
maFig.update_layout(margin={"r": 0, "t": 90, "l": 90, "b": 0})
# ---------------------------MARYLAND CHOROPLETH MAP------------------------------#
mdDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_mdWiki.csv',
    dtype={'fips': str})
cleanMD = mdDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxMD = (math.ceil(cleanMD['Confirmed Cases'].max() / 50.0) * 50.0) + 150

mdFig = px.choropleth_mapbox(cleanMD, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='purpor', range_color=(0, maxMD),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=6.4, center={"lat": 39.026261, "lon": -76.808917},
                             opacity=0.6, labels={"County": "County"})

mdFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
mdFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------MAINE CHOROPLETH MAP------------------------------#
meDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_meDDS.csv',
    dtype={'fips': str})
cleanME = meDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxME = (math.ceil(cleanME['Confirmed Cases'].max() / 50.0) * 50.0) + 150

meFig = px.choropleth_mapbox(cleanME, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='emrld', range_color=(0, maxME),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=5.6, center={"lat": 45.274323, "lon": -69.202765},
                             opacity=0.6, labels={"County": "County"})

meFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
meFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------MICHIGAN CHOROPLETH MAP------------------------------#
miDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_midoh.csv',
    dtype={'fips': str})
cleanMI = miDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxMI = (math.ceil(cleanMI['Confirmed Cases'].max() / 50.0) * 50.0) + 150

miFig = px.choropleth_mapbox(cleanMI, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='spectral_r', range_color=(0, maxMI),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.4, center={"lat": 44.488022, "lon": -84.746015},
                             opacity=0.6, labels={"County": "County"})

miFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
miFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------MINNESOTA CHOROPLETH MAP------------------------------#
mnDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_mndoh.csv',
    dtype={'fips': str})
cleanMN = mnDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxMN = (math.ceil(cleanMN['Confirmed Cases'].max() / 50.0) * 50.0) + 150

mnFig = px.choropleth_mapbox(cleanMN, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='tealgrn_r', range_color=(0, maxMN),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.2, center={"lat": 46.441920, "lon": -93.361527},
                             opacity=0.6, labels={"County": "County"})

mnFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
mnFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------MISSOURI CHOROPLETH MAP------------------------------#
moDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_modoh.csv',
    dtype={'fips': str})
cleanMO = moDF.fillna(0)
aggrr = {'Confirmed Cases': 'sum', 'Deaths': 'sum', 'County': 'first', 'fips': 'first'}
realness = cleanMO.groupby(['County']).aggregate(aggrr)

# Used to round up to a proper max for the range_color function
maxMO = (math.ceil(cleanMO['Confirmed Cases'].max() / 50.0) * 50.0) + 150

moFig = px.choropleth_mapbox(realness, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='temps', range_color=(0, maxMO),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.5, center={"lat": 38.462767, "lon": -92.574534},
                             opacity=0.6, labels={"County": "County"})

moFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
moFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------MISSISSIPPI CHOROPLETH MAP------------------------------#
msDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_msdoh.csv',
    dtype={'fips': str})
cleanMS = msDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxMS = (math.ceil(cleanMS['Confirmed Cases'].max() / 50.0) * 50.0) + 150

msFig = px.choropleth_mapbox(cleanMS, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='balance', range_color=(0, maxMS),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.5, center={"lat": 32.940921, "lon": -89.702028},
                             opacity=0.6, labels={"County": "County"})

msFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
msFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------MONTANA CHOROPLETH MAP------------------------------#
mtDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_mtdoh.csv',
    dtype={'fips': str})
cleanMT = mtDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxMT = (math.ceil(cleanMT['Confirmed Cases'].max() / 50.0) * 50.0) + 150

mtFig = px.choropleth_mapbox(cleanMT, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='sunset_r', range_color=(0, maxMT),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5, center={"lat": 47.072205, "lon": -109.398931},
                             opacity=0.6, labels={"County": "County"})

mtFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
mtFig.update_layout(margin={"r": 0, "t": 100, "l": 0, "b": 0})
# ---------------------------NORTH CAROLINA CHOROPLETH MAP------------------------------#
ncDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ncdoh.csv',
    dtype={'fips': str})
cleanNC = ncDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxNC = (math.ceil(cleanNC['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ncFig = px.choropleth_mapbox(cleanNC, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='delta', range_color=(0, maxNC),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.5, center={"lat": 35.591409, "lon": -78.979338},
                             opacity=0.7, labels={"County": "County"})

ncFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
ncFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------NORTH DAKOTA CHOROPLETH MAP------------------------------#
ndDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ndWiki.csv',
    dtype={'fips': str})
cleanNA = ndDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxND = (math.ceil(cleanNA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ndFig = px.choropleth_mapbox(cleanNA, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='tealrose', range_color=(0, maxND),
                             hover_data=['County', 'Confirmed Cases'],
                             zoom=5.7, center={"lat": 47.528438, "lon": -100.445038},
                             opacity=0.6, labels={"County": "County"})

ndFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
ndFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------NEBRASKA CHOROPLETH MAP------------------------------#
neDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_neWiki.csv',
    dtype={'fips': str})
cleanNE = neDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxNE = (math.ceil(cleanNE['Confirmed Cases'].max() / 50.0) * 50.0) + 150

neFig = px.choropleth_mapbox(cleanNE, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='teal', range_color=(0, maxNE),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.7, center={"lat": 41.527111, "lon": -99.810728},
                             opacity=0.6, labels={"County": "County"})

neFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
neFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------NEW HAMPSHIRE CHOROPLETH MAP-----------------------------#
nhDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_nhNews.csv',
    dtype={'fips': str})
cleanNH = nhDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxNH = (math.ceil(cleanNH['Confirmed Cases'].max() / 50.0) * 50.0) + 150

nhFig = px.choropleth_mapbox(cleanNH, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='phase', range_color=(0, maxNH),
                             hover_data=['County', 'Confirmed Cases'],
                             zoom=6, center={"lat": 43.989517, "lon": -71.469112},
                             opacity=0.6, labels={"County": "County"})

nhFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
nhFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------NEW JERSEY CHOROPLETH MAP-----------------------------#
njDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_njWiki.csv',
    dtype={'fips': str})
cleanNJ = njDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxNJ = (math.ceil(cleanNJ['Confirmed Cases'].max() / 50.0) * 50.0) + 150

njFig = px.choropleth_mapbox(cleanNJ, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='curl', range_color=(0, maxNJ),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=6.2, center={"lat": 40.267895, "lon": -74.412674},
                             opacity=0.6, labels={"County": "County"})

njFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
njFig.update_layout(margin={"r": 100, "t": 0, "l": 100, "b": 0})
# ---------------------------NEW MEXICO CHOROPLETH MAP-----------------------------#
nmDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_nmdoh.csv',
    dtype={'fips': str})
cleanNM = nmDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxNM = (math.ceil(cleanNM['Confirmed Cases'].max() / 50.0) * 50.0) + 150

nmFig = px.choropleth_mapbox(cleanNM, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='purp_r', range_color=(0, maxNM),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.3, center={"lat": 34.481461, "lon": -106.059789},
                             opacity=0.7, labels={"County": "County"})

nmFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
nmFig.update_layout(margin={"r": 100, "t": 0, "l": 100, "b": 0})
# ---------------------------NEVADA CHOROPLETH MAP-----------------------------#
nvDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_nvNews.csv',
    dtype={'fips': str})
cleanNV = nvDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxNV = (math.ceil(cleanNV['Confirmed Cases'].max() / 50.0) * 50.0) + 150

nvFig = px.choropleth_mapbox(cleanNV, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='curl', range_color=(0, maxNV),
                             hover_data=['County', 'Confirmed Cases'],
                             zoom=5, center={"lat": 38.502032, "lon": -117.023060},
                             opacity=0.6, labels={"County": "County"})

nvFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
nvFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------NEW YORK CHOROPLETH MAP-----------------------------#
nyDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_nydoh.csv',
    dtype={'fips': str})
cleanNY = nyDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxNY = (math.ceil(cleanNY['Confirmed Cases'].max() / 50.0) * 50.0) + 150

nyFig = px.choropleth_mapbox(cleanNY, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='geyser', range_color=(0, maxNY),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=5.3, center={"lat": 42.917153, "lon": -75.519960},
                             opacity=0.6, labels={"County": "County"})

nyFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
nyFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------OHIO CHOROPLETH MAP-----------------------------#
ohDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ohWiki.csv',
    dtype={'fips': str})
cleanOH = ohDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxOH = (math.ceil(cleanOH['Confirmed Cases'].max() / 50.0) * 50.0) + 150

ohFig = px.choropleth_mapbox(cleanOH, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='tealrose', range_color=(0, maxOH),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.7, center={"lat": 40.300325, "lon": -82.700806},
                             opacity=0.6, labels={"County": "County"})

ohFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
ohFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------OKLAHOMA CHOROPLETH MAP-----------------------------#
okDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_okdoh.csv',
    dtype={'fips': str})
cleanOK = okDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxOK = (math.ceil(cleanOK['Confirmed Cases'].max() / 50.0) * 50.0) + 150

okFig = px.choropleth_mapbox(cleanOK, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='haline', range_color=(0, maxOK),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=5.5, center={"lat": 35.732412, "lon": -97.386798},
                             opacity=0.6, labels={"County": "County"})

okFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
okFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------OREGON CHOROPLETH MAP-----------------------------#
orDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_ordoh.csv',
    dtype={'fips': str})
cleanOR = orDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxOR = (math.ceil(cleanOR['Confirmed Cases'].max() / 50.0) * 50.0) + 150

orFig = px.choropleth_mapbox(cleanOR, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='redor', range_color=(0, maxOR),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.3, center={"lat": 43.940439, "lon": -120.605284},
                             opacity=0.6, labels={"County": "County"})

orFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
orFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# ---------------------------PENNSYLVANIA CHOROPLETH MAP-----------------------------#
paDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_padoh.csv',
    dtype={'fips': str})
cleanPA = paDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxPA = (math.ceil(cleanPA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

paFig = px.choropleth_mapbox(cleanPA, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='sunset', range_color=(0, maxPA),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.5, center={"lat": 40.896699, "lon": -77.838908},
                             opacity=0.6, labels={"County": "County"})

paFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
paFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
##---------------------------PUERTO RICO CHOROPLETH MAP-----------------------------#
# prDF = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_prWiki.csv',encoding = 'ISO-8859-1', dtype={'fips':str})
# prDF.head()
##Used to round up to a proper max for the range_color function
# maxPR = (math.ceil(prDF['Confirmed Cases'].max() / 50.0) * 50.0) + 150
#
# prFig = px.choropleth_mapbox(prDF, geojson = counties, locations = 'fips', color = 'Confirmed Cases',
#                             color_continuous_scale = 'tropic', range_color = (0,maxPR),
#                             hover_data = ['County', 'Confirmed Cases'],
#                             zoom = 7, center = {"lat": 18.215691, "lon": -66.414655},
#                             opacity = 0.6, labels = {"County": "Region"})
#
# prFig.update_layout(mapbox_style = "satellite-streets", mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
# prFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# prFig.show()

# -----------------------RHODE ISLAND CHOROPLETH MAP----------------------------#
riDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_riNews.csv',
    dtype={'fips': str})
cleanRI = riDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxRI = (math.ceil(cleanRI['Confirmed Cases'].max() / 50.0) * 50.0) + 150

riFig = px.choropleth_mapbox(cleanRI, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='phase', range_color=(0, maxRI),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=7.5, center={"lat": 41.640049, "lon": -71.524728},
                             opacity=0.6, labels={"County": "County"})

riFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
riFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -----------------------SOUTH CAROLINA CHOROPLETH MAP----------------------------#
scDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_scWiki.csv',
    dtype={'fips': str})
cleanSC = scDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxSC = (math.ceil(cleanSC['Confirmed Cases'].max() / 50.0) * 50.0) + 150

scFig = px.choropleth_mapbox(cleanSC, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='tealgrn', range_color=(0, maxSC),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=6, center={"lat": 33.877856, "lon": -80.864605},
                             opacity=0.6, labels={"County": "County"})

scFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
scFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -----------------------SOUTH DAKOTA CHOROPLETH MAP----------------------------#
sdDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_sdWiki.csv',
    dtype={'fips': str})
cleanSD = sdDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxSD = (math.ceil(cleanSD['Confirmed Cases'].max() / 50.0) * 50.0) + 150

sdFig = px.choropleth_mapbox(cleanSD, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='cividis', range_color=(0, maxSD),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=5.3, center={"lat": 44.576328, "lon": -100.291920},
                             opacity=0.6)

sdFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
sdFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -----------------------TENNESSEE CHOROPLETH MAP----------------------------#
tnDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_tnWiki.csv',
    dtype={'fips': str})
cleanTN = tnDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxTN = (math.ceil(cleanTN['Confirmed Cases'].max() / 50.0) * 50.0) + 150

tnFig = px.choropleth_mapbox(cleanTN, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='matter', range_color=(0, maxTN),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=5.7, center={"lat": 35.866924, "lon": -85.881291},
                             opacity=0.6, labels={"County": "County"})

tnFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
tnFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -----------------------TEXAS CHOROPLETH MAP----------------------------#
txDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_txgit.csv',
    dtype={'fips': str})
cleanTX = txDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxTX = (math.ceil(cleanTX['Confirmed Cases'].max() / 50.0) * 50.0) + 150

txFig = px.choropleth_mapbox(cleanTX, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='agsunset', range_color=(0, maxTX),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries'],
                             zoom=4, center={"lat": 31.364552, "lon": -99.161239},
                             opacity=0.6, labels={"County": "County"})

txFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
txFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -----------------------UTAH CHOROPLETH MAP----------------------------#
utDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_utNews.csv',
    dtype={'fips': str})
cleanUT = utDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxUT = (math.ceil(cleanUT['Confirmed Cases'].max() / 50.0) * 50.0) + 150

utFig = px.choropleth_mapbox(cleanUT, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='tealrose', range_color=(0, maxUT),
                             hover_data=['County', 'Confirmed Cases', 'Deaths', 'Recoveries', 'Hospitalizations'],
                             zoom=5.2, center={"lat": 39.323777, "lon": -111.678222},
                             opacity=0.6, labels={"County": "County"})

utFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
utFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -----------------------VIRGINIA CHOROPLETH MAP----------------------------#
vaDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_vaWiki.csv',
    dtype={'fips': str})
cleanVA = vaDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxVA = (math.ceil(cleanVA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

vaFig = px.choropleth_mapbox(cleanVA, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='matter', range_color=(0, maxVA),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.3, center={"lat": 37.510857, "lon": -78.666367},
                             opacity=0.6, labels={"County": "County"})

vaFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
vaFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -----------------------VERMONT CHOROPLETH MAP----------------------------#
vtDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_vtWiki.csv',
    dtype={'fips': str})
cleanVT = vtDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxVT = (math.ceil(cleanVT['Confirmed Cases'].max() / 50.0) * 50.0) + 150

vtFig = px.choropleth_mapbox(cleanVT, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='purp', range_color=(0, maxVT),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=6, center={"lat": 44.075207, "lon": -72.735624},
                             opacity=0.6, labels={"County": "County"})

vtFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
vtFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -----------------------WASHINGTON CHOROPLETH MAP----------------------------#
waDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_waWiki.csv',
    dtype={'fips': str})
cleanWA = waDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxWA = (math.ceil(cleanWA['Confirmed Cases'].max() / 50.0) * 50.0) + 150

waFig = px.choropleth_mapbox(cleanWA, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='temps', range_color=(0, maxWA),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.3, center={"lat": 47.572970, "lon": -120.320940},
                             opacity=0.65, labels={"County": "County"})

waFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
waFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -----------------------WISCONSIN CHOROPLETH MAP----------------------------#
wiDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_widoh.csv',
    dtype={'fips': str})
cleanWI = wiDF.fillna(0)
# Used to round up to a proper max for the range_color function
maxWI = (math.ceil(cleanWI['Confirmed Cases'].max() / 50.0) * 50.0) + 150

wiFig = px.choropleth_mapbox(cleanWI, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='tropic', range_color=(0, maxWI),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.3, center={"lat": 44.672245, "lon": -89.878727},
                             opacity=0.6, labels={"County": "County"})

wiFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
wiFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -----------------------WEST VIRGINIA CHOROPLETH MAP----------------------------#
wvDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_wvWiki.csv',
    dtype={'fips': str})
cleanWV = wvDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxWV = (math.ceil(cleanWV['Confirmed Cases'].max() / 50.0) * 50.0) + 150

wvFig = px.choropleth_mapbox(cleanWV, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='thermal_r', range_color=(0, maxWV),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.5, center={"lat": 38.718442, "lon": -80.735224},
                             opacity=0.7, labels={"County": "County"})

wvFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
wvFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -----------------------WYOMING CHOROPLETH MAP----------------------------#
wyDF = pd.read_csv(
    'https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/Web%20Scrapers/US%20States/COVID-19_cases_wyWiki.csv',
    dtype={'fips': str})
cleanWY = wyDF.fillna(0)

# Used to round up to a proper max for the range_color function
maxWY = (math.ceil(cleanWY['Confirmed Cases'].max() / 50.0) * 50.0) + 150

wyFig = px.choropleth_mapbox(cleanWY, geojson=counties, locations='fips', color='Confirmed Cases',
                             color_continuous_scale='mygbm', range_color=(0, maxWY),
                             hover_data=['County', 'Confirmed Cases', 'Deaths'],
                             zoom=5.2, center={"lat": 42.999627, "lon": -107.551451},
                             opacity=0.6, labels={"County": "County"})

wyFig.update_layout(mapbox_style="satellite-streets",
                    mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOHlpdHo5bjA1dzYzZm5yZGduMTBvZTcifQ.ztpWyjPI2kHzwSbcdYrj7w')
wyFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# -------------------------------------------------------------------------------------------------#

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
app.config.suppress_callback_exceptions = True

CONTENT_STYLE = {
    "margin": "auto",
    "padding": "2rem 1rem",
    "width": "90%"
}

dropdown = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Home", href="/page-1", id="page-1-link"),
                dbc.DropdownMenuItem("US Maps", href="/page-2", id="page-2-link"),
                dbc.DropdownMenuItem("World View", href="/page-3", id="page-3-link"),
                dbc.DropdownMenuItem("Viz", href="/page-4", id="page-4-link"),
                dbc.DropdownMenuItem("3D Viewer", href="/page-5", id="page-5-link"),
                dbc.DropdownMenuItem("Prediction Models", href="/page-6", id="page-6-link"),
            ],
            nav=True,
            in_navbar=True,
            label="Menu",
            direction="right",
            color="info",
        ),
    )
],
    align="right",
)
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(
                                src="/assets/COVID-19 Outbreak visualization tool-shatter.png",
                                height="50px"
                            )
                        ),
                        dbc.Col(
                            dbc.NavbarBrand(
                                "COVID-19 OUTBREAK VISUALIZATION TOOL",
                                className="m1-2"
                            )
                        ),
                    ],
                    align="left",
                    no_gutters=True,

                ),
            ),
            dbc.NavbarToggler(
                id="navbar-toggler"
            ),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown],
                    pills=True,
                    className="m1-auto",
                    navbar=True,
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-6",
)

page1_card1 = [

    dbc.CardHeader("#HelpStopTheSpread", style={'font-family': 'Avantgarde',
                                                'font-variant': 'small-caps'}),
    dbc.CardBody(
        [
            html.H4("Together we can overcome", style={
                'font-family': 'fangsong',
                'text-align': 'center',
                'text-size': '16px'
            }),
            html.P(
                """\
                ~ Remember to wash your hands periodically for at least 20 seconds
                ~ Avoid touching your face as much as possible
                ~ Always keep a good social distance from those around you
                ~ Do these things to save yourself, your loved ones, and those around you""",
                style={
                    'font-family': 'Book Antiqua',
                    'font-size': '12px',
                    'font-style': 'normal'
                }
            ),
        ]
    ),
]

page1_card2 = dbc.CardBody(
    [
        html.Blockquote(
            [
                html.P(
                    """You may encounter many defeats, but you must not be defeated. 
                    In fact, it may be necessary to encounter the defeats, so you can know who you are, 
                    what you can rise from, how you can still come out of it."""
                ),
                html.Footer(
                    html.Small("Maya Angelou", className="text-muted")
                ),
            ],
            className="blockquote",
        )
    ]
)

page1_card3 = [
    dbc.CardImg(src="/assets/Protecting yourself and your loved ones from covid-19.png", top=True),
    dbc.CardBody(
        [
            html.H5("Remember these simple facts", className="card-title")
        ]
    ),
]

page1_card4 = [
    dbc.CardImg(src="/assets/cov.png", top=True),
    dbc.CardBody(
        [
            html.P("Structure of novel coronavirus spike receptor-binding domain complexed with its receptor ACE2",
                   className="card-title")
        ]
    ),
]

page1_card5 = [
    dbc.CardImg(src="/assets/6vxx.png", top=True),
    dbc.CardBody(
        [
            html.P("Structure of the SARS-CoV-2 spike glycoprotein (closed state)", className="card-title")
        ]
    ),
]

page1_card6 = [
    dbc.CardHeader("CDC's COVID-19 Self-Checker", style={'font-family': 'Avantgarde',
                                                         'font-variant': 'small-caps'}),
    dbc.CardBody(
        [
            html.H4("This is simply to help you in deciding whether you need to seek further medical assistance",
                    style={
                        'font-family': 'fangsong',
                        'text-align': 'center',
                        'text-size': '16px'
                    }),
            dbc.Button("CDC Self Checker",
                       color="light",
                       size="lg",
                       external_link= "False",
                       block="True",
                       href="https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/index.html#cdc-chat-bot-open"),
        ]
    ),
]

#This will allow for a bit of shuffling of the home page card system... This way, there is something new or
#different each time the user visits the home page

#card_deck1 will have subsets of proteins images for the user to look at
card_deck1_1 = [page1_card4, page1_card5]
#card_deck2 will have subsets of infographics
card_deck2_1 = [page1_card3]
#card_deck3 will have subsets of motivational quotes, etc.
card_deck3_1 = [page1_card2]
#card_deck4 will have subsets of links for the user to click on
card_deck4_1 = [page1_card6]
#card_deck5 will host cards with information on COVID-19 and how to stay safe
card_deck5_1 = [page1_card1]
colours = ["secondary", "primary", "success", "warning", "danger", "info", "dark"]

mason = dbc.CardColumns(
    [
        dbc.Card(r.choice(card_deck1_1), color=r.choice(colours), inverse=True),
        dbc.Card(page1_card2, body=True),
        dbc.Card(r.choice(card_deck2_1), color=r.choice(colours), inverse=True),
        dbc.Card(r.choice(card_deck3_1), color=r.choice(colours), inverse=True),
        dbc.Card(r.choice(card_deck4_1), color=r.choice(colours), inverse=True),
        dbc.Card(r.choice(card_deck5_1), color=r.choice(colours), inverse=True),
        ###So on and so forth....
    ]
)

us_map = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H3("Mapped Visuals of COVID-19's Virulent Spread Here in the US",
                                        style={
                                            "position": "relative",
                                            "text-align": "center"
                                        }),
                                #                               html.Br(),
                                html.P(
                                    """\
                                        The maps to the right are broken down into a state by state basis, wherein one can see
                                        the overall reach COVID-19 has had within our communities here in the US. Some maps will 
                                        have a few counties missing due to either those counties not having cases or because their
                                        numbers have yet to be reported. All data scraped in order to build these sites come from a 
                                        range of sources that had the most reliable and most current of information.""",
                                    style={'border-style': 'inset'})],
                            md=3,
                            width="auto"
                        ),
                        dbc.Col(
                            [
                                html.H3("US Maps on a State by State Basis"),
                                dcc.Dropdown(
                                    id="map_menu",
                                    options=states,
                                    value="AK"
                                ),
                                dcc.Graph(
                                    id='map',
                                    style={
                                        'width': '60%',
                                        'height': '60%',
                                        'display': 'block',
                                        'position': 'fixed',
                                        'border': '3px solid grey',
                                        'padding': '10px'
                                    }
                                ),
                            ],
                            md=8,
                            width="auto"
                        ),
                    ]
                )
            ]
        )
    ]
)

#
# Place world map html here
#



#
# Place graphs here
#

sarsView = html.Div(
    [
        dbc.Row(
            [
                html.Embed(
                    height="600px",
                    width="600px",
                    src="https://embed.molview.org/v1/?mode=line&pdbid=5RE4&bg=gray&chainType=cylinders&chainBonds=true&chainColor=spectrum"
                ),
            ]
        ),
        dbc.Row(
            [
                html.Embed(
                    height="600px",
                    width="600px",
                    src="https://embed.molview.org/v1/?mode=vdw&pdbid=6LXT&chainType=ribbon&chainColor=residue"
                ),
            ]
        ),

    ]
)


#
# Place  prediction model here
#

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), navbar, content]
)


# we use a callback to toggle the collapse on small screens
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


app.callback(
    Output(f"navbar-collapse", "is_open"),
    [Input(f"navbar-toggler", "n_clicks")],
    [State(f"navbar-collapse", "is_open")],
)(toggle_navbar_collapse)


@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 6)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False
    return [pathname == f"page-{i}" for i in range(1, 6)]


@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return mason
    elif pathname == "/page-2":
        return us_map
    elif pathname == "/page-3":
        return html.P("Page 3.... World Map")
    elif pathname == "/page-4":
        return html.P("Page 4.... Viz")
    elif pathname == "/page-5":
        return sarsView
    elif pathname == "/page-6":
        return html.P("Prediction model")
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P("Pathname {pathname} was not recognized... Oopss..")
        ]
    )


@app.callback(
    Output("map", "figure"),
    [Input("map_menu", "value")]
)
def build_map(value):
    if value == 'AK':
        return akFig
    elif value == 'AL':
        return alFig
    elif value == 'AR':
        return arFig
    elif value == 'AZ':
        return azFig
    elif value == 'CA':
        return caFig
    elif value == 'CO':
        return coFig
    elif value == 'CT':
        return ctFig
    elif value == 'DE':
        return deFig
    elif value == 'FL':
        return flFig
    elif value == 'GA':
        return gaFig
    elif value == 'HI':
        return hiFig
    elif value == 'ID':
        return idFig
    elif value == 'IL':
        return ilFig
    elif value == 'IN':
        return inFig
    elif value == 'IO':
        return ioFig
    elif value == 'KA':
        return kaFig
    elif value == 'KY':
        return kyFig
    elif value == 'LA':
        return laFig
    elif value == 'MA':
        return maFig
    elif value == 'MD':
        return mdFig
    elif value == 'ME':
        return meFig
    elif value == 'MI':
        return miFig
    elif value == 'MN':
        return mnFig
    elif value == 'MO':
        return moFig
    elif value == 'MS':
        return msFig
    elif value == 'MT':
        return mtFig
    elif value == 'NC':
        return ncFig
    elif value == 'ND':
        return ndFig
    elif value == 'NE':
        return neFig
    elif value == 'NH':
        return nhFig
    elif value == 'NJ':
        return njFig
    elif value == 'NM':
        return nmFig
    elif value == 'NV':
        return nvFig
    elif value == 'NY':
        return nyFig
    elif value == 'OH':
        return ohFig
    elif value == 'OK':
        return okFig
    elif value == 'OR':
        return orFig
    elif value == 'PA':
        return paFig
    elif value == 'RI':
        return riFig
    elif value == 'SC':
        return scFig
    elif value == 'SD':
        return sdFig
    elif value == 'TN':
        return tnFig
    elif value == 'TX':
        return txFig
    elif value == 'UT':
        return utFig
    elif value == 'VA':
        return vaFig
    elif value == 'VT':
        return vtFig
    elif value == 'WA':
        return waFig
    elif value == 'WI':
        return wiFig
    elif value == 'WV':
        return wvFig
    elif value == 'WY':
        return wyFig


if __name__ == "__main__":
    app.run_server(port=8050)
