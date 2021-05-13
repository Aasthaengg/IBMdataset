import sys
input = sys.stdin.readline
INF = 10**10
MOD = 10**9 + 7
sys.setrecursionlimit(100000000)
from functools import lru_cache
from itertools import permutations
from math import factorial


def main():
    n,a = map(int,input().split())
    x = list(map(int,input().split()))
    dp = [[[0] * (n * a + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0][0] = 1

    for i in range(n):
        num = x[i]
        for j in range(1,n + 1):
            for s in range(n * a + 1):
                if s - num >= 0:
                    dp[i + 1][j][s] = dp[i][j][s] + dp[i][j - 1][s - num]
                else:
                    dp[i + 1][j][s] = dp[i][j][s]
    
    ans = 0
    for i in range(1,n + 1):
        ans += dp[-1][i][i * a]
    print(ans)
    

if __name__=='__main__':
    main() 