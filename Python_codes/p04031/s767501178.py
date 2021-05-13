n = int(input())
ls = list(map(int,input().split()))
md = round(sum(ls)/n)
p = 0
for i in ls:
    p += (md-i)**2
print(p)