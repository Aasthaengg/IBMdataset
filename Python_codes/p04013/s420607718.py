import numpy as np


n, a = map(int, input().split())
X = np.array(list(map(int, input().split())))
X -= a

plus = X[X > 0]
zero = X[X == 0]
minus = abs(X[X < 0])

num_count = np.zeros(2551, dtype=np.int64)
num_count[0] = 1

for num in plus:
    num_count[num:] = num_count[:-num] + num_count[num:]

for num in minus:
    num_count[:-num] = num_count[:-num] + num_count[num:]

ans = 2 ** len(zero) * (num_count[0])

print(ans-1)
