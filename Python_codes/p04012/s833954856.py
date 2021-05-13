from collections import Counter
flg = True
c = Counter(input())

for v in c.values():
  flg = flg and v % 2 == 0

print('Yes' if flg else 'No')