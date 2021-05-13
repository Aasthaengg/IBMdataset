n = int(input())
A = list(map(int,input().split()))
ans = float("inf")

for i in range(min(A),max(A)+1):
    cost = 0
    
    for j in A:
        cost += (j-i)**2
        
    ans = min(ans,cost)
    
print(ans)