import numpy as np
N = int(input())
A = np.array([int(input()) for _ in range(N)])
ans = 0
for i in range(N-1):
    d,m = divmod(A[i],2)
    ans += d
    if m == 1:
        if A[i+1] > 0:
            A[i+1] -= 1
            ans += 1

ans += A[-1]//2
print(ans)