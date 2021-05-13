n,l=map(int,raw_input().split())
a=map(int,raw_input().split())
fknot=0
for i in xrange(n-1):
    if a[i]+a[i+1]>=l:
        fknot=i+1
if fknot==0:
    print("Impossible")
else:
    print("Possible")
    for i in xrange(n-1,fknot,-1):
        print(i)
    for i in xrange(1,fknot):
        print(i)
    print(fknot)