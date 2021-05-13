N = int(input())
a = list(map(int,input().split()))
b = sum(a)
b =  int((b+0.5*N) // N)
ans = 0
for i in range(N):
    ans += (a[i]-b)**2
print(ans)