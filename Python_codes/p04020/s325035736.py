N = int(input())
A = [int(input()) for _ in range(N)]
A.append(0)

con = False
ans = 0

for i in range(N):
    if A[i] >=2:
        ans += A[i]//2
        A[i] -= (A[i]//2)*2
    
    mm = min(A[i+1],A[i])
    ans += mm
    A[i+1] -= mm
    A[i] -= mm
    #print(A)


print(ans)