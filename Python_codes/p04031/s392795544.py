n = int(input())
a = list(map(int,input().split()))
asum = sum(a)
a2sum = 0
for m in a:
  a2sum += m**2
x1 = asum//n
x2 = x1+1
z1 = n*x1**2-2*asum*x1+a2sum
z2 = n*x2**2-2*asum*x2+a2sum
print(min(z1,z2))