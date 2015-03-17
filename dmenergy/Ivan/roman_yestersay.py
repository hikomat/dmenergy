# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:11:38 2015

@author: Iván
"""

import xlrd
import urllib
import csv
import os
from datetime import timedelta,datetime

# tegnapi adatokhoz
yesterday = datetime.now()- timedelta(days=1)
start_Year=yesterday.strftime('%Y')
start_Month=yesterday.strftime('%m')
start_Day=yesterday.strftime('%d')

end_Year=yesterday.strftime('%Y')
end_Month=yesterday.strftime('%m')
end_Day=yesterday.strftime('%d')

outfilename = "test.xls"
url_of_file = "http://www.transelectrica.ro/widget/web/tel/sen-grafic?p_p_id=SENGrafic_WAR_SENGraficportlet&p_p_lifecycle=2&p_p_state=maximized&p_p_mode=view&p_p_cacheability=cacheLevelPage&_SENGrafic_WAR_SENGraficportlet_random=random&_SENGrafic_WAR_SENGraficportlet_start_day="+start_Day+"&_SENGrafic_WAR_SENGraficportlet_start_month="+start_Month+"&_SENGrafic_WAR_SENGraficportlet_start_year="+start_Year+"&_SENGrafic_WAR_SENGraficportlet_start_Hour="+"0"+"&_SENGrafic_WAR_SENGraficportlet_start_Minute="+"0"+"&_SENGrafic_WAR_SENGraficportlet_end_day="+end_Day+"&_SENGrafic_WAR_SENGraficportlet_end_month="+end_Month+"&_SENGrafic_WAR_SENGraficportlet_end_year="+end_Year+"&_SENGrafic_WAR_SENGraficportlet_end_Hour="+"23"+"&_SENGrafic_WAR_SENGraficportlet_end_Minute="+"59"+"&_SENGrafic_WAR_SENGraficportlet_excel=true"
urllib.request.urlretrieve(url_of_file, outfilename) 

filename=yesterday.strftime("%Y-%m-%d")+".csv"
with open(os.path.join("D:\\romania", filename), 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)

    workbook = xlrd.open_workbook(outfilename)
    worksheet = workbook.sheet_by_index(0)
    num_rows = worksheet.nrows - 1
    num_cells = worksheet.ncols - 1
    curr_row = 0   #levágjuk az első sort
    while curr_row < num_rows-2:
        curr_row += 1
        row = worksheet.row(curr_row)
        curr_cell = -1
        while curr_cell < num_cells-8: #többi oszlop nem érdekes
            curr_cell += 1
            if curr_cell==0:
                date = datetime.strptime(worksheet.cell_value(curr_row, curr_cell),'%d-%m-%Y %H:%M:%S')
                date.strftime('%Y-%m-%d %H:%M:%S')
            elif curr_cell==1:
                consumption= worksheet.cell_value(curr_row, curr_cell)
            elif curr_cell==3:
                produce= worksheet.cell_value(curr_row, curr_cell)
        spamwriter.writerow([date] +[consumption]+[produce])
  