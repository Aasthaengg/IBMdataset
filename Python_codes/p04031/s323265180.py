import math
N = int(input())
A = list(map(int, input().split()))

ave = sum(A)//N
cost1 = 0
cost2 = 0
cost = []
for i in A:
    cost1 += math.pow((i - ave), 2)
cost.append(cost1)

for i in A:
    cost2 += math.pow((i - ave - 1), 2)
cost.append(cost2)


print(int(min(cost)))
