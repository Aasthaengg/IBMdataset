n = int(input())
l = list(map(int, input().split()))

l = sorted(l)
count = sum(l[i] for i in range(0, 2 * n, 2))
print(count)
