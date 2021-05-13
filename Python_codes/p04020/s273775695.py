#coding:utf-8
import sys,os
from collections import defaultdict, deque
from fractions import gcd
from math import ceil, floor
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    XLMIIS = lambda x: [LMIIS() for _ in range(x)]
    YN = lambda c : print('Yes') if c else print('No')
    MOD = 10**9+7

    N = II()
    
    ans = 0
    isPreEven = False

    for _ in range(N):
        a = II()
        if isPreEven and a > 0:
            ans += 1
            a -= 1
        ans += a // 2
        if a % 2 == 1:
            isPreEven = True
        else:
            isPreEven = False
        

    
    print(ans)


if __name__ == '__main__':
    main()