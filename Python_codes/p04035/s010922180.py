n,l=map(int,input().split())
a=list(map(int,input().split()))

flag=0
for i in range(n-1):
    if a[i]+a[i+1]>=l:
        flag=1
        break

if flag==0:
    print("Impossible")
else:
    print("Possible")
    if i>0:
        for j in range(1,i+1):
            print(j)
    if i+2<n:
        tmp=[]
        for j in range(i+2,n):
            tmp.append(j)
        for item in tmp[::-1]:
            print(item)
    print(i+1)


