import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

from collections import Counter
c = Counter(rs())
f = False
if (c['N'] > 0 and c['S'] > 0) or (c['N'] == 0 and c['S'] == 0):
    if (c['W'] > 0 and c['E'] > 0) or (c['W'] == 0 and c['E'] == 0):
        f = True
print('Yes' if f else 'No')