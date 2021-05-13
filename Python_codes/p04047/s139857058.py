n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
c=0
for i in range(1,2*n,2):
    c+=l[i]
print(c)
