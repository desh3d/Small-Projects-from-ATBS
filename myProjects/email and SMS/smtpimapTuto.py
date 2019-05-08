import subprocess, os, time, smtplib, imapclient, pyzmail

# SMTP and IMAP Tuto

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

# sending mail by smtplib

#smtpObj = smtplib.SMTP('smtp.gmail.com',587)
#print(smtpObj.ehlo())
#print(smtpObj.starttls())
#print(smtpObj.login('dom3d69@gmail.com', '3dom@6999'))  # you have to enable google Less sure apps to work this code
#print(smtpObj.sendmail('dhirajdeshpande1596@gmail.com', 'milinddevade5588@gmail.com', 'subject: HI bhava. \nKasa aahes? Udya college aahe ka?.'))
#print(smtpObj.quit())


# receving mail by imapclient and pyzmail


imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print(imapObj.login('dom3d69@gmail.com', '3dom@6999'))


print(imapObj.select_folder('INBOX', readonly=True))
UIDs = imapObj.search(['SINCE 18-Mar-2019'])
print(UIDs)     # this will output [40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
rawMessages = imapObj.fetch([40041],['BODY[]','FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessages[40032]['BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))   # 'from' or 'to' or 'cc' or 'bcc'
message.text_part != None    # True
message.html_part != None    # True
print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part.get_payload().decode(message.html_part.charset))
imapObj.logout()

# inbox searches

pprint.pprint(imapObj.list_folders())    #  in case you need a list of available folders, like INBOX
print(imapObj.search(['ALL']))
print(imapObj.search(['SINCE 01-Jan-2015', 'BEFORE 01-Feb-2015', 'UNSEEN']))
print(imapObj.search(['SINCE 01-Jan-2015', 'FROM alice@example.com']))
print(imapObj.search(['OR FROM alice@example.com FROM bob@example.com']))
