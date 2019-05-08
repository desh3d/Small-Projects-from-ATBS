#!
# program for manipulate copied text as you like

import pyperclip
import pprint

inputtext = pyperclip.paste()

#****************Do SOMETHING to this text eg.***************

#modifiedtext = inputtext.upper()


modifiedtext = inputtext.split('\n')
for i in range(len(modifiedtext)):
  modifiedtext[i] = '*** ' + modifiedtext[i] # adds *** at begenning of new line
modifiedtext = ('\n').join(modifiedtext)
print(pprint.pformat(modifiedtext))
print(modifiedtext)

#************copy modified text to clipboard*************

pyperclip.copy(modifiedtext)
