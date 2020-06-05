# Vasallius

# Import necessary modules
import ezsheets
import os

# Load the spreadsheet
spreadsheet_id = input("Enter id of spreadsheet to be uploaded ex:(1SZq-wSN_iWuOZENRrNfD_YcbK95p2mHCcw9WBeLSbmQ): ")
ss = ezsheets.Spreadsheet(spreadsheet_id)

# Download files
print("Downloading as excel file...")
ss.downloadAsExcel()
print("Downloading as OpenOffice file...")
ss.downloadAsODS()
print("Downloading as CSV file...")
ss.downloadAsCSV()
print("Downloading as TSV file...")
ss.downloadAsTSV()
print("Downloading as PDF file...")
ss.downloadAsPDF()
print("Downloading as HTML file...")
ss.downloadAsHTML()

print(f"Downloading done. \n Files saved at {os.getcwd()}.")