n = int(input())
ans = 0
m = 0
for i in range(n):
    a = int(input())
    ans += (m+a)//2
    m = max(0,a-m)%2
print(ans)