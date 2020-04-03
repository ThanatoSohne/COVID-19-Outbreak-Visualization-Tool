import pandas as pd
import sys, os, glob
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from apscheduler.schedulers.blocking import BlockingScheduler

os.chdir("C:/Users/Erwac/Desktop/COVID-19/Web Scrapers/US States")

def fusion():

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    
    drive = GoogleDrive(gauth)
    
    extension = 'csv'
    
    alles_COVID = [i for i in glob.glob('COVID-19*.{}'.format(extension))]
    
    #print(alles_COVID)
    
    #combine all files in the list
    verbinden = pd.concat([pd.read_csv(f, encoding = 'ISO-8859-1', error_bad_lines=False, sort=False) for f in alles_COVID])
    #export to csv
    verbinden.to_csv( "COVID-19_COMBINED.csv", index=False, encoding='utf-8-sig')
    
    file1 = drive.CreateFile({"mimeType": "csv"})
    file1.SetContentFile("COVID-19_COMBINED.csv") #just a test to ensure it uploads
    file1.Upload()

planerin = BlockingScheduler()
planerin.add_job(fusion, 'interval', hours=24)
planerin.start()

#, encoding='utf-8-sig'