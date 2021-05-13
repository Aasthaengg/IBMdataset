N = int(input())
A = list(map(int, input().split()))
cost = float("inf")
for i in range(-100, 101):
    tmp_cost = 0
    for a in A:
        tmp_cost += (a - i) ** 2
    cost = min(tmp_cost, cost)
print(cost)