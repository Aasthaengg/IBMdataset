import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

w = LS2()

from collections import Counter

c = Counter(w)
a = sum(c[i] % 2 != 0 for i in c.keys())
print('Yes' if a == 0 else 'No')
