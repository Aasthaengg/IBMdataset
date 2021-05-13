n = int(input())
a = [0]*n
res = 0
tmp = 0
zero = False
for i in range(n):
    s = int(input())
    a[i] = s
    if s==0:
        zero = True
if not zero:
    print(sum(a)//2)
    exit()

for i in range(n):
    if a[i]!=0:
        tmp+=a[i]
    else:
        res+=tmp//2
        tmp = 0
    if i==n-1 and tmp>1:
        res+=tmp//2
print(res)
