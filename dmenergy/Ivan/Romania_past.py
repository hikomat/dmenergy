# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:55:27 2015

@author: Iván
"""
import xlrd
import urllib
import os
import csv
from datetime import date,timedelta,datetime
from dateutil.rrule import rrule, DAILY

# tegnapi adatokhoz
yesterday = datetime.now()- timedelta(days=1)
start_Year=yesterday.strftime('%Y')
start_Month=yesterday.strftime('%m')
start_Day=yesterday.strftime('%d')

end_Year=yesterday.strftime('%Y')
end_Month=yesterday.strftime('%m')
end_Day=yesterday.strftime('%d')

star_tdate = date(2008, 1, 1)
end_date = date(2015, 3, 11)
for dt in rrule(DAILY, dtstart=star_tdate, until=end_date):
    filename=dt.strftime("%Y-%m-%d")+".csv"
    with open(os.path.join("D:\\romania", filename), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        outfilename = "test.xls"
        url_of_file = "http://www.transelectrica.ro/widget/web/tel/sen-grafic?p_p_id=SENGrafic_WAR_SENGraficportlet&p_p_lifecycle=2&p_p_state=maximized&p_p_mode=view&p_p_cacheability=cacheLevelPage&_SENGrafic_WAR_SENGraficportlet_random=random&_SENGrafic_WAR_SENGraficportlet_start_day="+dt.strftime('%d')+"&_SENGrafic_WAR_SENGraficportlet_start_month="+dt.strftime('%m')+"&_SENGrafic_WAR_SENGraficportlet_start_year="+dt.strftime('%Y')+"&_SENGrafic_WAR_SENGraficportlet_start_Hour="+"0"+"&_SENGrafic_WAR_SENGraficportlet_start_Minute="+"0"+"&_SENGrafic_WAR_SENGraficportlet_end_day="+dt.strftime('%d')+"&_SENGrafic_WAR_SENGraficportlet_end_month="+dt.strftime('%m')+"&_SENGrafic_WAR_SENGraficportlet_end_year="+dt.strftime('%Y')+"&_SENGrafic_WAR_SENGraficportlet_end_Hour="+"23"+"&_SENGrafic_WAR_SENGraficportlet_end_Minute="+"59"+"&_SENGrafic_WAR_SENGraficportlet_excel=true"
        urllib.request.urlretrieve(url_of_file, outfilename) 

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
                    datum= worksheet.cell_value(curr_row, curr_cell)
                elif curr_cell==1:
                    fogyasztas= worksheet.cell_value(curr_row, curr_cell)
            spamwriter.writerow([datum] +[fogyasztas])
  