# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:23:19 2015

@author: Dániel
"""

import xlrd
import csv
import urllib
from datetime import datetime,timedelta

cdate=datetime.now()-timedelta(days=2)
url1='http://rtdwweb.mavir.hu/webuser/ExportChartXlsIntervalServlet?fromDateXls='+cdate.strftime("%Y-%m-%d")+'&fromTimeXls=T23%3A45%3A00&toDateXls='+(cdate+timedelta(days=1)).strftime("%Y-%m-%d")+'&toTimeXls=T23%3A45%3A00&resoulutionInput=15&unit=min&outputType=XLS&selectedTabId=tab4480&submitXls='   
url2='http://rtdwweb.mavir.hu/webuser/ExportChartXlsIntervalServlet?fromDateXls='+cdate.strftime("%Y-%m-%d")+'&fromTimeXls=T23%3A45%3A00&toDateXls='+(cdate+timedelta(days=1)).strftime("%Y-%m-%d")+'&toTimeXls=T23%3A45%3A00&resoulutionInput=15&unit=min&outputType=XLS&selectedTabId=tab4469&submitXls='
file=r'D:\Suli\Önlab\\temp.xls'
load=r'D:\Suli\Önlab\Adatok\Hun\Load\\'+(cdate+timedelta(days=1)).strftime("%Y-%m-%d")+'.csv'
wind=r'D:\Suli\Önlab\Adatok\Hun\Wind\\'+(cdate+timedelta(days=1)).strftime("%Y-%m-%d")+'.csv'

def Download(url,dest):
    with xlrd.open_workbook(file) as wb:
        ws = wb.sheet_by_index(0) 
        with open(dest, 'w',newline='') as f:
            c = csv.writer(f)
            for r in range(ws.nrows):
                if r!=0:
                    c.writerow(str(ws.cell_value(r,0)).split()+str(ws.cell_value(r,1)).split())				
    f.close()
	
urllib.request.urlretrieve(url1, file)
Download(url1,load)
urllib.request.urlretrieve(url2, file)
Download(url2,wind)