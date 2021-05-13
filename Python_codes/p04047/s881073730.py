#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = input()
l = sorted(list(map(int, input().split())))
i = 0
sum = 0
while (i < len(l) - 1):
  sum += l[i]
  i += 2
print(sum)
