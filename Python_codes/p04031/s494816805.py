# -*- coding:utf-8 -*-
import sys,math,statistics
input = sys.stdin.readline
n = int(input())
a = [int(_) for _ in input().split()]
c1 = math.floor(statistics.mean(a))
c2 = math.ceil(statistics.mean(a))
a1 = sum([(i-c1)**2 for i in a])
a2 = sum([(i-c2)**2 for i in a])
print(min(a1,a2))