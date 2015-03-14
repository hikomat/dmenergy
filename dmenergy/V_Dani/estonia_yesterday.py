# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:20:20 2015

@author: Vasinger
"""



import urllib
import csv
from datetime import timedelta,datetime


yesterday = datetime.now()- timedelta(days=1)
outfilename = "temp.csv"

filename=yesterday.strftime("%Y-%m-%d")+".csv"
url_of_file = "http://elering.ee/production-and-consumption-3/?period=date&chart=data_tootmine&tpl=1101&title=Production%20and%20consumption&from="+yesterday.strftime("%d.%m.%Y")+"&to="+yesterday.strftime("%d.%m.%Y")+"&step=&timezone="
urllib.request.urlretrieve(url_of_file, outfilename)  
with open(outfilename, 'r') as f: 
    reader = csv.reader(f,delimiter= ";")
    with open(filename,'w') as f1:
        i = 0
        for row in reader:
            i +=1            
            if i>1:
                datum,eloallitas,fogyasztas,tervezettf,tervezette,tervezettea=row
                row = datum+" "+fogyasztas
                f1.write(str(row)+'\n')