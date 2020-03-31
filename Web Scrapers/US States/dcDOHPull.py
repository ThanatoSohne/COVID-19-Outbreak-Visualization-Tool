from urllib import request
from urllib.request import urlretrieve
import requests
import time

dcFile = "https://coronavirus.dc.gov/sites/default/files/dc/sites/coronavirus/page_content/attachments/COVID19_DCHealthStatisticsDataV2%20%283%29.xlsx"

download = requests.get(dcFile)
download.raise_for_status()

newLife = open('DC-COVID-19.xlsx', 'wb')
for chunk in download.iter_content(100000):
    newLife.write(chunk)



newLife.close()