from collections import Counter

c = Counter(input())

for k in c.keys():
  if c[k] % 2 == 1:
    print('No')
    exit()
    
print('Yes')