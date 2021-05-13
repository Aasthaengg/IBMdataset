import math

n = int(input())
s = list(map(int,input().split()))

b = c = 0
for i in s:
    b += i
    c += i**2

if b%n == 0:
    print(int(c-b**2/n))
else:
    koho1 = math.floor(b/n)
    koho2 = math.ceil(b/n)
    ans = min(n*(koho1**2)-2*b*koho1+c,n*(koho2**2)-2*b*koho2+c)
    print(ans)