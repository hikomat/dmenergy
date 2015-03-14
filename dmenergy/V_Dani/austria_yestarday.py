# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:11:40 2015

@author: Vasinger
"""

import urllib
from datetime import date
from datetime import timedelta,datetime
import csv

yesterday = datetime.now()- timedelta(days=1)
outfilename = "temp.csv"
start_date = date(2010, 1,1)
end_date = date(2015, 1,3)

filename=yesterday.strftime("%Y-%m-%d")+".csv"
url_of_file = "http://www.apg.at/transparency/Download.aspx?LANGUAGE=en&PID=AL&Format=csv&Resolution=15M&DateFromLocal="+yesterday.strftime("%Y%m%d")+"&DateToLocal="+yesterday.strftime("%Y%m%d")+"&CacheDir=20150313224613_f0159e533ae746d98b6fdde1a7c6cb3d&CacheFileName=export_al_"+yesterday.strftime("%Y-%m-%d")+"T00_00_00Z_"+yesterday.strftime("%d.%m.%Y")+"T23_45_00Z_15M_en.csv"
urllib.request.urlretrieve(url_of_file, outfilename) 
with open(outfilename, 'r') as f: 
    reader = csv.reader(f,delimiter= ",")
    with open(filename,'w') as f1:
        for row in reader:
            datum1,datum2,fogyasztas,egyeb=row
            row=datum1+" "+fogyasztas
            f1.write(str(row)+'\n')

