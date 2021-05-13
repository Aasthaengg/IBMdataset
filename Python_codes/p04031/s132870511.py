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
    N=int(input())
    a=list(map(int,input().split()))
    ans=INF
    for i in range(-100,101):
        tmp=0
        for x in a:
            tmp+=(x-i)**2
        ans=min(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()
