import math
H, W, A, B = map(int,input().split())
e = 10**9 + 7
def power(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a % e
    elif b%2 == 0:
        return power(a,b//2)**2 % e
    else:
        return power(a,b//2)**2*a % e
    
M = [1]
for i in range(1,H+W):
    a = M[i-1]*i%e
    M.append(a)
N= [0]*(H+W)
N[H+W-1] = power(M[H+W-1], e-2)
for i in range(H+W-2, -1, -1):
    N[i] = N[i+1] * (i+1) % e

def c(a,b):
    return M[a]*N[b]*N[a-b]%e

T = 0
for i in range(W-B):
    P = c(H+W-A-i-2,H-A-1)
    Q = c(A+i-1,i)
    T = (T + P*Q)
print(T%e)