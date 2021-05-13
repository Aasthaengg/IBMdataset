from sys import stdin
N = int(stdin.readline().rstrip())
A = []
for i in range(N):
    A.append(int(input()))
    
ans = 0
for i in range(N-1):
    ans += (A[i]//2)
    A[i+1] -= min(A[i+1],A[i]%2)
    ans += min(A[i+1],A[i]%2)
ans += (A[-1]//2)
print(ans)