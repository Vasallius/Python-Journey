# Blank Row Inserter

import openpyxl
import sys

# Assign variables
row = int(sys.argv[1])
times = int(sys.argv[2])
filename = sys.argv[3]

# Open workbook
wb = openpyxl.load_workbook(filename)
sheet = wb.active

# Insert rows
while times != 0:
    sheet.insert_rows(row)
    times -= 1
    row += 1

wb.save(filename)
