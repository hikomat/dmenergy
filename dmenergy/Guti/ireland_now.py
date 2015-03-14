# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from urllib import request
from datetime import datetime,timedelta

cdate=datetime.now()-timedelta(days=1)

url1='http://www.eirgrid.com/operations/systemperformancedata/download.jsp?download=Y&startdate='+cdate.strftime("%d/%m/%Y")+'&enddate='+cdate.strftime("%d/%m/%Y")+'&proc=data_pack.getsystemdemandforadayt4&templatename=System%20Demand&columnnames=Time,System%20Demand%20MW&prevurl=http://www.eirgrid.com/operations/systemperformancedata/systemdemand/'
url2='http://www.eirgrid.com/operations/systemperformancedata/download.jsp?download=Y&startdate='+cdate.strftime("%d/%m/%Y")+'&enddate='+cdate.strftime("%d/%m/%Y")+'&proc=data_pack.getwindgenforadayt4&templatename=Wind%20Generation&columnnames=Time,Wind%20Generation%20MW,Forecast%20MW&prevurl=http://www.eirgrid.com/operations/systemperformancedata/windgeneration/'
sysdem='D:\Suli\Önlab\Adatok\Ireland\System Demand\\'+cdate.strftime("%Y-%m-%d")+'.csv'
wind='D:\Suli\Önlab\Adatok\Ireland\Wind\\'+cdate.strftime("%Y-%m-%d")+'.csv'
def Download(url,dest):
    elso=True
    response=request.urlopen(url)
    csvs=response.read()
    csv_str= str(csvs).strip("b'")
    lines= csv_str.split("\\n")
    fx=open(dest,"w")
    tdate=cdate+timedelta(days=1)
    for line in lines:
        if elso==False and not "null" in line and not line.startswith(tdate.strftime("%d/%m/%Y")):
            line=line[:-4]
            if "Wind" in dest:
                k = line.rsplit(" ,",1)
                line=k[0]
            fx.write(line+'\n')
        elso=False
    fx.close()
    
Download(url1,sysdem)
Download(url2,wind)    