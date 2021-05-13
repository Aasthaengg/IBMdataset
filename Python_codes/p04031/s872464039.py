def sigma(a,r):
    t=0
    for i in a:
        t+=(i-r)**2
    return t

_=int(input())
a=list(map(int,input().split()))
s=min([sigma(a,r) for r in range(-100,101)])
print(s)
