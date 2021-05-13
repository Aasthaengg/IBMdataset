#!/usr/bin/python

import sys

kusi = int(input())
kusi_len = input().rstrip().split(" ")
cnt = 0
ans = 0
for line in sorted(kusi_len, key=int):
  cnt += 1
  if cnt == 1:
    a = int(line)
  elif cnt == 2:
    b = int(line)
    if a <= b:
      ans = ans + a
    else:
      ans = ans + b
    cnt = 0
print(ans)
