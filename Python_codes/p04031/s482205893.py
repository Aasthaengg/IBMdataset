n = int(input())
A = list(map(int, input().split()))
min_cost = float("inf")
for num in range(-100, 101):
    cost = 0
    for a in A:
        cost += (a - num) ** 2
    min_cost = min(min_cost, cost)
print(min_cost)