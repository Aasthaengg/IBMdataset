import collections
W=collections.Counter(x for x in input())

for i,v in W.items():
  if v%2!=0:
    print('No')
    break
else:
  print('Yes')