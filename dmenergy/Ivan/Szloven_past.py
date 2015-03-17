# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:11:38 2015

@author: Iván
"""


import urllib.request
from xml.dom import minidom
import os
import csv
from datetime import date
from dateutil.rrule import rrule, DAILY

star_tdate = date(2007, 2, 22)
end_date = date(2015, 3,16)
for dt in rrule(DAILY, dtstart=star_tdate, until=end_date):
    opener = urllib.request.FancyURLopener({})
    url = "http://www.eles.si/prevzem-in-proizvodnja.aspx?destinationp=1&mesecifrom=1&letofrom=2012&letood=2012&datefrom="+dt.strftime('%d.%m.%Y')+"&dateto="+dt.strftime('%d.%m.%Y')+"&XML=XML"
    f = opener.open(url)
    xmldoc = minidom.parse(f)
    
    filename=dt.strftime("%Y-%m-%d")+".csv"
    with open(os.path.join("D:szlovenia", filename), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)    
    
        items = xmldoc.getElementsByTagName("item")
        for item in items:
            prevzems = item.getElementsByTagName("prevzem")
            date = datetime.strptime(item.getElementsByTagName("datum")[0].childNodes[0].data,'%d.%m.%Y %H:%M')
            date.strftime('%Y-%m-%d %H:%M')
            for prevzem in prevzems:
                consumption = prevzem.getElementsByTagName("dejansko_MWh")[0].childNodes[0].data
                forcast = prevzem.getElementsByTagName("napoved_MWh")[0].childNodes[0].data
                spamwriter.writerow([date] +[consumption]+[forcast])

