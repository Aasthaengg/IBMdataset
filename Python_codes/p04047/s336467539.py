# -*- coding: utf-8 -*-
n = int(input())
l_list = list(map(int, input().split()))
counter = 0
for i in range(2 * n):
    if i % 2 == 0:
        counter += sorted(l_list)[i]
print(counter)