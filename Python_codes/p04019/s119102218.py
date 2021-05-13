#! /usr/bin/env python3

import sys
import numpy as np
from collections import defaultdict
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

S = readline().decode().rstrip()
dicts = defaultdict(int)

for c in S:
  dicts[c] += 1

for pair in [('N', 'S'), ('W', 'E')]:
  if min(dicts[pair[0]], dicts[pair[1]]) == 0:
    if max(dicts[pair[0]], dicts[pair[1]]) != 0:
      print('No')
      sys.exit()
print('Yes')

