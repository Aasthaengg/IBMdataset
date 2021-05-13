from collections import Counter
s = Counter(input())
if (s['N'] > 0) ^ (s['S'] > 0) or (s['E'] > 0) ^ (s['W'] > 0):
    print('No')
else:
    print('Yes')
