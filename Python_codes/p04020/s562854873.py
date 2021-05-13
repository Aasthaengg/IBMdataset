N=int(input())
A=[0]*N
for i in range(N):
    A[i]=int(input())
A.append(0)

K=0
S=0
for a in A:
    if a:
        S+=a
    else:
        K+=S//2
        S=0

print(K)