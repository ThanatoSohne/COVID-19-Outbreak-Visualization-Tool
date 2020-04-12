from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
        
df = pd.read_csv('https://raw.githubusercontent.com/ThanatoSohne/COVID-19-Outbreak-Visualization-Tool/master/COVID-19_cases_nydoh.csv')
        
fips = ['36001','36003','36007','36009','36011','36013','36015','36017','36019','36021','36023','36025','36027','36029','36031','36033','36035','36037',
       '36039','36041','36043','36045','36049','36051','36053','36055','36057','36059','36063','36065','36067','36069',
       '36071','36073','36075','36077','36079','36083','36087','36091','36093','36095','36097','36099','36089','36101','36103','36105','36107','36109','36111','36113',
       '36115','36117','36119','36121','36123','36061']

fig = px.choropleth_mapbox(df, geojson=counties, locations=fips, color='Confirmed Cases',
                           color_continuous_scale="IceFire",
                           range_color=(0,25000),
                           hover_data = ['Deaths', 'County', 'Recoveries'],
                           zoom=5, center = {"lat": 43.2994, "lon": -74.2179},
                           opacity=0.6, labels={'Confirmed Cases': 'Confirmed Cases', 'Deaths': 'Deaths', 'Recoveries':'Recoveries'})

fig.update_layout(mapbox_style="satellite", mapbox_accesstoken='pk.eyJ1IjoibGFlc3RyeWdvbmVzIiwiYSI6ImNrOGg2ZGttdjA5M2kzb3J5MGFjYXlnMHgifQ.3G4eulHhTzI335CFMKY10A',)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()