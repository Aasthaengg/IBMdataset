n = int(input())
l = list(map(int, input().split()))
l = sorted(l, reverse=True)
t = 0
for i in range(1, n * 2, 2):
    t += min(l[i], l[i-1])
print(t)
