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
    N,L=map(int,input().split())
    a=tuple(map(int,input().split()))
    for i in range(N-1):
        if a[i]+a[i+1]>=L:
            print('Possible')
            for j in range(i):
                print(j+1)
            for j in range(N-2,i,-1):
                print(j+1)
            print(i+1)
            break
    else:
        print('Impossible')

if __name__ == '__main__':
    main()
