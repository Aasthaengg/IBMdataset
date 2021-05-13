n = int(input())
a = list(map(int,input().split()))
asrt = sorted(a,reverse=True)
ans = 0
for v in range(1,2*n,2):
    ans += asrt[v]
print(str(ans))