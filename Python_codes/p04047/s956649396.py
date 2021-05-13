n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
i = 0
while i <= n * 2 - 1:
    ans += min(l[i], l[i+1])
    i += 2
print(ans)