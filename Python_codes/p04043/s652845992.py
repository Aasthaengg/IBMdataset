import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B,C = MI()
if A == B == 5 and C == 7:
    print('YES')
elif A == C == 5 and B == 7:
    print('YES')
elif B == C == 5 and A == 7:
    print('YES')
else:
    print('NO')