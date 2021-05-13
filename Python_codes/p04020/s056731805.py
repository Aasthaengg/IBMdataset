import sys
INF = 10 ** 10
MOD = 10 ** 9 + 7
from functools import lru_cache
sys.setrecursionlimit(100000000)

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    ans = 0
    for i in range(n):
        ans += a[i]//2
        if i != n - 1:
            if a[i]%2 == 1 and a[i + 1] > 0:
                ans += 1
                a[i + 1] -= 1
    
    print(ans)
if __name__ =='__main__':
    main()    