n = int(input())
a = list(map(int, input().split()))
ans = 0

a.sort(reverse=True)

for i in range(1,n+1):
    ans += a[2*i-1]

print(ans)