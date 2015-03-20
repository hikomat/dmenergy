# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from urllib import request
from datetime import date,datetime,timedelta
from dateutil.rrule import rrule, DAILY

sdate = date(2000, 1, 1)
edate = date(2015, 3, 19)

def Download(url,dest,cdate):
    elso=True
    response=request.urlopen(url)
    csvs=response.read()
    csv_str= str(csvs).strip("b'")
    lines= csv_str.split("\\n")
    fx=open(dest,"w")
    tdate=cdate+timedelta(days=1)
    for line in lines:
        if elso==False and "System" in dest and not "null" in line and not line.startswith(tdate.strftime("%d/%m/%Y")):
            line=line[:-4]
            line=line[:10]+','+line[11:]
            fx.write(line+'\n')
        elif elso==False and "Wind" in dest and not line.startswith(tdate.strftime("%d/%m/%Y")):
            line=line[:-4]            
            k = line.rsplit(" ,",1)
            line=k[0]
            line=line[:10]+','+line[11:]
            if "null" in line:
                line=line[:8]
            fx.write(line+'\n')
        elso=False
    fx.close()
    
for cdate in rrule(DAILY, dtstart=sdate, until=edate):
        url1='http://www.eirgrid.com/operations/systemperformancedata/download.jsp?download=Y&startdate='+cdate.strftime("%d/%m/%Y")+'&enddate='+cdate.strftime("%d/%m/%Y")+'&proc=data_pack.getsystemdemandforadayt4&templatename=System%20Demand&columnnames=Time,System%20Demand%20MW&prevurl=http://www.eirgrid.com/operations/systemperformancedata/systemdemand/'
        url2='http://www.eirgrid.com/operations/systemperformancedata/download.jsp?download=Y&startdate='+cdate.strftime("%d/%m/%Y")+'&enddate='+cdate.strftime("%d/%m/%Y")+'&proc=data_pack.getwindgenforadayt4&templatename=Wind%20Generation&columnnames=Time,Wind%20Generation%20MW,Forecast%20MW&prevurl=http://www.eirgrid.com/operations/systemperformancedata/windgeneration/'
        sysdem='D:\Suli\Önlab\Adatok\Ireland\System Demand\\'+cdate.strftime("%Y-%m-%d")+'.csv'
        wind='D:\Suli\Önlab\Adatok\Ireland\Wind\\'+cdate.strftime("%Y-%m-%d")+'.csv'
        Download(url1,sysdem,cdate)
        if cdate>=datetime(2003, 1, 1):
            Download(url2,wind,cdate)