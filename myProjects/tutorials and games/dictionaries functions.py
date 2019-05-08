import pprint

john = {'finisher':'attitude adjustment','signature':'5 knuckle shuffle','comeback':'cenation'}
ronda = {'finisher':'arm bar','signature':'samoan drop','comeback':'rowdy!!'}
linejohn = ('john cena\'s finisher is ' + str(john.get('finisher')))
line = ('this program prints the number of times each character has occurred in the line')

def disp(playername):
        for i in playername:
         print('john'+' has '+ str(playername[i])+' as his '+(i))
#disp(john)


bayek = {'swords':2,'arrows':45,'bolts':15,'rope':1,'coins':6000}
hiddenone = ['swords','coins','rubies','collectibles','rope']
def disp2(player,listname):
        print('inventory:')
        x=0
        for i in listname:
                if i in player.keys():
                        player[i]=player[i]+1
                else:
                        player.setdefault(i,1)
                #player.setdefault(str(listname),0)
        for k,v in player.items():
                print(str(v)+' ' + k)
                x+=v
        print('total items are '+str(x))
        
disp2(bayek,hiddenone)


