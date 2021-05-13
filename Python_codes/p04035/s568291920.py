n,l=map(int,raw_input().split())
a=map(int,raw_input().split())
ans=[]
f=-1
for i in range(n-1):
    if a[i]+a[i+1]>=l:
        f=i
        break
if f==-1:
    print 'Impossible'
else:
    print 'Possible'
    for i in range(f):
        print i+1
    for i in range(n-1,f,-1):
        print i