n,k=map(int,input().split())
l=list(map(int,input().split()))
tmp=0
for i in range(1,n):
    if l[i-1]+l[i]>=k:
        tmp=i
        break
if tmp==0:
    print("Impossible")
else:
    print("Possible")
    for i in range(1,tmp):
        print(i)
    for i in range(n-1,tmp,-1):
        print(i)
    print(tmp)