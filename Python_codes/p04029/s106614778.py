n = int(input())
ans = 1
b = 1
for i in range(n-1):
    b += 1
    ans += b
print(ans)