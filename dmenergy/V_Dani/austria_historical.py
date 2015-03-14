# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:20:20 2015

@author: Vasinger
"""

import urllib
from datetime import date
from dateutil.rrule import rrule, DAILY
import csv

outfilename = "temp.csv"
start_date = date(2010, 1,1)
end_date = date(2015, 1,3)

for dt in rrule(DAILY, dtstart=start_date, until=end_date):
    filename=dt.strftime("%Y-%m-%d")+".csv"
    url_of_file = "http://www.apg.at/transparency/Download.aspx?LANGUAGE=en&PID=AL&Format=csv&Resolution=15M&DateFromLocal="+dt.strftime("%Y%m%d")+"&DateToLocal="+dt.strftime("%Y%m%d")+"&CacheDir=20150313224613_f0159e533ae746d98b6fdde1a7c6cb3d&CacheFileName=export_al_"+dt.strftime("%Y-%m-%d")+"T00_00_00Z_"+dt.strftime("%d.%m.%Y")+"T23_45_00Z_15M_en.csv"
    urllib.request.urlretrieve(url_of_file, outfilename) 
    with open(outfilename, 'r') as f: 
        reader = csv.reader(f,delimiter= ",")
        with open(filename,'w') as f1:
            for row in reader:
                datum1,datum2,fogyasztas,egyeb=row
                row=datum1+" "+fogyasztas
                f1.write(str(row)+'\n')