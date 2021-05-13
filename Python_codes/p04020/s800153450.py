n=int(input())
count=0
ans=0
for i in range(n):
    a=int(input())
    if a==0:
        ans+=(count//2)
        count=0
    else:
        count+=a
print(ans+count//2)