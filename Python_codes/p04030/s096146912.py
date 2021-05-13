# -*- coding:utf-8 -*-
import sys
from collections import deque
input = sys.stdin.readline
s = list(input())
d = deque()
for i in s:
  if (i=='B')&(len(d)!=0):
    d.pop()
  elif (i=='B')&(len(d)==0):
    continue
  else:
    d.append(i)
print(''.join(list(d)))