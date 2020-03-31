from urllib import request
from urllib.request import urlretrieve
import requests
import time

#Retrieved from Florida's opendata site https://open-fdoh.hub.arcgis.com/datasets/florida-covid19-cases

flFile = "https://opendata.arcgis.com/datasets/a7887f1940b34bf5a02c6f7f27a5cb2c_0.csv?outSR=%7B%22latestWkid%22%3A3087%2C%22wkid%22%3A3087%7D"

download = requests.get(flFile)
download.raise_for_status()

newLife = open('FLCOVID-19.csv', 'wb')
for chunk in download.iter_content(100000):
    newLife.write(chunk)



newLife.close()
