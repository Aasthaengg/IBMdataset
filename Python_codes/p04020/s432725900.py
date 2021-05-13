N,*A=map(int, open(0).read().split())
acc=A[0]&1
ans=A[0]//2
for a in A[1:]:
    b=min(acc,a)
    ans+=b
    a-=b
    ans+=a//2
    acc=a&1
ans+=acc//2
print(ans)