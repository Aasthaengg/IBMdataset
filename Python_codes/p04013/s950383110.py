N,A=map(int, input().split())
x=tuple(map(lambda i:int(i)-A,input().split()))
l=[0]*5001
l[0]=1
for i in x:
    f=l.copy()
    for j in range(-2500,2501):
        if l[j]:
            f[i+j]+=l[j]
    l=f.copy()
print(l[0]-1)