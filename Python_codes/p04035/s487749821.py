# coding: utf-8
N, L = map(int, input().split())
A = list(map(int, input().split()))
flag = True
l = -1
for i in range(N-1):
    if A[i] + A[i+1] >= L:
        l = i+1
if l < 0:
    print("Impossible")
    exit()
knot = list(range(1, N))
print("Possible")
idx = 1
while idx < l:
    print(idx)
    idx += 1
idx = N-1
while idx > l:
    print(idx)
    idx -= 1
print(l)