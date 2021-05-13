n,*aa = map(int, open(0).read().split())

ans = 0
for i in range(n):
    ans += aa[i]//2
    if aa[i]%2 and i+1<n and aa[i+1]:
        ans += 1
        aa[i+1] -= 1

print(ans)