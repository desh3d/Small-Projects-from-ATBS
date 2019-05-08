tictac={'topL':'','topM':'','topR':'',
           'midL':'','midM':'','midR':'',
           'botL':'','botM':'','botR':''}


def theboard(board):
        print(board['topL']+'|'+board['topM']+'|'+board['topR']+'\n'+
              board['midL']+'-'+board['midM']+'-'+board['midR']+'\n'+
              board['botL']+'|'+board['botM']+'|'+board['botR'])
print('this is what board looks like now')
theboard(tictac)
for i,j in zip(range(1,4), range(1,4)):
 X=input('Enter your ' + str(i)+'st'+ ' X position, eg topR or botM or midL:')
 if X in tictac.keys():
        tictac[X] = 'X'
        theboard(tictac)
 O=input('Enter your ' + str(j)+'st'+ ' O position, eg topR or botM or midL:')
 if O in tictac.keys():
        tictac[O] = 'O'
 theboard(tictac)
