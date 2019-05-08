#!  shebang, create a batch file and keep on desktop for easy access

import subprocess, os, time, smtplib, imaplib, imapclient, openpyxl

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

# this thing launches Utorrent from anywhere, just send an email with subject utorrent and nothing but magneturl in the text area,
#checks email every 20 mins,

# needs some corrections, google authorization required, etc

#subprocess.Popen(['start',''], shell=True)
#magnetlinks = 'magnet:?xt=urn:btih:58D36CFD421B7D187ED58127313A79E9E1DFF27F&dn=Ant-Man%20and%20the%20Wasp%20%282018%29%20720p%20BluRay%20x264%20%5bDual-Audio%5d%5bHindi%20DTH%205.1%20-%20English%205.1%5d%20ESubs%20-%20Downloadhub'
#'C:\\Users\\dhira\\Downloads\\antman.torrent'


while True:
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login('dom3d69@gmail.com', '3dom@6999')
    imapObj.select_folder('INBOX', readonly=True)
    UIDs = imapObj.search(['SINCE 18-Mar-2019','FROM alice@example.com','Subject utorrent'])
    for UID in UIDs:
        message = pyzmail.PyzMessage.factory(rawMessages[UID]['BODY[]'])
        maglink = message.text_part.get_payload().decode(message.text_part.charset)
        subprocess.Popen(['start','maglink'], shell=True)
    imapObj.logout()
    time.sleep(20*60)
                          
