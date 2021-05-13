N =int(input())
L =[int(j) for j in input().split()]
L.sort()
ans=0
for i in range(0,2*N-1,2):
    ans+=min(L[i:i+2])
print(ans)