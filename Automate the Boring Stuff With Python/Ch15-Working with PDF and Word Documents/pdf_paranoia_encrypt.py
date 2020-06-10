# Vasallius

# Import necessary modules
import os
import PyPDF2
import sys

# Make sure user enters two command line arguments
if len(sys.argv) < 2:
    print('Usage: pdf_paranoia_encrypt.py <password>')
    sys.exit()

password = sys.argv[1]

# Walk through each file in the current directory
for root, dir, file in os.walk(os.getcwd()):

    for filename in file:
        # Skip non-PDF Files
        if not filename.endswith('.pdf'):
            continue
        # Try to open PDFs
        try:
            pdfFileObj = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        except:
            print(f'{filename} cannot be opened.')
        # Check for unencrypted PDFs
        if pdfReader.isEncrypted == False:
            pdfWriter = PyPDF2.PdfFileWriter()
            # Add every page to writer object
            for pagenum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pagenum)
                pdfWriter.addPage(pageObj)
            # Encrypt the password
            pdfWriter.encrypt(password)
            # Save as <file>_encrypted.pdf
            (base_filename, extension) = os.path.splitext(filename)
            encryptedPDF = open(f'{base_filename}_encrypted.pdf', 'wb')
            pdfWriter.write(encryptedPDF)
            print(filename, 'has been encrypted.')
            pdfFileObj.close()
            encryptedPDF.close()
        else:
            pass

print('All PDFs have been encrypted...')

# Code for testing if encryption was successful
print('Now testing to decrypt...')
for root, dir, file in os.walk(os.getcwd()):

    for filename in file:
        # Skil non-encrypted PDFs
        if not filename.endswith('encrypted.pdf'):
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
            else:
                print('Password decryption was unsuccessful')
        else:
            pass
