# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:51:40 2015

@author: Vasinger
"""

import urllib
import csv
from datetime import timedelta,datetime

yesterday = datetime.now()- timedelta(days=1)
outfilename = 'temp.txt'

filename=yesterday.strftime("%Y-%m-%d")+".csv"
url_of_file = "http://www.ceps.cz/_layouts/15/Ceps/_Pages/GraphData.aspx?mode=txt&from="+yesterday.strftime("%m/%d/%Y")+"%2012:00:00%20AM&to="+yesterday.strftime("%m/%d/%Y")+"%2011:59:59%20PM&hasinterval=True&sol=1&lang=ENG&agr=MI&fnc=AVG&ver=RT&"    
response = urllib.request.urlopen(url_of_file)
output = open(outfilename,'wb')
output.write(response.read())
output.close()
with open(outfilename, "r",newline='') as infile, open(filename, "w",newline='') as outfile:
    in_txt = csv.reader(infile,delimiter= ";")
    out_csv = csv.writer(outfile)
    i = 0
    for row in in_txt:
        i +=1
        if i>3:
            datum,fogyasztasp,fogyasztas,egyeb=row
            hasznos=datum+" "+fogyasztas            
            outfile.write(str(hasznos)+'\n')