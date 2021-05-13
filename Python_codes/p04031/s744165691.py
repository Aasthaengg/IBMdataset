from math import ceil, floor

n = int(input())
ls = list(map(int, input().split()))
sqsm = 0
for i in range(n):
    sqsm += ls[i] * ls[i]
sm = sum(ls)
x1 = floor(sm / n)
x2 = ceil(sm / n)
print(min(sqsm + n * x1 * x1 - 2 * sm * x1, sqsm + n * x2 * x2 - 2 * sm * x2))
