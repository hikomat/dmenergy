# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:11:38 2015

@author: Iván
"""

import xlrd
import os
import urllib
from datetime import date
from dateutil.rrule import rrule, DAILY
import csv


star_tdate = date(2010, 1, 1)
end_date = date(2015, 3,11)
for dt in rrule(DAILY, dtstart=star_tdate, until=end_date):
    filename=dt.strftime("%Y-%m-%d")+".csv"
    with open(os.path.join("D:\\litvania", filename), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        outfilename = "test.xls"
        url_of_file = "http://www.litgrid.eu/index.php/generate-excel-file/687?filter[from]="+dt.strftime("%Y-%m-%d")+"&filter[to]="+dt.strftime("%Y-%m-%d")+"&lines=648%2C649%2C650"
        urllib.request.urlretrieve(url_of_file, outfilename) 

        workbook = xlrd.open_workbook(outfilename)
        worksheet = workbook.sheet_by_index(0)
        num_rows = worksheet.nrows - 1
        num_cells = worksheet.ncols - 1
        curr_row = 1   #levágjuk az első sorokat
        while curr_row < num_rows:
            curr_row += 1
            row = worksheet.row(curr_row)
            curr_cell = -1
            while curr_cell < num_cells-2: #többi oszlop nem érdekes
                curr_cell += 1
                if curr_cell==0:
                    datum= worksheet.cell_value(curr_row, curr_cell)
                elif curr_cell==1:
                    ertek= worksheet.cell_value(curr_row, curr_cell)
                    spamwriter.writerow([datum]  + [ertek])

  