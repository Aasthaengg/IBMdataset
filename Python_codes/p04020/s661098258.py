n = int(input())
a = [int(input()) for _ in range(n)]
a.append(0)
ans = 0
for i in range(n):
    p,r = divmod(a[i],2)
    ans += p
    if a[i+1]: a[i+1] += r
print(ans)