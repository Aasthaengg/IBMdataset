n=int(input())
a=list(int(input()) for _ in range(n))
s=0
r=0
for i in range(n):
    if a[i]==0:
        r=0
    else:
        s+=(a[i]+r)//2
        r=(a[i]+r)%2
print(s)