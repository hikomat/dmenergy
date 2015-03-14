# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:51:40 2015

@author: Vasinger
"""

import urllib
import csv
from datetime import date
from dateutil.rrule import rrule, DAILY

start_date = date(2010, 1,1)
end_date = date(2015, 3,12)

outfilename = 'temp.txt'

for dt in rrule(DAILY, dtstart=start_date, until=end_date):
    filename=dt.strftime("%Y-%m-%d")+".csv"
    url_of_file = "http://www.ceps.cz/_layouts/15/Ceps/_Pages/GraphData.aspx?mode=txt&from="+dt.strftime("%d/%m/%Y")+"%2012:00:00%20AM&to="+dt.strftime("%d/%m/%Y")+"%2011:59:59%20PM&hasinterval=True&sol=1&lang=ENG&agr=MI&fnc=AVG&ver=RT&"    
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