N=int(input())
a = list(map(int,input().split()))
res = 10**18
for val in range(-100,101):
    tmp = sum([(val-val2)**2 for val2 in a])
    res = min(res,tmp)
print(res)