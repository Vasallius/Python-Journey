# Auto Unsubscriber

import imapclient
import imaplib
import webbrowser
import bs4
import pyzmail

email = input('Email: ')
password = input('Password: ')

imaplib._MAXLINE = 1000000
imap_object = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imap_object.login(email, password)
imap_object.select_folder('INBOX', readonly=False)
UIDs = imap_object.search(['ALL'])
rawmessages = imap_object.fetch(UIDs, ['BODY[]'])
unsub_links = []

for index, uid in enumerate(UIDs):
    message = pyzmail.PyzMessage.factory(rawmessages[UIDs[index]][b'BODY[]'])
    if message.html_part != None:
        message_body = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(message_body, 'html.parser')
        for link in soup.find_all('a'):
            if 'unsubscribe' in link.text.lower():
                unsub_links.append(link.get('href'))
            elif 'unsubscribe' in link:
                unsub_links.append(link)
            else:
                pass
    else:
        pass

for unsub_link in unsub_links:
    webbrowser.open(unsub_link)

print('Check google chrome for opened tabs.')
