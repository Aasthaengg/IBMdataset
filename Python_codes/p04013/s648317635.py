from collections import Counter
n,a=map(int,input().split())
X=sorted(list(map(lambda x:int(x)-a,input().split())))
ans=Counter([0])
for x in X:
    tmp=Counter()
    for i,j in ans.items():
        tmp[i+x]+=j
    ans+=tmp
print(ans[0]-1)

