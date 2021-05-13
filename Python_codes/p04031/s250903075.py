import copy

N = int(input())
a = list(map(int,input().split()))

res = 1e+9
for i in range(min(a),max(a)+1):
    tmp = copy.copy(a)
    res = min(res,sum(map(lambda x:(x-i)**2,tmp)))
print(res)
