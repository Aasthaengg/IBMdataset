from collections import defaultdict
 
n, k = map(int, input().split())
x = [int(i) for i in input().split()]
x = [i-k for i in x]
dic = defaultdict(int)

dic[0]=1
for i in x:
    for k,v in list(dic.items()):
        dic[k+i]+=v
print(dic[0]-1)

