n,l=map(int,input().split())
a=[int(j)for j in input().split()]
for i in range(1,n):
    if a[i-1]+a[i]>=l:
        print("Possible")
        for j in range(i+1,n)[::-1]:
            print(j)
        for j in range(1,i+1):
            print(j)
        exit()
print("Impossible")