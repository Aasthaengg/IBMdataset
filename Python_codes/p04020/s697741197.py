ans=0
c=0
for i in range(int(input())):
    k=int(input())
    if k:c+=k
    else:ans+=c//2;c=0
print(ans+c//2)