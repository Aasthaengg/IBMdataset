N=int(input())
L=list(map(int,input().split()))

L.sort()

ans=sum(L[0:2*N:2])
print(ans)