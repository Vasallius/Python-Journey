# Finding Mistakes in a Spreadsheet

import ezsheets

# Load spreadsheet
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]

for row_num in range(2, sheet.rowCount+1):
    data_row = sheet.getRow(row_num)
    for data_num in range(len(data_row)):
        try:
            data_row[data_num] = int(data_row[data_num])
        except:
            pass
    try:
        if data_row[0] * data_row[1] == data_row[2]:
            pass
        else:
            print(f'Row number {row_num} has an error. Total beans'
                  f'should be {data_row[0] * data_row[1]}, not {data_row[2]}')
    except:
        pass
