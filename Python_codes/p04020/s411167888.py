n = int(input())

A = [0]*(n+1)

ans = 0
for i in range(n):
    A[i] = int(input())
    
    
for i in range(n):
    ans += A[i]//2
    A[i] = A[i]%2
    
    if A[i] and A[i+1]:
        ans += 1
        A[i+1] -= 1
        
print(ans)