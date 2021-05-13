N=int(input())
L=list(map(int,input().split()))
L.sort(reverse=True)
x=0
for i in range(len(L)):
    if i%2!=0:
        x+=L[i]
print(x)