import sys
import numpy as np

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split())) # applies to only numbers
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces
sys.setrecursionlimit(10 ** 7)

N, L = rl()
A = np.array(rl())
couple = A[:-1] + A[1:]
if couple.max() < L:
    print('Impossible')
    exit()
print('Possible')
index = np.nonzero(couple>=L)[0][0] + 1
for i in range(1, N):
    if i == index:
        break
    print(i)
for i in range(N-1, 0, -1):
    if i == index:
        break
    print(i)

print(index)
# 43
