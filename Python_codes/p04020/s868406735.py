n = int(input())
ans = 0
x = 0
for i in range(n):
    a = int(input())
    ans += (a + x) // 2
    x = (a + x) % 2 if a != 0 else 0
    #print(a, x, ans)
print(ans)