#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from collections import Counter
def resolve():
    S=input()
    a=[s in S for s in"NSEW"]
    if a[0]==a[1] and a[2]==a[3]:
        print("Yes")
        return
    print("No")
    #print()
#%%submit!
resolve()
