flag=True
a=list(input())
a=sorted(a)
while len(a)>0 and flag:
    n=a.count(a[0])
    if n%2==0:
        a=a[n:]
    else:
        flag=False
if flag:
    print("Yes")
else:
    print("No")    