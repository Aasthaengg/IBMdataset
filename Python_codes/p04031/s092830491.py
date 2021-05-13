n = int(input())
x = list(map(int,input().split()))
ave = sum(x)//n
sum1=0
sum2=0
for i in range(n):
    sum1+=(x[i]-ave)*(x[i]-ave)
    sum2+=(x[i]-ave-1)*(x[i]-ave-1)
print(min(sum1,sum2))
