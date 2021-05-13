from collections import Counter
L=Counter(list(map(int,input().split())))

if L[5]==2 and L[7]==1:
  print('YES')
else:
  print('NO')