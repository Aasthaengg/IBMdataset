N = int(input())
a = sorted(list(map(int, input().split())))
answer = 10000000
for i in range(a[0], a[-1] + 1):
    cost = 0
    for num in a:
        cost += ((num - i) ** 2)
    answer = min(answer, cost)
print(answer)
