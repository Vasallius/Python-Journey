# PDF Paranoia Decrypt

import os
import PyPDF2
import sys

# Make sure user enters two command line arguments
if len(sys.argv) < 2:
    print('Usage: pdf_paranoia_encrypt.py <password>')
    sys.exit()

password = sys.argv[1]

# Code for testing if encryption was successful
print('Now testing to decrypt...')
for root, dir, file in os.walk(os.getcwd()):

    for filename in file:
        # Skip non-encrypted PDFs
        if not filename.endswith('_encrypted.pdf'):
            continue
        # Try to open PDFs
        try:
            pdfFileObj = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        except:
            print(f'{filename} cannot be opened')
        if pdfReader.isEncrypted == True:
            decryptSuccess = pdfReader.decrypt(password)
            if decryptSuccess == True:
                print('Password decryption was successful')
                pdfWriter = PyPDF2.PdfFileWriter()
                for pagenum in range(pdfReader.numPages):
                    pageobj = pdfReader.getPage(pagenum)
                    pdfWriter.addPage(pageobj)
                decryptedpdf = open(f'{filename[:-14]}.pdf', 'wb')
                pdfWriter.write(decryptedpdf)
                print(f'{filename[:-14]} created without password')
            else:
                print('Password decryption was unsuccessful')
        else:
            pass
