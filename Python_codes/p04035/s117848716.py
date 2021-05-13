N,L=map(int,input().split())

a=list(map(int,input().split()))


for i in range(1,len(a)):
    if a[i]+a[i-1]<L:
        pass
    else:
        print("Possible")
        for j in range(1,i):
            print(j)
        for k in range(len(a)-i-1):
            print(len(a)-1-k)
        print(i)
        exit()
print("Impossible")