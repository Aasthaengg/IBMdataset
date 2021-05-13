n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    ans += l[2 * i]
print(ans)