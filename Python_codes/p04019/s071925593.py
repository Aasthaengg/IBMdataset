S=input()
n=('N' in S)
s=('S' in S)
w=('W' in S)
e=('E' in S)
if not n^s and not w^e:
  print('Yes')
else:
  print('No')