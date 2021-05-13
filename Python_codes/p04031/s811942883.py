N = int(input())
a = [int(x) for x in input().split()]
ans = []
for i in range(-100, 101, 1):
    v = 0
    for j in range(N):
        v += (a[j] - i) ** 2
    ans.append(v)
print(min(ans))
