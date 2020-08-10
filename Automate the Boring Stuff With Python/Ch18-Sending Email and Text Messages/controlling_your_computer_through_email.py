# Controlling Your Computer Through Email

import imaplib
import imapclient
import subprocess
import pyzmail
import smtplib
import time

# INITIALIZATION
# FILL IN WITH RESPECTIVE CREDENTIALS
MY_EMAIL = 'testemail@gmail.com'
MY_PASSWORD = 'testpassword'
TEST_SENDER = 'testemail2@gmail.com'

while True:
    # INIATIALIZE
    imaplib._MAXLINE = 1000000
    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_obj.login(MY_EMAIL, MY_PASSWORD)
    imap_obj.select_folder('INBOX', readonly=False)
    UIDs = imap_obj.search(['FROM', TEST_SENDER])
    rawmessages = imap_obj.fetch(UIDs, ['BODY[]'])

    torrent_links = []

    # RETRIEVE MAGNET LINK
    for message in rawmessages:
        raw_body = pyzmail.PyzMessage.factory(rawmessages[message][b'BODY[]'])
        if raw_body.text_part != None:
            message_body = raw_body.text_part.get_payload().decode(raw_body.text_part.charset)
            torrent_links.append(message_body)

    if len(torrent_links) > 0:
        # OPEN TORRENT AND START DOWNLOADING
        for link in torrent_links:
            # REPLACE WITH THE YOUR QBITTORRENT PATH
            qb_process = subprocess.Popen(
                [r'C:\Program Files\qBittorrent\qbittorrent.exe', link])
            qb_process.wait()
            print('Torrent file has finished downloading.')
            smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpobj.ehlo()
            smtpobj.starttls()
            smtpobj.login(MY_EMAIL, MY_PASSWORD)
            print(f'Sending completion message to {MY_EMAIL}')
            smtpobj.sendmail(
                MY_EMAIL, MY_EMAIL, 'Subject: Torrent File \nTorrent file has finished downloading.')
            smtpobj.quit()

            # DELETE MESSAGE
            imap_obj.delete_messages(UIDs)
            imap_obj.expunge()

    time.sleep(60 * 15)  # REPEAT EVERY 15 MINUTES
