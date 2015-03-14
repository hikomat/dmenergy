# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:23:19 2015

@author: Dániel
"""

import xlrd
import csv
import urllib
from datetime import date,timedelta
from dateutil.rrule import rrule, DAILY

sdate = date(2004, 1, 1)
edate = date(2015,3,12)

def Download(url,dest,cdate):
    with xlrd.open_workbook(file) as wb:
        ws = wb.sheet_by_index(0) 
        with open(dest, 'w',newline='') as f:
            c = csv.writer(f)
            a=0
            for r in range(ws.nrows):
                if r!=0:
                    wdate=cdate.strftime("%Y-%m-%d ")+str(a)+":00"
                    a+=1
                    c.writerow(wdate.split()+str(ws.cell_value(r,2)).split())	
    f.close()
    
for cdate in rrule(DAILY, dtstart=sdate, until=edate):
    url1='http://www.fingrid.fi/EN/ELECTRICITY-MARKET/LOAD-AND-GENERATION/Pages/default.aspx/Excel/TimeSeries.xls?beginDate='+cdate.strftime("%Y%m%d")+'&endDate='+cdate.strftime("%Y%m%d")+'&variables=H4sIAAAAAAAEAO29B2AcSZYlJi9tynt_SvVK1-B0oQiAYBMk2JBAEOzBiM3mkuwdaUcjKasqgcplVmVdZhZAzO2dvPfee--999577733ujudTif33_8_XGZkAWz2zkrayZ4hgKrIHz9-fB8_Ih7_ZFYX2aTMmyP769nyvDp6_CJb5Efnxe__dl2u23Xz-1_P28d3-cPHZ8vLvG5_MivX1CIrm_zxXf-jx_zjWVUvsvZ1WxfLi6MfH_34j-88vtv_4vFXy6J9k79rj7747vzu_PFd-_fjN0Vb5kenZT6lptOivU7LKps9viufP35eLPOTqqzq9K73x7fbRXn048-e7dDz-G748ePX8-rqy2V5_YwGVOdPszYz6Ee-AbY-PSLUeXb2-7_56ss3xy_efPn7_z7ffvNzTZ6LfJnXWVtUy1sRaYefb5ZI9s_m6P8BT2NihFoCAAA1&cultureId=en-US&dataTimePrecision=5'   
    file=r'D:\Suli\Önlab\\temp.xls'
    load=r'D:\Suli\Önlab\Adatok\Finland\Load\\'+cdate.strftime("%Y-%m-%d")+'.csv'
    urllib.request.urlretrieve(url1, file)
    Download(url1,load,cdate)