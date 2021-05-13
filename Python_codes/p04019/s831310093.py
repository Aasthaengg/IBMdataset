S=input()
A=[]
for letter in S:
    A.append(letter)
if ('N' in A and 'S' not in A) or ('S' in A and 'N' not in A) or ('E' in A and 'W' not in A)or ('W' in A and 'E' not in A):
    print('No')
else:
    print('Yes')