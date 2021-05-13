n = int(input())

ans = x = 0
for _ in range(n):
    a = int(input())
    if a == 0:
        ans += x//2
        x = 0
    x += a
else:
    ans += x//2

print(ans)