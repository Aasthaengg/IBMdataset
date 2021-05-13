string=input()
n=[]
for letter in string:
    n.append(letter)
if ('N' in n and 'S' not in n) or ('S' in n and 'N' not in n) or ('E' in n and 'W' not in n)or ('W' in n and 'E' not in n):
    print('No')
else:
    print('Yes')