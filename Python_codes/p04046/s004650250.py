h,w,a,b=map(int,input().split());m=10**9+7;f=[1]
for i in range(h+w):f+=[f[-1]*(i+1)%m]
def comb(a,b,m):return f[a]*pow(f[b],m-2,m)*pow(f[a-b],m-2,m)%m
x=0
for i in range(b,w):x+=comb(h-a+i-1,i,m)*comb(a+w-i-2,a-1,m)%m
print(x%m)