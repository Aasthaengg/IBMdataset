n = int(input())
a1 = int(input())
flag = a1%2
ans = a1//2
for i in range(n-1):
    a = int(input())
    if flag:
        ans+=1 if 0<a else 0
        ans+=(a-1)//2 if a!=0 else 0
        flag=1 if a!=0 and (a-1)%2==1 else 0
    else:
        ans +=a//2
        flag=a%2
print(ans)