N,L,*A=map(int,open(0).read().split())
for i,a,b in zip(range(1,N),A,A[1:]):
    if a+b>=L:print("Possible",*range(1,i));print(*range(N-1,i-1,-1));quit()
print("Impossible")