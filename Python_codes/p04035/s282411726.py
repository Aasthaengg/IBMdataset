import sys
input=sys.stdin.readline

n,l=map(int,input().split())
a=list(map(int,input().split()))

x=-1
for i in range(n-1):
    if a[i]+a[i+1]>=l:
        x=i
        break

if x==-1:
    print('Impossible')
else:
    print('Possible')
    for i in range(x):
        print(i+1)
    for i in range(n-2,x,-1):
        print(i+1)
    print(x+1)