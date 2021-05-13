N,L=map(int,input().split())
A=list(map(int,input().split()))

if N==2:
    if sum(A)>=L:
        print("Possible")
        print("1")
        exit()
    else:
        print("Impossible")
        exit()
ans=[]
for i in range(N-1):
    if A[i]+A[i+1]>=L:
        last=i
        for j in range(i):
            ans.append(j)
        for j in range(N-2,i,-1):
            ans.append(j)
        break

if len(ans)==0:
    print("Impossible")
    exit()

ans.append(last)

print("Possible")
for i in range(N-1):
    print(ans[i]+1)