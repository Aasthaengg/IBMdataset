n = int(input())
l = list(map(int,input().split()))
l = sorted(l)
ans = 0
for i in range(0,2*n-1,2):
    ans +=min(l[i],l[i+1])
print(ans)