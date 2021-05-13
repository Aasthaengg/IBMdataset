N = int(input())
A = [int(input()) for i in range(N)]
ans = 0
for i in range(N-1):
    ans += (A[i] + A[i+1])//2
    A[i+1] = min(A[i+1], (A[i] + A[i+1]) % 2)
if N == 1:
    print(A[0]//2)
    exit()
print(ans)
