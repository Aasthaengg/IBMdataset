N = int(input())
A = list(map(int,input().split()))
ans=10000000
for i in range(-100, 101):
    sum=0
    for a in range(len(A)):
        sum+=(A[a]-i)**2
    ans=min(ans,sum)
print(ans)