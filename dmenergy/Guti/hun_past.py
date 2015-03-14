# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:57:21 2015

@author: Dániel
"""

import xlrd
import csv
import urllib
from datetime import date,datetime,timedelta
from dateutil.rrule import rrule, DAILY

sdate = date(2006, 12, 31)
edate = date(2015, 3, 12)

def Download(url,dest):
    with xlrd.open_workbook(file) as wb:
        ws = wb.sheet_by_index(0) 
        with open(dest, 'w',newline='') as f:
            c = csv.writer(f)
            for r in range(ws.nrows):
                if r!=0:
                    c.writerow(str(ws.cell_value(r,0)).split()+str(ws.cell_value(r,1)).split())		
    f.close()

for cdate in rrule(DAILY, dtstart=sdate, until=edate):
    url1='http://rtdwweb.mavir.hu/webuser/ExportChartXlsIntervalServlet?fromDateXls='+cdate.strftime("%Y-%m-%d")+'&fromTimeXls=T23%3A45%3A00&toDateXls='+(cdate+timedelta(days=1)).strftime("%Y-%m-%d")+'&toTimeXls=T23%3A45%3A00&resoulutionInput=15&unit=min&outputType=XLS&selectedTabId=tab4480&submitXls='   
    url2='http://rtdwweb.mavir.hu/webuser/ExportChartXlsIntervalServlet?fromDateXls='+cdate.strftime("%Y-%m-%d")+'&fromTimeXls=T23%3A45%3A00&toDateXls='+(cdate+timedelta(days=1)).strftime("%Y-%m-%d")+'&toTimeXls=T23%3A45%3A00&resoulutionInput=15&unit=min&outputType=XLS&selectedTabId=tab4469&submitXls='
    file=r'D:\Suli\Önlab\\temp.xls'
    load=r'D:\Suli\Önlab\Adatok\Hun\Load\\'+(cdate+timedelta(days=1)).strftime("%Y-%m-%d")+'.csv'
    wind=r'D:\Suli\Önlab\Adatok\Hun\Wind\\'+(cdate+timedelta(days=1)).strftime("%Y-%m-%d")+'.csv'
    urllib.request.urlretrieve(url1, file)
    Download(url1,load)
    if cdate>=datetime(2008, 12, 31):
        urllib.request.urlretrieve(url2, file)
        Download(url2,wind)