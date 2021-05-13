N=int(input())
A=[0]*N
for i in range(N):
    A[i]=int(input())
B   = [0]*N
B[0]= A[0] %2
ans= A[0]//2

for i in range(1,N):
    #print(i,A[i],B[i-1], (B[i-1]+A[i])//2 )
    pair= (B[i-1]+A[i])//2
    ans += pair
    if (A[i]+B[i-1]) %2==1 and A[i]!=0:
        B[i] = 1
    else:
        B[i] = 0

print(ans)
