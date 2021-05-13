n=int(input())
a=list(map(int,input().split()))
total=0
ans1=0
ans2=0
for i in a:
    total+=i
tmp1=total//n
tmp2=-(-total//n)
for i in a:
    ans1+=(i-tmp1)**2
for i in a:
    ans2+=(i-tmp2)**2
print(min(ans1,ans2))