# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 17:49:00 2015

@author: Dániel
"""

import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import timedelta,datetime

driver = webdriver.Chrome(r'C:\Users\Dániel\Downloads\WinPython-64bit-3.4.3.1\chromedriver')
cdate=datetime.now()-timedelta(days=1)
url1='https://demanda.ree.es/movil/peninsula/demanda/tablas/'+cdate.strftime("%Y-%m-%d")+'/1'
url2='https://demanda.ree.es/movil/peninsula/demanda/tablas/'+cdate.strftime("%Y-%m-%d")+'/2'
demand=r'D:\Suli\Önlab\Adatok\Spain\Demand\\'+cdate.strftime("%Y-%m-%d")+'.csv'
wind=r'D:\Suli\Önlab\Adatok\Spain\Wind\\'+cdate.strftime("%Y-%m-%d")+'.csv'

def Download(url,dest):
    driver.get(url)
    time.sleep(5)
    file=open(dest,"w",newline='')
    c=csv.writer(file,delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for i in range(20,164):
        if "Demand" in dest:
            element = driver.find_element_by_xpath('//*[@id="tabla_evolucion"]/tbody/tr['+str(i)+']')
        elif "Wind" in dest:
            element = driver.find_element_by_xpath('//*[@id="tabla_generacion"]/tbody/tr['+str(i)+']')
        html=element.get_attribute('innerHTML')
        soup=BeautifulSoup(html)
        html=soup.find_all('td')
        a=html[0].text[:10]
        b=html[0].text[11:16]
        if "Demand" in dest:
            c.writerow([a,b,html[1].text])
        elif "Wind" in dest:
            c.writerow([a,b,html[6].text])
    file.close()
    
Download(url1,demand)
Download(url2,wind)
driver.close()