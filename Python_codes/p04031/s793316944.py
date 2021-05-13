import os, sys, re, math

N = int(input())
a = [int(s) for s in input().split(' ')]

ret = float('inf')
for i in range(-100,101):
    s = 0
    for aj in a:
        s += (aj - i) ** 2
    ret = min(ret,s)

print(ret)
