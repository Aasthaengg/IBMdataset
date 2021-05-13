# coding: utf-8
# Your code here!

N = int(input())
a = sorted(list(map(int, input().split())))
ctr = 0

for i in range(N * 2):
    if i % 2 == 0:
        ctr += a[i]
print(ctr)