# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:09:24 2015

@author: Vasinger
"""
import urllib
import csv

from datetime import timedelta,datetime


yesterday = datetime.now()- timedelta(days=1)
outfilename = "temp.csv"

filename=yesterday.strftime("%Y-%m-%d")+".csv"

url_of_file = "http://www.pse.pl/modules/cenyKSE/okres_csv.php?odkiedy="+yesterday.strftime("%Y-%m-%d")+"&dokiedy="+yesterday.strftime("%Y-%m-%d")+"&CSV=Get+file"
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

