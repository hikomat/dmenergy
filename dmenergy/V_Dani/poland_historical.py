# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:09:24 2015

@author: Vasinger
"""
import urllib
import csv
from datetime import date
from dateutil.rrule import rrule, DAILY


start_date = date(2004, 1,1)
end_date = date(2015, 1,3)

outfilename = "temp.csv"

for dt in rrule(DAILY, dtstart=start_date, until=end_date):
    filename=dt.strftime("%Y-%m-%d")+".csv"
    
    url_of_file = "http://www.pse.pl/modules/cenyKSE/okres_csv.php?odkiedy="+dt.strftime("%Y-%m-%d")+"&dokiedy="+dt.strftime("%Y-%m-%d")+"&CSV=Get+file"
    urllib.request.urlretrieve(url_of_file, outfilename)     
    with open(outfilename, 'r') as f: 
        reader = csv.reader(f, delimiter = ";")
        with open(filename,'w') as f1:
            next(f)
            for row in reader:
                datum,ora,perc,fogyasztas=row
                if (perc == "0"):
                    perc= "00"
                if (len(ora)<2):
                    ora="0"+ora
                d = datum  +" "+ora+":"+perc
                row = d+" "+fogyasztas
                f1.write(row+'\n')

