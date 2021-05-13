import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

a, b = ri_()
if a == 0 or b == 0 or (a < 0 and b > 0):
    ans = 'Zero'
elif a > 0 and b > 0:
    ans = 'Positive'
else:
    if (b - a + 1) % 2 == 0:
        ans = 'Positive'
    else:
        ans = 'Negative'
print(ans)