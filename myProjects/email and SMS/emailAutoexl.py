import subprocess, os, time, smtplib, openpyxl

# this is a simple program whic grabs seletive emails from excel sheet and send mail accordingly, This needs some work, eg setting up and actual email that works and has less secure app
# access from gmail, remove necessary comments, updating condition,etc.
# but with a little work This program si very useful for the right person

os.chdir('C:\\Users\\dhira\\Desktop\\mywork')

wb = openpyxl.load_workbook('duesRecords.xlsx')
#print(wb.sheetnames)
sheet = wb['Sheet1']

emails = {}
unpaidMembers = {}

for rowNum in range(2,sheet.max_row+1):
            rowData = []
            for colNum in range(2,sheet.max_column+1):
                cellVal = (sheet.cell(row=rowNum, column=colNum).value)
                #print('Cell ' + str(rowNum)+ str(colNum) + ' has value ' + str(cellVal))
                if cellVal == None:                                                                   # change this condition to -- if payment != 'paid':
                    #print(sheet.cell(row=1, column=colNum).value)   # to get corresponding column title
                    #print(sheet.cell(row=rowNum, column=2).value)   # to get corresponding row value
                    emails.setdefault((sheet.cell(row=rowNum, column=2).value), sheet.cell(row=1, column=colNum).value)

                    # OR name = sheet.cell(row=r, column=1).value
                    #    email = sheet.cell(row=r, column=2).value
                    #    sunpaidMembers[name] = email

print(emails)

# Log in to email account.
#smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
#smtpObj.ehlo()
#smtpObj.starttls()
#smtpObj.login(' my_email_address@gmail.com ', sys.argv[1])   # or ,enter your_secret_passward
# Send out reminder emails.
for email, month in emails.items():
     body = "Subject: Monthly dues unpaid.\nDear member \nRecords show that you have not paid your dues since " + str(month) + " plz pay "
     print(body)
     print("sending mail to "+ email)
     #sendmailStatus = smtpObj.sendmail
     #if sendmailStatus != {}:
     #      print('There was a problem sending email to ' + email)
#smtpObj.quit()
