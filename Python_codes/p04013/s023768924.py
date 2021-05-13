# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,A=map(int,input().split())
    x=list(map(int,input().split()))
    dp=[[[0]*2501 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0]=1
    for i in range(N):
        for j in range(i+1):
            for k in range(2501):
                dp[i+1][j][k]+=dp[i][j][k]
                if k-x[i]>=0 and j<=i:
                    dp[i+1][j+1][k]+=dp[i][j][k-x[i]]
    ans=0
    for i in range(1,N+1):
        ans+=dp[-1][i][i*A]
    print(ans)

if __name__ == '__main__':
    main()
