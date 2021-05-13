n=int(input())
a = list(map(int,input().split()))

ans = 10**7
for i in range(102):
    p = 0
    m = 0
    for j, aa in enumerate(a):
        p += (aa-i)**2
        m += (aa+i)**2
    ans = min(ans,p,m)

print(ans)
