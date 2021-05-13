n = int(input())
a = list(map(int, input().split()))

a_min = min(a)
a_max = max(a)

a_sum = []
for i in range(a_min, a_max + 1):
    num=0
    for j in range(n):
        num += (a[j] - i) ** 2
    a_sum.append(num)
print(min(a_sum))