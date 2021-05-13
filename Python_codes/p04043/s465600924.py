# -*- coding: utf-8 -*-

l = list(map(int, input().split()))
l_s = sorted(l)
l_r = [5, 5, 7]

if l_s == l_r:
    print('YES')
else:
    print('NO')