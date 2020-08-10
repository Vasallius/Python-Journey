# Downloading Google Forms Data

import ezsheets

# Load the spreadsheet and the sheet
# Replace with your spreadsheet id
ss = ezsheets.Spreadsheet('1SZq-wSN_iWuOZENRrNfD_YcbK95p2mHCcw9WBeLSbmQ')
sheet = ss[0]

# Check for the column that has email address as its header
for column in range(sheet.columnCount):
    coldata = sheet.getColumn(column+1)

    if 'Email Address' in coldata:
        colnumber = column+1
        break

# Store emails into a list
column_data = sheet.getColumn(colnumber)
email_list = column_data[1:]


def filter_function(email):
    if email == '':
        return False
    else:
        return True


# Remove empty emails
email_list = filter(filter_function, email_list)

# Print!
print('Email addresses: ')
for email in email_list:
    print(email)
