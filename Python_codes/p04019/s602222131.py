from collections import Counter
S = list(input())
def zeroandnot0(a, b):
    if (a == 0 and b != 0) or (a != 0 and b == 0):
        return True
    else:
        return False
c = Counter(S)
if zeroandnot0(c['E'], c['W']) or zeroandnot0(c['N'], c['S']):
    print('No')
else:
    print('Yes')
