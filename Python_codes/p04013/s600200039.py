
n,k = map(int,input().split())
A = list(map(int,input().split()))
dic1 = {(0,0):1}
for i in range(n):
    dic2 = {(0,0):0}
    for (total,num),amount in dic1.items():
        if (total,num) in dic2:
            dic2[(total,num)] += amount
        else:
            dic2[(total,num)] = amount
        if (total+A[i],num+1) in dic2:
            dic2[(total+A[i],num+1)] += amount
        else:
            dic2[(total+A[i],num+1)] = amount
    
    dic1 = dic2

ans = 0
for i in range(1,n+1):
    if (i*k,i) in dic1:
        ans += dic1[(i*k,i)]

print(ans)