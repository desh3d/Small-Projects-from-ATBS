#!

john = {'finisher':'attitude adjustment','signature':'5 knuckle shuffle','comeback':'cenation'}
ronda = {'finisher':'arm bar','signature':'samoan drop','comeback':'rowdy!!'}
linejohn = ('john cena\'s finisher is ' + str(john.get('finisher')))
line = ('this program prints the number of times each character has occurred in the line')
count = {}
for char in line:
        count.setdefault(char,0)
        count[char]=count[char]+1
print(count)
