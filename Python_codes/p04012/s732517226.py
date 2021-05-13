# -*- coding:utf-8 -*-
import sys
# input = sys.stdin.readline
w = list(input())
w_set = set(w)
for i in w_set:
  if w.count(i)%2==1:
    print("No")
    sys.exit()
  else:
    continue
print("Yes")