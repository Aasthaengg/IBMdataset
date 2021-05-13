n = int(input())
ans = 0
r = 0
for i in range(n):
    a = int(input())
    if a == 0:
        r = 0
        continue
    else:
        ans += (a + r) // 2
        r = (a + r) % 2
print(ans)