n, l = map(int, input().split())
s = sorted([input() for i in range(n)])
ans = ""
for i in s:
    ans += i
print(ans)