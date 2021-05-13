m=10**9+7
h,w,a,b=map(int,input().split())
d=c=1
for i in range(h-1):
    d=c=c*(w+h-b-2-i)*pow(i+1,m-2,m)%m
for i in range(1,h-a):
    c=c*(b-1+i)*(h-i)*pow(i*(w+h-b-1-i),m-2,m)%m
    d+=c
print(d%m)