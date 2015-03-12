# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:11:38 2015

@author: Iván
"""


import urllib.request
from datetime import timedelta,datetime
from xml.dom import minidom
import csv
import os

yesterday = datetime.now()- timedelta(days=1)

opener = urllib.request.FancyURLopener({})
url = "http://www.eles.si/prevzem-in-proizvodnja.aspx?destinationp=1&mesecifrom=1&letofrom=2012&letood=2012&datefrom="+yesterday.strftime('%d.%m.%Y')+"&dateto="+yesterday.strftime('%d.%m.%Y')+"&XML=XML"
f = opener.open(url)
xmldoc = minidom.parse(f)

filename=yesterday.strftime("%Y-%m-%d")+".csv"
with open(os.path.join("D:szlovenia", filename), 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',quotechar=',', quoting=csv.QUOTE_MINIMAL)

    items = xmldoc.getElementsByTagName("item")
    for item in items:
        prevzems = item.getElementsByTagName("prevzem")
        datum = item.getElementsByTagName("datum")[0].childNodes[0].data
        for prevzem in prevzems:
            fogyasztas = prevzem.getElementsByTagName("dejansko_MWh")[0].childNodes[0].data
            spamwriter.writerow([datum] +[fogyasztas])

