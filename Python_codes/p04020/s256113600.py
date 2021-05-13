import sys

N = int(sys.stdin.readline().rstrip())

A = []
for _ in range(N):
    A.append(int(sys.stdin.readline().rstrip()))

pairs = 0
res = 0
for a_i in A:
    if a_i == 0:
        res = 0
        continue
    
    a_i += res
    r = a_i // 2
    pairs += r
    res = a_i - 2*r

print(pairs)