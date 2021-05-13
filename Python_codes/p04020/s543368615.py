#  --*-coding:utf-8-*--

N = int(input())
A = list(int(input()) for _ in range(N))

s = 0
s2 = 0

for a in A:
    if a != 0:
        s2 += a
    else:
        s += s2//2
        s2 = 0

s += s2//2

print(s)
