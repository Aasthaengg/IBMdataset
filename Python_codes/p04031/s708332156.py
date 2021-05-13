from math import floor, ceil


n = int(input())
A = list(map(int, input().split()))

x = sum(A) / n
if abs(floor(x) - x) < abs(ceil(x) - x):
    x = floor(x)
else:
    x = ceil(x)

answer = 0
for a in A:
    answer += (a - x)**2

print(answer)
