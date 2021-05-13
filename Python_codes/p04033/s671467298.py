# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

a,b=map(int,input().split())
if a*b<0:
    print('Zero')
elif a<0 and ((b>0 and a%2) or (b<0 and (b-a+1)%2)):
    print('Negative')
else:
    print('Positive')