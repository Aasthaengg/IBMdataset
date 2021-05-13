from sys import stdin
input = stdin.readline

L = list(map(int, input().split()))

T = [5,5,7]

for l in L:
    if l in T:
        T.pop(T.index(l))
if T:
    print('NO')
else:
    print('YES')