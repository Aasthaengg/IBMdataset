# -*- coding: utf-8 -*-
#abc042
a, b, c=map(int, input().split())

A=[a,b,c]

if A in [[5,5,7], [5,7,5], [7,5,5]]:
    print("YES")
else:
    print("NO")
