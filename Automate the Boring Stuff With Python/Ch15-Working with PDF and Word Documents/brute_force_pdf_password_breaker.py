# Vasallius

# Import necessary modules
import PyPDF2

# Open dictionary file
dictionaryfile = open('dictionary.txt')
word_list = []

filename = input('Enter filename of password protected pdf: ')

# Add uppercase and lowercase version of the word to word_list
for line in dictionaryfile.readlines():
    uppercase = line.upper().rstrip()
    lowercase = line.lower().rstrip()
    word_list.append(uppercase)
    word_list.append(lowercase)

# Open password-protected pdf
pdfObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfObj)

# Loop over the words and try to decrypt
for word in word_list:
    if pdfReader.decrypt(word) == 1:
        print(f'The password is {word}.')
        break
    else:
        pass
    