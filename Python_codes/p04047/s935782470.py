n = int(input())
l = list(map(int, input().split()))

l.sort()
ans = sum(l[::2])
print(ans)
