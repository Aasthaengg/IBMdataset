# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
s = [int(_) for _ in input().split()]

if (s.count(7)==1)&(s.count(5)==2):
  print('YES')
else:
  print('NO')