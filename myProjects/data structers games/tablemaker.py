#!

table = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

for i,j,k in zip(table[0], table[1], table[2]):
  x= i.rjust(10)+ ' ' + j.rjust(10) +' '+ k.rjust(10)
  print(x)
