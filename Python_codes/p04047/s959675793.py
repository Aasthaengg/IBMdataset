N = int(input())
kushi = list(map(int,input().split()))
kushi.sort()
ans = 0
for i in range(0,2*N,2):
    ans += min(kushi[i],kushi[i+1])
print(ans)
