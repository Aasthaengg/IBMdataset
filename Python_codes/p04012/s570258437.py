import collections
w=str(input())
cc=collections.Counter(w)

a=list(cc.values())
for ans in a:
    if ans%2!=0:
        print('No')
        exit()
    
print('Yes')