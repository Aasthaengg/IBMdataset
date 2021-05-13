n = int(input())
a = list(map(int, input().split()))

i = 0
m = 100
M = -100

s = 0
while i < n:
    s += a[i]
    i+=1

s1 = s//n
s2 = s1 + 1

i = 0
x1 = 0
x2 = 0
while i < n:
    x1 += (s1-a[i])**2
    x2 += (s2-a[i])**2
    i+=1

if x1<x2:
    ans = x1
else:
    ans = x2
print(ans)

