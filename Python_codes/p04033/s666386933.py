#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

a,b = map(int,input().split())
if a > 0:
  print("Positive")
elif a <= 0 and 0 <= b:
  print("Zero")
else:
  if (b-a) % 2 == 1:
    print("Positive")
  else:
    print("Negative")