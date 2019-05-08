#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

# Preset values:
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+15559998888'
twilioNumber = '+15552225678'

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

# save above code as py and jsut import and pass message as argument
import textmyself     
textmyself.textmyself('The boring task is finished.')



print(message.to, message.from_, message.body, message.status, message.date_created)   # not accurate
print(message.sid)
updatedMessage = twilioCli.messages.get(message.sid)   
print(updatedMessage.status, updatedMessage.date_sent)  # accurate


'''Once you’ve installed the twilio module, signed up for a Twilio account, verified your phone number, registered a Twilio phone number, and obtained your account
SID and auth token, you will finally be ready to send yourself text messages from your Python scripts.
Compared to all the registration steps, the actual Python code is fairly simple.''' 
